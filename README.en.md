# CN Direct by DeepWheel | Always-on Shadowrocket routing for mainland China

[简体中文](README.md) | **English**

For mainland-China Shadowrocket users who already have a proxy subscription. Mainland and local-network traffic stays direct, while overseas AI, developer and other traffic follows the node you select on the Shadowrocket home screen.

![Keep Shadowrocket enabled while mainland apps stay direct and overseas services stay proxied](assets/intro/cn-smart-routing-hero-en.png)

## Keep Shadowrocket on. Keep mainland apps fast.

CN Direct does one job: send mainland and overseas traffic down the right paths. You keep control of your provider, country and node.

### Useful? Star it first

Click **Star** in the repository header to save the project and help more mainland-China users discover it.

> Star is a bookmark and discovery signal. It is not required for installation and does not send release notifications.

## 124,653 | 251 | 0

| Verifiable evidence | What it means for you |
|---|---|
| **124,653** mainland matching rules | Common domains and mainland IP ranges are less likely to detour through an overseas node |
| **251** upstream sub-rule sets | Coverage spans banking, payments, carriers, work, media, games and daily services |
| **0 nodes, 0 subscriptions, 0 MITM, 0 scripts** | The config routes traffic without taking over your provider or account |

The pinned snapshot also contains **112,138 domain/domain-suffix rules** and **12,436 mainland IP ranges**. These figures measure matching volume; they do not equal app counts or guarantee zero latency. [Inspect the pinned evidence](https://github.com/blackmatrix7/ios_rule_script/blob/e69663d642551aa3e0164a656179335a896127ad/rule/Shadowrocket/ChinaMax/README.md).

## Need Shadowrocket?

**[Download it from the US App Store (recommended)](https://apps.apple.com/us/app/shadowrocket/id932747118)**

Already use a Hong Kong Apple Account? [Open the Hong Kong App Store listing](https://apps.apple.com/hk/app/shadowrocket/id932747118).

The same official app supports iPhone, iPad and Mac. It is not currently listed in the Chinese mainland App Store. Use an Apple Account you personally control for the matching region; do not use shared accounts or unofficial installation packages.

## One setup path

### 1. Prepare your own node

Import and update your own provider subscription in Shadowrocket, then select a verified node on the home screen. This project does not provide, read or store subscriptions.

### 2. Copy the stable configuration URL

```text
https://raw.githubusercontent.com/lucaszsGH/shadowrocket-cn-smart-routing/main/configs/shadowrocket/CN-Direct-DeepWheel.conf
```

Add it as a remote URL on Shadowrocket's Config page. Canonical source: [`CN-Direct-DeepWheel.conf`](configs/shadowrocket/CN-Direct-DeepWheel.conf).

### 3. Use the configuration

1. In the Config list, tap the **`CN-Direct-DeepWheel.conf` filename**;
2. Choose **Use Config**;
3. Return home and set Global Routing to **Config**;
4. Enable Shadowrocket. Continue selecting nodes manually on the home screen.

![Import the remote URL, tap the configuration filename and choose Use Config](assets/intro/cn-smart-routing-workflow-en.png)

## A 30-second acceptance check

1. Open a frequently used mainland website or app;
2. Open GitHub or an overseas AI service;
3. Switch the home-screen node once and confirm overseas traffic follows it.

If all three work, keep using Config mode. If anything breaks, switch back to your previous configuration or turn Shadowrocket off, then follow the [troubleshooting guide](docs/zh-cn/troubleshooting.md).

## Same URL. Easier updates.

After remote-URL installation, stable releases continue using the same address.

```text
Settings -> Subscription -> Config
Automatic Background Update: on
Update Notifications: on
Update Interval: 3 days
```

Also allow Background App Refresh and notifications for Shadowrocket at the OS level. iOS, iPadOS and macOS decide when background tasks run, so updates are not guaranteed to arrive immediately.

To check now: **Config list -> tap filename -> Update -> Preview version**.

![Enable configuration updates and manually verify the current version](assets/intro/cn-direct-update-en.png)

- **URL** fetches the latest stable configuration;
- **Star** bookmarks the project but sends no notifications;
- **Watch -> Custom -> Releases** optionally sends GitHub release notes.

## Routing at a glance

| Traffic | Examples | Route |
|---|---|---|
| Mainland work and real-time communication | Feishu, Minutes, Tencent Meeting, WeChat, WeCom | `DIRECT` |
| Mainland banking and payments | major banks, UnionPay, Alipay | `DIRECT` |
| Mainland media and games | Bilibili, Douyin, Tencent, NetEase | `DIRECT` |
| Apple services in mainland China | Apple China, iCloud, Guizhou-Cloud related services | `DIRECT` |
| Local network | private IP ranges, `.local`, `.lan` | `DIRECT` |
| AI and developer services | ChatGPT, Claude, Gemini, GitHub, Docker, npm, PyPI | `PROXY` |
| Unmatched overseas traffic | anything not matched earlier | `PROXY` |

## Device and product boundaries

| Client | Status |
|---|---|
| Shadowrocket on iPhone/iPad | Supported; same configuration |
| Shadowrocket on macOS | Supported; same configuration; TUN is managed by the app |
| Apple TV | Not independently verified |
| Clash/Mihomo, Surge, Quantumult X, sing-box | This file cannot be imported directly |

Know before use:

- some banking apps warn whenever a system VPN is active, even when their traffic is `DIRECT`;
- node quality, region suitability and account access remain outside this configuration;
- this project cannot prevent ChatGPT, Claude or other platform account restrictions;
- local edits are overwritten by remote configuration updates.

## Share and contribute

Share the public project page, never your private subscription:

```text
https://github.com/lucaszsGH/shadowrocket-cn-smart-routing
```

- Report a [routing problem](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=routing-problem.yml);
- suggest a [public rule](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=rule-request.yml);
- read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a Pull Request.

Never post subscription URLs, nodes, QR codes, cookies, tokens, public IPs, account data or full logs.

<details>
<summary><strong>Version, validation and license</strong></summary>

Current stable version: `0.2.0`.

```bash
python3 scripts/validate_shadowrocket.py
python3 scripts/validate_shadowrocket.py --network
python3 scripts/validate_shadowrocket.py --audit-realtime-upstreams
```

The configuration references pinned rules from [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) and selectively adapts a small set of Feishu domains from the Unlicense-licensed [`icewithcola/Clash-Rule-Set`](https://github.com/icewithcola/Clash-Rule-Set). See [THIRD_PARTY.md](THIRD_PARTY.md).

Configuration and repository code are GPL-2.0 licensed. DeepWheel names and brand marks are covered separately in [NOTICE.md](NOTICE.md).

</details>
