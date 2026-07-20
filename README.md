# Shadowrocket CN Smart Routing

**English** | [简体中文](README.zh-CN.md)

Status: public release candidate. Current version: `0.1.0-rc.1`.

[![Validate Shadowrocket config](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/actions/workflows/validate.yml/badge.svg)](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/actions/workflows/validate.yml)
[![Latest release](https://img.shields.io/github/v/release/lucaszsGH/shadowrocket-cn-smart-routing?include_prereleases&label=release)](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/releases)
[![GPL-2.0 license](https://img.shields.io/github/license/lucaszsGH/shadowrocket-cn-smart-routing)](LICENSE)

An open-source **Shadowrocket configuration for mainland China**: mainland apps, banking, office tools, video, games and local-network traffic stay direct, while ChatGPT, Claude, Gemini, GitHub and other overseas services use your own manually selected proxy node.

![CN Smart Routing keeps mainland apps direct and overseas services proxied](assets/intro/cn-smart-routing-hero-en.png)

## One-line value

Keep Shadowrocket on without sending everyday mainland-China traffic through your proxy.

CN Smart Routing sends mainland apps, sites, IP ranges and local-network traffic directly, while AI, developer tools and other overseas services follow the node you manually select on the Shadowrocket home screen.

## Why this exists

Many users in mainland China already have their own proxy subscription, but still have to switch the VPN on and off:

- banking or payment apps may warn when traffic takes an overseas route;
- WeChat, Feishu, DingTalk, video and games may become slower;
- AI services and GitHub stop working when the proxy is turned off;
- complex policy groups make it unclear which node is actually in use;
- downloaded configurations may contain unknown nodes, scripts, certificates or credentials.

This project reduces the daily workflow to three visible choices:

```text
Import the config -> select your own node -> use Configuration mode
```

![Three-step CN Smart Routing setup while node choice stays with the user](assets/intro/cn-smart-routing-workflow-en.png)

## How this project is different

This repository is intentionally narrower than a general rule library or an ad-blocking suite.

| Design choice | CN Smart Routing |
|---|---|
| Primary user | Mainland-China Shadowrocket users who already have their own subscription |
| Daily goal | Keep the VPN enabled while mainland traffic stays direct |
| Node control | One node, selected manually on the Shadowrocket home screen |
| Default scope | Mainland office, banking, payment, media, games and LAN; overseas AI and development |
| Security surface | No bundled nodes, subscription URL, MITM, scripts or default ad blocking |
| Validation | Repository checks cover structure, priority, remote sources and common credential patterns |

Comparable projects often optimize for a different job: a large upstream rule ecosystem, many routing modes, aggressive ad blocking, or a different country. See the [neutral project comparison](docs/project-comparison.md) before choosing.

## What it does

- Sends mainland domains, IP ranges, office tools, banking, payments, video, games and LAN traffic to `DIRECT`.
- Sends ChatGPT, Claude, Gemini, Perplexity, GitHub, Docker, npm, PyPI and common overseas services to `PROXY`.
- Sends unmatched traffic to `PROXY`, so unknown overseas sites continue to work.
- Uses the node currently selected on the Shadowrocket home screen.
- Includes no proxy node, subscription URL, automatic country selection, HTTPS decryption or MITM certificate.

## Who it is for

Use this project if you:

- live or work in mainland China;
- already have your own Shadowrocket nodes or subscription;
- want to keep the VPN enabled for long periods;
- need mainland office, payment, media and gaming traffic to stay direct;
- need overseas AI and developer services;
- prefer manual node and region selection over automatic switching.

## Quick Start

### 1. Prepare Shadowrocket

Import your own subscription or nodes, then select one usable node on the home screen.

### 2. Import the configuration

Download [`configs/shadowrocket/cn-smart-routing.conf`](configs/shadowrocket/cn-smart-routing.conf).

Import it from the Shadowrocket **Config** page using Files, iCloud Drive, AirDrop, or a GitHub Raw URL.

Canonical auto-updating Raw URL:

```text
https://raw.githubusercontent.com/lucaszsGH/shadowrocket-cn-smart-routing/main/configs/shadowrocket/cn-smart-routing.conf
```

### 3. Use Configuration mode

1. Select `cn-smart-routing.conf` on the Config page.
2. Choose **Use Config**.
3. Return to the home screen.
4. Set Global Routing to **Config**.
5. Keep selecting nodes manually from the home screen.

Recommended tunnel options for the simplest mainland-first experience:

```text
Force Route: off
Include All Networks: off
Include Local Networks: off
Include APNs: off
```

Menu names may vary by Shadowrocket and OS version. The detailed walkthrough is currently Chinese-first: [快速开始](docs/zh-cn/quick-start.md).

## Routing at a glance

| Traffic | Examples | Route |
|---|---|---|
| Mainland office and real-time communication | Feishu, Minutes, Tencent Meeting, WeChat, WeCom | `DIRECT` |
| Mainland banking and payments | major banks, UnionPay, Alipay | `DIRECT` |
| Mainland media and games | Bilibili, Douyin, Tencent, NetEase | `DIRECT` |
| Apple services in mainland China | Apple China, iCloud, Guizhou-Cloud related services | `DIRECT` |
| Local network | private IP ranges, `.local`, `.lan` | `DIRECT` |
| AI | ChatGPT, OpenAI API, Claude, Gemini, Perplexity | `PROXY` |
| Developer services | GitHub, Docker Hub, npm, PyPI | `PROXY` |
| Overseas services | Google, YouTube, X, Reddit | `PROXY` |
| Unmatched traffic | anything not matched earlier | `PROXY` |

## Device support

| Client | Status | Notes |
|---|---|---|
| Shadowrocket on iPhone/iPad | Supported | Uses the shared core configuration |
| Shadowrocket on macOS | Supported | Uses the shared core configuration |
| Apple TV | Not yet independently verified | Not part of the supported matrix yet |
| Clash/Mihomo, Surge, Quantumult X, sing-box | Not supported by this file | Require separate adapters and tests |

This repository currently ships **Shadowrocket format only**. Do not import the `.conf` file into Clash or another client.

## Capability boundary

### Supported

- Transparent rule-based routing for Shadowrocket Configuration mode.
- Mainland-first direct routing and overseas proxy routing.
- Mainland chat, WSS signaling, meetings and recording-sync domains routed directly first.
- Manual home-screen node selection.
- Static checks for structure, rule priority, remote sources and obvious credential patterns.

### Requires real-device confirmation

- Bank-app behaviour: some apps warn whenever any system VPN is active, even when their traffic is `DIRECT`.
- Node quality, region suitability and account access.
- Sleep/wake, Wi-Fi/5G switching, captive portals, meetings and long sessions on each device.
- Apple TV behaviour and iCloud synchronization.

See the Chinese-first [real-time communication routing and test guide](docs/zh-cn/realtime-communications.md) for Feishu meetings, Minutes, Tencent Meeting and WeChat calls.

### Not promised

- Proxy nodes, subscriptions, accounts or login services.
- Automatic node or country selection.
- Prevention of platform account restrictions or risk controls.
- Zero latency change on every network and device.
- Bypassing local law, service terms, regional policy or platform controls.

## Privacy and security

The public package should never contain:

- subscription URLs or node details;
- public IP addresses tied to a user;
- cookies, tokens or account credentials;
- browsing, meeting or chat content;
- full Shadowrocket logs.

Do not post these items in Issues or Pull Requests. See [SECURITY.md](SECURITY.md).

## Customization

Fork the repository before maintaining personal rules. You can add mainland `DIRECT` domains, overseas `PROXY` services or internal team domains without embedding your subscription.

See the Chinese-first [customization guide](docs/zh-cn/customization.md).

## Validation

Run the structural and privacy-oriented checks:

```bash
python3 scripts/validate_shadowrocket.py
```

Also check whether every remote rule URL is reachable:

```bash
python3 scripts/validate_shadowrocket.py --network
```

Audit the realtime-communication coverage against selected Feishu community data and Tencent Meeting's official machine-readable firewall list:

```bash
python3 scripts/validate_shadowrocket.py --audit-realtime-upstreams
```

The validator does not replace a real Shadowrocket import or real-device traffic test.

## Third-party rules

The configuration references public rule lists from [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) by URL. A small set of Feishu domain suffixes is selectively adapted from the Unlicense-licensed [`icewithcola/Clash-Rule-Set`](https://github.com/icewithcola/Clash-Rule-Set); incompatible or high-risk IP lists are not imported. See [THIRD_PARTY.md](THIRD_PARTY.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Rule changes should preserve the priority order and include validation evidence.

Use the issue forms for a [routing problem](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=routing-problem.yml) or a [rule request](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=rule-request.yml). Never paste subscription URLs, node details, credentials or full traffic logs.

## License

Configuration and repository code are licensed under GPL-2.0. See [LICENSE](LICENSE). DeepWheel names and brand marks are covered separately in [NOTICE.md](NOTICE.md).
