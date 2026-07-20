#!/usr/bin/env python3
"""Validate the public Shadowrocket configuration without reading credentials."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs" / "shadowrocket" / "cn-smart-routing.conf"
REQUIRED_SECTIONS = ["General", "Proxy", "Proxy Group", "Rule", "Host"]
REQUIRED_LINES = {
    "dns-direct-fallback-proxy = false",
    "udp-policy-not-supported-behaviour = REJECT",
    "block-quic = all-proxy",
    "DOMAIN-SUFFIX,bytevcloud.com,DIRECT",
    "DOMAIN-SUFFIX,meeting.tencent.com,DIRECT",
    "DOMAIN-SUFFIX,wemeet.qq.com,DIRECT",
    "GEOIP,CN,DIRECT",
    "FINAL,PROXY",
}
FORBIDDEN_PATTERNS = [
    r"(?i)api[_-]?key\s*=",
    r"(?i)(token|password|passwd|secret|sessionkey)\s*=",
    r"(?i)(ss|ssr|vmess|vless|trojan)://",
    r"(?i)subscription[-_ ]?url\s*=",
]


def active_lines(block: str) -> list[str]:
    return [
        line.strip()
        for line in block.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def section(text: str, name: str) -> str:
    match = re.search(
        rf"(?ms)^\[{re.escape(name)}\]\s*$\n(.*?)(?=^\[[^\]]+\]\s*$|\Z)",
        text,
    )
    return match.group(1) if match else ""


def validate_static(text: str) -> list[str]:
    errors: list[str] = []
    found_sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", text)
    if found_sections != REQUIRED_SECTIONS:
        errors.append(f"sections mismatch: {found_sections}")

    for required in sorted(REQUIRED_LINES):
        if required not in text:
            errors.append(f"missing required line: {required}")

    rules = active_lines(section(text, "Rule"))
    if len(rules) < 150:
        errors.append(f"too few active rules: {len(rules)}")
    if rules.count("FINAL,PROXY") != 1:
        errors.append("FINAL,PROXY must appear exactly once")
    elif rules[-1] != "FINAL,PROXY":
        errors.append("FINAL,PROXY must be the last active rule")

    proxy_lines = active_lines(section(text, "Proxy"))
    group_lines = active_lines(section(text, "Proxy Group"))
    if proxy_lines:
        errors.append("[Proxy] must not contain bundled nodes")
    if group_lines:
        errors.append("[Proxy Group] must not contain automatic or fixed groups")

    remote = [
        line.split(",", 2)[1]
        for line in rules
        if line.startswith(("RULE-SET,", "DOMAIN-SET,"))
    ]
    if len(remote) != 17:
        errors.append(f"expected 17 remote rule references, found {len(remote)}")
    if any(not url.startswith("https://raw.githubusercontent.com/") for url in remote):
        errors.append("all remote rule references must use HTTPS GitHub Raw URLs")

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text):
            errors.append(f"possible credential or bundled node matched: {pattern}")

    checks = {
        "chatgpt.com": "PROXY",
        "anthropic.com": "PROXY",
        "github.com": "PROXY",
        "feishu.cn": "DIRECT",
        "bytevcloud.com": "DIRECT",
        "meeting.tencent.com": "DIRECT",
        "wemeet.qq.com": "DIRECT",
        "weixin.qq.com": "DIRECT",
        "alipay.com": "DIRECT",
        "icbc.com.cn": "DIRECT",
    }
    for domain, policy in checks.items():
        needle = f"DOMAIN-SUFFIX,{domain},{policy}"
        if needle not in rules:
            errors.append(f"missing smoke-test route: {needle}")

    realtime_rules = [
        "DOMAIN-SUFFIX,feishu.cn,DIRECT",
        "DOMAIN-SUFFIX,bytevcloud.com,DIRECT",
        "DOMAIN-SUFFIX,meeting.tencent.com,DIRECT",
        "DOMAIN-SUFFIX,wemeet.qq.com,DIRECT",
        "DOMAIN-SUFFIX,weixin.qq.com,DIRECT",
    ]
    if "GEOIP,CN,DIRECT" in rules:
        cn_fallback = rules.index("GEOIP,CN,DIRECT")
        for rule in realtime_rules:
            if rule in rules and rules.index(rule) > cn_fallback:
                errors.append(f"realtime rule must precede GEOIP,CN fallback: {rule}")

    precedence_pairs = [
        ("DOMAIN-SUFFIX,meeting.qq.com,DIRECT", "DOMAIN-SUFFIX,qq.com,DIRECT"),
        ("DOMAIN-SUFFIX,wemeet.qq.com,DIRECT", "DOMAIN-SUFFIX,qq.com,DIRECT"),
        ("DOMAIN-SUFFIX,weixin.qq.com,DIRECT", "DOMAIN-SUFFIX,qq.com,DIRECT"),
        ("DOMAIN-SUFFIX,wxwork.qq.com,DIRECT", "DOMAIN-SUFFIX,qq.com,DIRECT"),
    ]
    for specific, broad in precedence_pairs:
        if specific in rules and broad in rules and rules.index(specific) > rules.index(broad):
            errors.append(f"specific realtime rule must precede broad rule: {specific}")

    unsafe_udp_fallbacks = {
        "PROTOCOL,UDP,DIRECT",
        "PROTOCOL,UDP,PROXY",
    }
    for rule in unsafe_udp_fallbacks.intersection(rules):
        errors.append(f"broad UDP routing is not allowed: {rule}")

    return errors


def remote_urls(text: str) -> list[str]:
    rules = active_lines(section(text, "Rule"))
    return [
        line.split(",", 2)[1]
        for line in rules
        if line.startswith(("RULE-SET,", "DOMAIN-SET,"))
    ]


def validate_network(urls: list[str]) -> list[str]:
    errors: list[str] = []
    headers = {"User-Agent": "cn-smart-routing-validator/0.1"}
    for url in urls:
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status != 200:
                    errors.append(f"remote returned {response.status}: {url}")
                response.read(64)
        except Exception as exc:  # noqa: BLE001 - report remote failures uniformly
            errors.append(f"remote unavailable: {url} ({type(exc).__name__})")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--network", action="store_true", help="check remote rule URLs")
    args = parser.parse_args()

    if not CONFIG.is_file():
        print(f"FAIL: missing {CONFIG}")
        return 1

    text = CONFIG.read_text(encoding="utf-8")
    errors = validate_static(text)
    if args.network:
        errors.extend(validate_network(remote_urls(text)))

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: Shadowrocket configuration is structurally valid")
    print("PASS: no bundled nodes or obvious credentials detected")
    if args.network:
        print("PASS: all remote rule URLs are reachable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
