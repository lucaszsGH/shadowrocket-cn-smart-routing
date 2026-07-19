# Shadowrocket CN Smart Routing｜中国大陆智能分流

[English](README.md) | **简体中文**

状态：公开发布候选；当前版本：`0.1.0-rc.1`。

一套面向中国大陆用户的开源 **Shadowrocket（小火箭）配置与分流规则**：国内 App、网银、办公、影音、游戏和局域网优先直连，ChatGPT、Claude、Gemini、GitHub 等海外服务使用你在首页手动选择的代理节点。

![CN Smart Routing 让中国大陆应用直连、海外服务代理](assets/intro/cn-smart-routing-hero-zh-CN.png)

## 一句话价值

让 Shadowrocket 保持开启，也让中国大陆流量尽量不绕路。

CN Smart Routing 会把国内 App、网站、IP 和局域网流量优先直连；AI、开发工具和其他海外服务，则统一跟随你在 Shadowrocket 首页手动选择的节点。

## 为什么需要它

很多中国大陆用户已经有自己的代理订阅，却仍然需要频繁开关 VPN：

- 打开 VPN 后，网银或支付 App 提示异常；
- 微信、飞书、钉钉、视频和游戏变慢；
- 关闭 VPN 后，ChatGPT、Claude、Gemini 和 GitHub 又无法使用；
- 策略组太多，不知道当前究竟用了哪个节点；
- 网上下载的配置可能夹带未知节点、脚本、证书或隐私风险。

这个项目把日常操作压缩成三个看得见的动作：

```text
导入配置 -> 选择自己的节点 -> 使用“配置”模式
```

![三步启用 CN Smart Routing，节点选择权仍由用户掌握](assets/intro/cn-smart-routing-workflow-zh-CN.png)

## 你能得到什么

- 国内域名、IP、办公、银行、支付、影音、游戏和局域网流量优先 `DIRECT`；
- ChatGPT、Claude、Gemini、Perplexity、GitHub、Docker、npm、PyPI 等服务自动 `PROXY`；
- 未命中的流量最终走 `PROXY`，未知海外网站不容易漏掉；
- 所有代理流量跟随 Shadowrocket 首页当前手动选择的节点；
- 配置不包含节点、订阅地址、自动选区、HTTPS 解密或 MITM 证书。

## 适合谁

- 居住或工作在中国大陆；
- 已经拥有自己的 Shadowrocket 节点或订阅；
- 希望 VPN 长期开启；
- 国内办公、支付、视频和游戏不能明显受影响；
- 需要使用海外 AI、代码托管和开发服务；
- 希望国家、地区和节点由自己决定，不交给自动选择。

## 3 分钟开始使用

### 1. 准备 Shadowrocket

先导入自己的订阅或节点，再在首页手动选择一个可用节点。

### 2. 导入配置

下载：[`configs/shadowrocket/cn-smart-routing.conf`](configs/shadowrocket/cn-smart-routing.conf)

在 Shadowrocket 的“配置”页面，通过“文件”、iCloud Drive、AirDrop 或 GitHub Raw URL 导入。

自动跟随`main`更新的标准 Raw URL：

```text
https://raw.githubusercontent.com/lucaszsGH/shadowrocket-cn-smart-routing/main/configs/shadowrocket/cn-smart-routing.conf
```

### 3. 使用“配置”模式

1. 在“配置”页面选中 `cn-smart-routing.conf`；
2. 点击“使用配置”；
3. 返回首页；
4. 将“全局路由”设为“配置”；
5. 以后仍在首页手动切换节点。

为降低局域网、网银和国内 App 受影响的概率，推荐：

```text
强制路由：关闭
包括所有网络：关闭
包括本地网络：关闭
包括 APNs：关闭
```

不同版本的菜单名称可能略有差异。完整步骤见[快速开始](docs/zh-cn/quick-start.md)。

## 分流一览

| 流量 | 代表服务 | 路由 |
|---|---|---|
| 国内办公 | 飞书、钉钉、微信、企业微信 | `DIRECT` |
| 银行支付 | 常见商业银行、银联、支付宝 | `DIRECT` |
| 国内影音和游戏 | B 站、抖音、腾讯、网易 | `DIRECT` |
| Apple 中国大陆服务 | Apple 中国、iCloud、云上贵州相关服务 | `DIRECT` |
| 局域网 | 私有地址、`.local`、`.lan` | `DIRECT` |
| AI | ChatGPT、OpenAI API、Claude、Gemini、Perplexity | `PROXY` |
| 开发服务 | GitHub、Docker Hub、npm、PyPI | `PROXY` |
| 海外服务 | Google、YouTube、X、Reddit | `PROXY` |
| 未命中流量 | 前面规则没有覆盖的流量 | `PROXY` |

## 设备支持

| 客户端 | 当前状态 | 说明 |
|---|---|---|
| iPhone/iPad Shadowrocket | 支持 | 使用同一核心配置 |
| macOS Shadowrocket | 支持 | 使用同一核心配置 |
| Apple TV | 尚未独立验证 | 暂不列入正式支持范围 |
| Clash/Mihomo、Surge、Quantumult X、sing-box | 本文件不支持 | 需要单独适配和测试 |

当前仓库只提供 **Shadowrocket 格式**，不能把这个 `.conf` 直接导入 Clash 或其他客户端。

## 能力边界

### 已支持

- Shadowrocket“配置”模式下的透明规则分流；
- 国内优先直连、海外优先代理；
- 首页手动选择节点；
- 对配置结构、规则优先级、远程来源和常见凭证形状做静态检查。

### 需要真机确认

- 网银 App：部分银行只要检测到系统 VPN 就会提示异常，即使该流量已经 `DIRECT`；
- 节点质量、地区适配和账号访问；
- 每台设备的睡眠唤醒、Wi-Fi/5G 切换、门户网络、在线会议和长时间运行；
- Apple TV 行为和 iCloud 同步。

### 不承诺

- 提供节点、订阅、账号或登录服务；
- 自动选择节点、国家或地区；
- 避免 ChatGPT、Claude 等平台的账号风控；
- 在所有网络和设备上做到完全零延迟变化；
- 绕过所在地法律、服务条款、地区政策或平台限制。

## 隐私与安全

公开仓库不需要，也不应该包含：

- 订阅 URL 和节点信息；
- 能关联个人的公网 IP；
- Cookie、Token 和账号凭证；
- 浏览、会议或聊天内容；
- 完整 Shadowrocket 日志。

公开 Issue 和 Pull Request 中也不要提交这些内容。详见 [SECURITY.md](SECURITY.md)。

## 自定义

建议先 Fork，再维护自己的规则。你可以增加国内 `DIRECT` 域名、海外 `PROXY` 服务或团队内部域名，但不要把自己的订阅写进配置。

详见[自定义指南](docs/zh-cn/customization.md)。

## 配置验证

运行结构与隐私检查：

```bash
python3 scripts/validate_shadowrocket.py
```

同时检查远程规则 URL：

```bash
python3 scripts/validate_shadowrocket.py --network
```

验证脚本不能替代真实导入和真机流量测试。

## 第三方规则

配置通过 URL 引用 [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) 的公开规则集，但不复制或重新发布这些规则文件。详见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 参与贡献

请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。修改规则时，应保留现有优先级并附上验证依据。

## 许可证

配置与仓库代码采用 GPL-2.0。详见 [LICENSE](LICENSE)。DeepWheel 名称与品牌标志单独遵循 [NOTICE.md](NOTICE.md)。
