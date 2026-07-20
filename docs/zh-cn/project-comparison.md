# 相似项目与定位对比

最后核对：2026-07-20。

这是一份中立的定位对比，不是质量排名。不同项目解决的问题不同；导入前仍应查看各仓库当前 README、许可证和最近变更。

| 项目 | 主要定位 | 它更擅长什么 | CN Smart Routing 的不同 |
|---|---|---|---|
| [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) | 提供多种 Shadowrocket 分流模式和去广告配置 | 模式多、规则变体多、广告过滤能力强 | 本项目只提供一套中国大陆优先配置，默认不启用广告拦截，节点仍由首页手动选择 |
| [GMOogway/shadowrocket-rules](https://github.com/GMOogway/shadowrocket-rules) | 大规模模块化 `DIRECT`、`PROXY`、`REJECT` 规则 | 适合高级用户自由组合、覆盖广、可叠加覆盖规则 | 本项目更像面向普通用户的成品配置，减少策略组和日常选择，并明确隐私与能力边界 |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | 跨客户端的上游规则、重写和脚本生态 | 服务覆盖极广，可供多种代理客户端引用 | 本项目不是它的替代品，而是选用其中的 Shadowrocket 规则，并补上中国大陆场景、配置结构和校验层 |
| [misha-tgshv/shadowrocket-configuration-file](https://github.com/misha-tgshv/shadowrocket-configuration-file) | 面向俄语用户和当地网络环境的区域化配置 | 地区化规则和配置变体 | 本项目把“按地区优化”的思路用于中国大陆办公、支付、影音、游戏、局域网以及海外 AI、开发场景 |

## 更适合选择本项目的情况

- 你已有自己的机场订阅或节点；
- 你要的是一套可直接理解的 Shadowrocket 配置，而不是自己拼装规则的工具箱；
- 飞书、钉钉、微信、企微、网银、支付、国内视频、游戏和局域网需要优先直连；
- ChatGPT、Claude、Gemini、GitHub 及其他未知海外流量统一跟随首页手动节点；
- 你不希望公开配置内置节点、自动选国家、脚本、MITM 或默认去广告。

## 更适合选择其他项目的情况

- 你的第一目标是强力去广告；
- 你需要黑名单、白名单、回国、流媒体等多套模式；
- 你喜欢自己组合和维护模块化规则；
- 你需要同时服务 Clash、Surge、Quantumult X、sing-box 等多个客户端；
- 你需要面向中国大陆以外地区的网络优化。

## 本项目主动接受的取舍

CN Smart Routing 用更少的选择换取更简单的日常体验：通过ChinaMax获得较完整的大陆覆盖，但只提供一个成品配置，不提供复杂策略组、脚本或默认广告拦截。它仍依赖上游公开规则，无法保证所有网银 App 在系统 VPN 开启时都不告警，也必须结合每个人的网络和节点做真机验证。
