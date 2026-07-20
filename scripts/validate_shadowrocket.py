#!/usr/bin/env python3
"""Validate the public Shadowrocket configuration without reading credentials."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs" / "shadowrocket" / "cn-smart-routing.conf"
VERSION_FILE = ROOT / "VERSION"
MANIFEST = ROOT / "manifest.json"
BLACKMATRIX_COMMIT = "e69663d642551aa3e0164a656179335a896127ad"
BLACKMATRIX_BASE = (
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/"
    f"{BLACKMATRIX_COMMIT}/"
)
FEISHU_REFERENCE_COMMIT = "6baf0076c10bc87b9f9d30221254fdbd97f0f221"
REQUIRED_SECTIONS = ["General", "Proxy", "Proxy Group", "Rule", "Host"]
REQUIRED_LINES = {
    "dns-direct-fallback-proxy = false",
    "udp-policy-not-supported-behaviour = REJECT",
    "block-quic = all-proxy",
    "DOMAIN-SUFFIX,bytevcloud.com,DIRECT",
    "DOMAIN-SUFFIX,baseopendev.com,DIRECT",
    "DOMAIN-SUFFIX,feishu-3rd-party-services.com,DIRECT",
    "DOMAIN-SUFFIX,feishuimg.com,DIRECT",
    "DOMAIN-SUFFIX,feishupkg.com,DIRECT",
    "DOMAIN-SUFFIX,larkoffice.com,DIRECT",
    "DOMAIN-SUFFIX,bytehwm.com,DIRECT",
    "DOMAIN-SUFFIX,ttwebview.com,DIRECT",
    "DOMAIN-SUFFIX,volcvideo.com,DIRECT",
    "DOMAIN-SUFFIX,meeting.tencent.com,DIRECT",
    "DOMAIN-SUFFIX,wemeet.qq.com,DIRECT",
    f"RULE-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/Copilot/Copilot.list,PROXY,force-remote-dns",
    f"RULE-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/Notion/Notion.list,PROXY,force-remote-dns",
    f"RULE-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/Slack/Slack.list,PROXY,force-remote-dns",
    f"RULE-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/Teams/Teams.list,PROXY,force-remote-dns",
    f"RULE-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/ChinaMax/ChinaMax.list,DIRECT",
    f"DOMAIN-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/ChinaMax/ChinaMax_Domain.list,DIRECT",
    "GEOIP,CN,DIRECT",
    "FINAL,PROXY",
}
FORBIDDEN_PATTERNS = [
    r"(?i)api[_-]?key\s*=",
    r"(?i)(token|password|passwd|secret|sessionkey)\s*=",
    r"(?i)(ss|ssr|vmess|vless|trojan)://",
    r"(?i)subscription[-_ ]?url\s*=",
]
UPSTREAM_URLS = {
    "feishu": (
        "https://raw.githubusercontent.com/icewithcola/Clash-Rule-Set/"
        f"{FEISHU_REFERENCE_COMMIT}/feishu.yaml"
    ),
    "chinamax": f"{BLACKMATRIX_BASE}rule/Shadowrocket/ChinaMax/ChinaMax.list",
    "chinamax_domains": (
        f"{BLACKMATRIX_BASE}rule/Shadowrocket/ChinaMax/ChinaMax_Domain.list"
    ),
    "tencent_meeting": "https://cdn.meeting.tencent.com/upload/firewall/domain_ip.json",
}


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
    if len(remote) != 20:
        errors.append(f"expected 20 remote rule references, found {len(remote)}")
    if any(not url.startswith(BLACKMATRIX_BASE) for url in remote):
        errors.append("all runtime rule references must use the pinned Blackmatrix commit")
    if any("/master/" in url or "/main/" in url for url in remote):
        errors.append("runtime rule references must not follow a moving branch")

    chinamax_rules = {
        f"DOMAIN-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/ChinaMax/ChinaMax_Domain.list,DIRECT",
        f"RULE-SET,{BLACKMATRIX_BASE}rule/Shadowrocket/ChinaMax/ChinaMax.list,DIRECT",
    }
    first_chinamax = min(
        (rules.index(rule) for rule in chinamax_rules if rule in rules),
        default=len(rules),
    )
    for rule in rules:
        if rule.startswith(("RULE-SET,", "DOMAIN-SET,")) and ",PROXY" in rule:
            if rules.index(rule) > first_chinamax:
                errors.append(f"overseas rule must precede ChinaMax: {rule}")

    redundant_domestic_sources = (
        "/DingTalk/DingTalk.list,DIRECT",
        "/WeChat/WeChat.list,DIRECT",
        "/ByteDance/ByteDance.list,DIRECT",
        "/Tencent/Tencent.list,DIRECT",
        "/Tencent/Tencent_Domain.list,DIRECT",
        "/NetEase/NetEase.list,DIRECT",
        "/TapTap/TapTap.list,DIRECT",
        "/China/China.list,DIRECT",
        "/China/China_Domain.list,DIRECT",
    )
    for source in redundant_domestic_sources:
        if any(source in rule for rule in rules):
            errors.append(f"domestic source duplicates ChinaMax: {source}")

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


def validate_manifest(config_text: str) -> list[str]:
    """Validate the minimal release manifest against the canonical config."""
    errors: list[str] = []
    if not VERSION_FILE.is_file():
        return ["missing VERSION"]
    if not MANIFEST.is_file():
        return ["missing manifest.json"]

    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    expected_channel = "release-candidate" if "-rc." in version else "stable"
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return [f"invalid manifest.json ({type(exc).__name__})"]

    expected_sha256 = hashlib.sha256(config_text.encode("utf-8")).hexdigest()
    checks = {
        "manifest version": (manifest.get("version"), version),
        "manifest channel": (manifest.get("channel"), expected_channel),
        "manifest config path": (
            manifest.get("config", {}).get("path"),
            "configs/shadowrocket/cn-smart-routing.conf",
        ),
        "manifest config sha256": (
            manifest.get("config", {}).get("sha256"),
            expected_sha256,
        ),
        "manifest runtime upstream commit": (
            manifest.get("upstreams", {}).get("blackmatrix7/ios_rule_script"),
            BLACKMATRIX_COMMIT,
        ),
        "manifest Feishu reference commit": (
            manifest.get("upstreams", {}).get("icewithcola/Clash-Rule-Set"),
            FEISHU_REFERENCE_COMMIT,
        ),
    }
    for label, (actual, expected) in checks.items():
        if actual != expected:
            errors.append(f"{label} mismatch: expected {expected}, found {actual}")

    if f"# 版本：{version}" not in config_text:
        errors.append("config header version does not match VERSION")

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


def fetch_text(url: str) -> str:
    headers = {"User-Agent": "cn-smart-routing-validator/0.1"}
    request = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        return response.read().decode("utf-8")


def domain_rules(text: str) -> tuple[set[str], set[str]]:
    """Return domain suffixes and exact domains from supported upstream formats."""
    suffixes: set[str] = set()
    exact: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.strip().strip("'\"")
        if not line or line.startswith("#"):
            continue
        if re.fullmatch(r"\.[A-Za-z0-9._-]+", line):
            suffixes.add(line[1:].lower())
            continue
        match = re.match(r"DOMAIN-SUFFIX,([^,]+)", line)
        if match:
            suffixes.add(match.group(1).lower().lstrip("*."))
            continue
        match = re.match(r"DOMAIN,([^,]+)", line)
        if match:
            exact.add(match.group(1).lower().lstrip("*."))
            continue
        match = re.match(r"-\s*['\"]?\+\.([A-Za-z0-9._-]+)", line)
        if match:
            suffixes.add(match.group(1).lower())
            continue
        match = re.match(r"-\s*['\"]?([A-Za-z0-9._-]+)", line)
        if match and "." in match.group(1):
            exact.add(match.group(1).lower())
    return suffixes, exact


def domains_are_covered(
    candidates: set[str], suffixes: set[str], exact: set[str]
) -> set[str]:
    missing: set[str] = set()
    for candidate in candidates:
        domain = candidate.lower().lstrip("*.")
        if domain in exact:
            continue
        if any(domain == suffix or domain.endswith(f".{suffix}") for suffix in suffixes):
            continue
        missing.add(domain)
    return missing


def audit_realtime_upstreams(config_text: str) -> tuple[list[str], list[str]]:
    """Compare the config with selected Feishu and Tencent upstream sources."""
    errors: list[str] = []
    notes: list[str] = []
    try:
        sources = {name: fetch_text(url) for name, url in UPSTREAM_URLS.items()}
    except Exception as exc:  # noqa: BLE001 - keep optional audit readable
        return [f"realtime upstream unavailable ({type(exc).__name__}: {exc})"], notes

    config_suffixes, config_exact = domain_rules(config_text)

    feishu_suffixes, feishu_exact = domain_rules(sources["feishu"])
    chinamax_suffixes: set[str] = set()
    chinamax_exact: set[str] = set()
    for name in ("chinamax", "chinamax_domains"):
        suffixes, exact = domain_rules(sources[name])
        chinamax_suffixes.update(suffixes)
        chinamax_exact.update(exact)
    missing_feishu = domains_are_covered(
        feishu_suffixes | feishu_exact,
        config_suffixes | chinamax_suffixes,
        config_exact | chinamax_exact,
    )
    if missing_feishu:
        errors.append(
            "Feishu upstream domains not covered: " + ", ".join(sorted(missing_feishu))
        )
    else:
        notes.append(
            f"Feishu source coverage: {len(feishu_suffixes | feishu_exact)}/"
            f"{len(feishu_suffixes | feishu_exact)} domains"
        )

    try:
        meeting = json.loads(sources["tencent_meeting"])
        meeting_domains = {
            item["universal_domain"].lower().lstrip("*.")
            for section_name in ("login_domains", "other_domains")
            for item in meeting.get(section_name, [])
            if item.get("universal_domain")
        }
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        errors.append(f"Tencent Meeting source format changed: {type(exc).__name__}")
        meeting_domains = set()

    missing_meeting = domains_are_covered(
        meeting_domains,
        config_suffixes | chinamax_suffixes,
        config_exact | chinamax_exact,
    )
    if missing_meeting:
        errors.append(
            "Tencent Meeting official wildcard domains not covered: "
            + ", ".join(sorted(missing_meeting))
        )
    elif meeting_domains:
        notes.append(
            f"Tencent Meeting official coverage ({meeting.get('date', 'unknown')} "
            f"{meeting.get('version', 'unknown')}): {len(meeting_domains)}/"
            f"{len(meeting_domains)} wildcard domains"
        )

    return errors, notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--network", action="store_true", help="check remote rule URLs")
    parser.add_argument(
        "--audit-realtime-upstreams",
        action="store_true",
        help="compare Feishu and Tencent Meeting coverage with selected upstreams",
    )
    args = parser.parse_args()

    if not CONFIG.is_file():
        print(f"FAIL: missing {CONFIG}")
        return 1

    text = CONFIG.read_text(encoding="utf-8")
    errors = validate_static(text)
    errors.extend(validate_manifest(text))
    if args.network:
        errors.extend(validate_network(remote_urls(text)))
    upstream_notes: list[str] = []
    if args.audit_realtime_upstreams:
        upstream_errors, upstream_notes = audit_realtime_upstreams(text)
        errors.extend(upstream_errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: Shadowrocket configuration is structurally valid")
    print("PASS: no bundled nodes or obvious credentials detected")
    print("PASS: manifest version, pinned upstreams and config checksum match")
    if args.network:
        print("PASS: all remote rule URLs are reachable")
    for note in upstream_notes:
        print(f"PASS: {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
