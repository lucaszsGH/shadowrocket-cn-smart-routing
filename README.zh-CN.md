# CN Direct by DeepWheel｜Shadowrocket 中国大陆直连配置

[English](README.md) | **简体中文**

状态：发布候选；当前版本：`0.2.0-rc.2`。

[![配置校验](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/actions/workflows/validate.yml/badge.svg)](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/actions/workflows/validate.yml)
[![最新版本](https://img.shields.io/github/v/release/lucaszsGH/shadowrocket-cn-smart-routing?include_prereleases&label=release)](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/releases)
[![GPL-2.0 许可证](https://img.shields.io/github/license/lucaszsGH/shadowrocket-cn-smart-routing)](LICENSE)

面向中国大陆用户的一套开源 **Shadowrocket（小火箭）配置**：国内办公、网银、支付、影音、游戏和局域网优先直连；ChatGPT、Claude、Gemini、GitHub 等海外服务跟随你在首页选择的节点。

![CN Direct 让中国大陆应用直连、海外服务代理](assets/intro/cn-smart-routing-hero-zh-CN.png)

## 国内直连。海外照常代理。

**安装一次。以后，只选节点。**

CN Direct 不提供节点，也不替你选择国家或地区。它只负责把国内与海外流量送上正确的路径，让 Shadowrocket 可以保持开启，节点选择权仍留在首页。

## 唯一安装方式

CN Direct 只推荐一种安装路径：**通过远程 URL 导入**。这样 Shadowrocket 才能在首次设置后继续检查稳定更新。

### 1. 准备自己的节点

先在 Shadowrocket 中导入自己的机场订阅，并在首页选择一个可用节点。本项目不提供、读取或保存订阅。

### 2. 复制稳定配置地址

```text
https://raw.githubusercontent.com/lucaszsGH/shadowrocket-cn-smart-routing/main/configs/shadowrocket/CN-Direct-DeepWheel.conf
```

打开 Shadowrocket 的“配置”页，通过远程 URL 添加该地址。GitHub 会过滤 `shadowrocket://` 自定义协议，因此本项目不提供看似一键、实际可能无效的安装按钮。

配置真源：[`configs/shadowrocket/CN-Direct-DeepWheel.conf`](configs/shadowrocket/CN-Direct-DeepWheel.conf)

### 3. 使用配置模式

1. 在“配置”列表中**点击 `CN-Direct-DeepWheel.conf` 的文件名称**；
2. 在弹出的操作菜单中点击“使用配置”；
3. 返回首页，将“全局路由”设为“配置”；
4. 开启 Shadowrocket；
5. 以后仍在首页手动切换自己的节点。

> 关键位置：点击配置文件名称，不是在右侧寻找信息符号。Shadowrocket不同设备版本的排版可能略有差异。

![CN Direct远程导入、点击配置名称并使用配置的三步图示](assets/intro/cn-smart-routing-workflow-zh-CN.png)

### 4. 首次开启自动更新

在 Shadowrocket 的“设置 → 订阅”中找到“配置”更新区域：

```text
自动后台更新：开启
更新提醒：开启
更新间隔：3 天
```

同时在 iPhone/iPad 系统设置中允许 Shadowrocket 使用“后台 App 刷新”和通知。不同版本的菜单名称可能略有差异。

需要立即检查更新时：在“配置”列表点击配置文件名称，再点击“更新”；随后点击“预览”，可在顶部核对版本。该路径已在macOS Shadowrocket真机验证。

![CN Direct开启自动更新、手动更新并预览版本的图示](assets/intro/cn-direct-update-zh-CN.png)

> 配置内同时写入同一稳定 `update-url`，用于恢复导入后的更新识别；远程 URL 仍是唯一推荐安装方式。iOS 结束 Shadowrocket 进程、关闭后台刷新或长时间不打开应用时，后台任务可能延后；本地修改也会在远程配置更新时被覆盖。

## 不是更多规则。是更少打扰。

CN Direct 使用固定到已验证提交的 ChinaMax 作为大陆覆盖基础，再把海外 AI、开发和办公服务放在它之前明确代理，避免大型大陆规则误判海外服务。

当前固定版本包含：

| 可核对的覆盖证据 | 数量 |
|---|---:|
| 总匹配规则 | **124,653 条** |
| 域名与域名后缀规则 | **112,138 条** |
| 中国大陆 IP 网段规则 | **12,436 条** |
| 上游明确列出的子规则集合 | **251 个** |

子规则集合涉及常见银行、支付、运营商、办公、影音、游戏和生活服务。数字来自本项目锁定的 ChinaMax `2026-07-20` 版本，代表匹配体量，不代表 124,653 个 App，也不保证所有网络和设备完全没有延迟变化。[查看固定版本证据](https://github.com/blackmatrix7/ios_rule_script/blob/e69663d642551aa3e0164a656179335a896127ad/rule/Shadowrocket/ChinaMax/README.md)

## 你仍然掌握节点

- 使用自己的机场订阅；
- 首页手动选择国家、地区和节点；
- 不自动选择节点；
- 不定义复杂策略组；
- 不内置节点、订阅 URL、脚本、MITM 或证书；
- 未命中的海外流量最终跟随首页节点代理。

## 分流一览

| 流量 | 代表服务 | 路由 |
|---|---|---|
| 国内办公与实时通信 | 飞书、妙记、腾讯会议、微信、企业微信 | `DIRECT` |
| 银行支付 | 常见商业银行、银联、支付宝 | `DIRECT` |
| 国内影音和游戏 | B 站、抖音、腾讯、网易 | `DIRECT` |
| Apple 中国大陆服务 | Apple 中国、iCloud、云上贵州相关服务 | `DIRECT` |
| 局域网 | 私有地址、`.local`、`.lan` | `DIRECT` |
| AI | ChatGPT、OpenAI API、Claude、Gemini、Perplexity | `PROXY` |
| 开发服务 | GitHub、Copilot、Docker Hub、npm、PyPI、JetBrains | `PROXY` |
| 海外办公 | Notion、Slack、Teams、Discord、OneDrive | `PROXY` |
| 未命中流量 | 前面规则没有覆盖的流量 | `PROXY` |

## 设备支持

| 客户端 | 当前状态 | 说明 |
|---|---|---|
| iPhone/iPad Shadowrocket | 支持 | 使用同一个 `CN-Direct-DeepWheel.conf` |
| macOS Shadowrocket | 支持 | 使用同一个配置；TUN 由应用设置管理 |
| Apple TV | 尚未独立验证 | 暂不列入正式支持范围 |
| Clash/Mihomo、Surge、Quantumult X、sing-box | 不支持 | 不能直接导入本文件 |

## 能力边界

### 已支持

- Shadowrocket“配置”模式下的透明规则分流；
- 国内优先直连、海外优先代理；
- 国内聊天、WSS 信令、会议和录制同步关键域名优先直连；
- 首页手动选择节点；
- 稳定 `update-url`、Shadowrocket 配置后台更新与固定上游版本；
- 对结构、规则优先级、远程来源、兼容旧地址和常见凭证形状进行校验。

### 仍需真机确认

- 部分银行只要检测到系统 VPN 就会提示异常，即使流量已经 `DIRECT`；
- 节点质量、地区适配和账号访问；
- 睡眠唤醒、Wi-Fi/5G 切换、门户网络、在线会议和长时间运行；
- 系统调度的后台更新时机；手动“更新 → 预览版本”链路已通过真机验证；
- Apple TV 行为。

### 不承诺

- 提供节点、订阅、账号或登录服务；
- 自动选择节点、国家或地区；
- 避免 ChatGPT、Claude 等平台的账号风控；
- 在所有网络和设备上做到完全零延迟变化；
- 绕过所在地法律、服务条款、地区政策或平台限制。

## 已经装好了？

如果 CN Direct 让你少开关一次小火箭，请在仓库右上角点亮 **Star**。它能帮你下次找到项目，也能帮助更多中国大陆用户发现这份配置。

- **自动更新配置**：使用上面的稳定 URL，并在 Shadowrocket 中开启配置自动更新；
- **接收版本说明**：仓库右上角选择 `Watch → Custom → Releases`；
- **提交问题或改进**：使用 Issue 或 Pull Request，但不要公开订阅 URL、节点、Cookie、Token、公网 IP 或完整日志。

Star 用来收藏。Watch 用来提醒。URL 用来更新。

## 排查与自定义

- [快速开始与首次验收](docs/zh-cn/quick-start.md)
- [常见问题排查](docs/zh-cn/troubleshooting.md)
- [国内实时通信与会议分流](docs/zh-cn/realtime-communications.md)
- [Fork 后自定义](docs/zh-cn/customization.md)
- [为什么采用这种设计](docs/zh-cn/design-principles.md)

本地文件、iCloud Drive 和 AirDrop 只作为远程 URL 无法使用时的恢复方式，不是默认安装路径。

## 配置验证

```bash
python3 scripts/validate_shadowrocket.py
python3 scripts/validate_shadowrocket.py --network
python3 scripts/validate_shadowrocket.py --audit-realtime-upstreams
```

验证脚本不能替代真实导入和真机流量测试。

## 第三方规则与许可证

配置引用 [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) 的固定版本规则，并从采用 Unlicense 的 [`icewithcola/Clash-Rule-Set`](https://github.com/icewithcola/Clash-Rule-Set) 选择性整理少量飞书域名。详见 [THIRD_PARTY.md](THIRD_PARTY.md)。

配置与仓库代码采用 GPL-2.0。DeepWheel 名称与品牌标志单独遵循 [NOTICE.md](NOTICE.md)。
