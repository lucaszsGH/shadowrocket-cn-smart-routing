# 国内实时通信与会议分流

## 目标

在 Shadowrocket 长期开启时，让飞书、飞书会议、妙记、腾讯会议、会记、微信和企业微信的国内聊天、语音、视频、录制及同步链路尽量保持 `DIRECT`，避免无意经过首页代理节点。

配置只能减少 VPN 分流带来的干扰，不能消除运营商拥塞、Wi-Fi 干扰、服务器调度、设备性能或应用自身故障。

## 为什么不能只写“WebSocket 直连”

实时通信通常包含多个层次：

| 层次 | 常见用途 | 当前策略 |
|---|---|---|
| HTTPS / WSS | 登录、消息、会议控制和长连接信令 | 关键业务域名显式 `DIRECT` |
| UDP / QUIC | 实时语音、视频和弱网传输 | 已识别的国内服务与中国 IP `DIRECT` |
| TCP 回退 | UDP 不可用时的媒体或信令回退 | 跟随同一域名/IP规则 |
| CDN / 对象存储 | 妙记、会记、录制、图片和文件同步 | 飞书、字节、腾讯及中国域名规则 `DIRECT` |
| 未识别海外流量 | 海外网站和服务 | `FINAL,PROXY` |

WebSocket、HTTPS 和部分 QUIC 都可能使用 443 端口。按协议或端口把所有流量直连，会同时放过海外服务，因此本项目按业务域名、上游规则和中国 IP 分层匹配。

## 当前保障范围

### 飞书与妙记

- `*.feishu.cn` 覆盖聊天、会议及 `*-frontier.feishu.cn` WSS 信令；
- `feishucdn.com`、字节 CDN 与对象存储相关域名覆盖静态资源和同步；
- `bytevcloud.com`、`bdurl.net`、`snssdk.com`、`pstatp.com`、`toutiaocloud.com` 等辅助域名显式直连；
- 对照采用 Unlicense 的 `icewithcola/Clash-Rule-Set` 飞书域名表，补充 `feishuimg.com`、`feishupkg.com`、`baseopendev.com`、`bytehwm.com`、`ttwebview.com`、`volcvideo.com` 等当前 ByteDance 上游未覆盖的稳定后缀；
- 中国大陆媒体服务器 IP 由 `GEOIP,CN,DIRECT` 兜底。

### 腾讯会议、会记、微信和企业微信

- `meeting.tencent.com`、`wemeet.tencent.com`、`meeting.qq.com`、`wemeet.qq.com` 和 `tencentmeeting.cn` 显式直连；
- `qq.com`、`weixin.qq.com`、`wechat.com`、`wxwork.qq.com` 等聊天和登录域名直连；
- Tencent 与 WeChat 上游规则补充 RTC、CDN、媒体和动态业务域名；
- 中国大陆媒体服务器 IP 由 `GEOIP,CN,DIRECT` 兜底。

## UDP 策略为什么保持不变

配置继续使用：

```conf
udp-policy-not-supported-behaviour = REJECT
block-quic = all-proxy
```

国内实时通信先命中 `DIRECT`，不需要代理节点承载其 UDP。未知流量如果落入 `FINAL,PROXY`，则仍遵守代理边界。

不建议把 UDP 不支持时的行为全局改成 `DIRECT`：这会让未识别的海外 UDP 绕过代理，也无法从根本上解决错误分流。

## 为什么不写死全部媒体 IP

会议厂商会按地区、容量和容灾动态调度媒体服务器。腾讯会议也明确提示个人用户媒体 IP 可能频繁变化。把某一时刻的完整 IP 表写进通用配置，会产生三个问题：

1. 列表很快过期；
2. 云厂商共享网段可能误伤其他服务；
3. 过大的 IP 规则增加维护和排障成本。

本项目优先维护稳定的业务域名，再用上游腾讯/字节规则和 `GEOIP,CN` 兜底。只有真机日志证明存在持续、可复现且边界明确的媒体 IP 缺口时，才考虑增加最小 IP 段。

## GitHub 现有方案如何取舍

调研日期：2026-07-20。结论不是“规则越多越好”，而是按许可证、客户端格式、维护状态、误伤面和可验证性分层复用。

| 来源 | 处理方式 | 原因 |
|---|---|---|
| [`blackmatrix7/ios_rule_script`](https://github.com/blackmatrix7/ios_rule_script) | 继续通过 URL 引用选定的 Shadowrocket 规则 | 格式兼容、覆盖面广、项目持续维护；避免在本仓库复制大规则库 |
| [`icewithcola/Clash-Rule-Set/feishu.yaml`](https://github.com/icewithcola/Clash-Rule-Set/blob/6baf0076c10bc87b9f9d30221254fdbd97f0f221/feishu.yaml) | 只整理当前上游未覆盖的稳定域名 | 采用 Unlicense，但文件是 Clash YAML，不能直接当 Shadowrocket `RULE-SET`；域名可审计，IP 不需要 |
| [`buhuizhuce/Rule/Feishu.list`](https://github.com/buhuizhuce/Rule/blob/deccbf6835a735781c5f1ecff9451d9e2f7dd5fc/Feishu.list) | 不直接引用 | 未检测到明确许可证，且包含约 195 条跨地区/云服务 IP；全部 `DIRECT` 会扩大误伤与过期风险 |
| [`www011215/Surge_rule_list/Surge_TencentMeeting.list`](https://github.com/www011215/Surge_rule_list/blob/d442f0887293d6968cae348af5ba702a3594edc2/Surge_TencentMeeting.list) | 仅作交叉核对，不直接引用 | 未检测到明确许可证，包含约 114 条动态媒体 IP 和本机观察项；腾讯官方明确提示域名/IP会持续变化，不应靠解析结果固定 IP |
| [`Shadowrocket/config`](https://github.com/Shadowrocket/config) | 借鉴语法和局域网排除思路，不盲加参数 | 官方账户示例有参考价值，但仓库较旧；`bypass-system`、`bypass-tun` 等仍需在当前版本真机 A/B 后再决定 |

腾讯会议提供持续更新的[官方 JSON 防火墙清单](https://cdn.meeting.tencent.com/upload/firewall/domain_ip.json)。本项目不把该 JSON 直接交给 Shadowrocket，因为格式不兼容；而是通过可选审计命令，将官方泛域名与当前配置及 Tencent/WeChat 上游规则做覆盖对比。

```bash
python3 scripts/validate_shadowrocket.py --audit-realtime-upstreams
```

这使“自动引用”和“安全边界”同时成立：成熟、兼容的规则运行时引用；小而稳定的缺口显式维护；动态官方清单用于检查漂移；低可信或无许可证的大 IP 表不进入默认配置。

## 真机测试矩阵

每次涉及实时通信规则时，至少完成以下测试：

| 应用 | 必测动作 | Wi-Fi | 5G | Mac |
|---|---|---:|---:|---:|
| 飞书 | 收发消息、加入会议、麦克风、摄像头、共享屏幕 | 建议 | 建议 | 建议 |
| 妙记 | 生成、同步、打开和播放记录 | 建议 | 建议 | 建议 |
| 腾讯会议 | 登录、入会、语音、视频、共享、录制或会记 | 建议 | 建议 | 建议 |
| 微信 | 语音消息、语音通话、视频通话、文件发送 | 建议 | 建议 | 建议 |
| 企业微信 | 消息、语音或会议入口 | 建议 | 建议 | 建议 |

至少额外测试一次 Wi-Fi 与 5G 切换，以及设备睡眠唤醒后的重连。测试期间保持 Shadowrocket 为“配置”模式，首页节点保持不变，避免同时改变多个变量。

## 可公开的最小记录

```text
时间：仅到分钟
设备：iPhone / Mac，不写设备序列号
网络：Wi-Fi / 5G，不写公网 IP 或 Wi-Fi 名称
应用与动作：例如“飞书会议加入 + 语音 10 分钟”
结果：正常 / 卡顿 / 断线 / 无法同步
路由：DIRECT / PROXY / 未确认
对照：关闭 Shadowrocket 后是否仍复现
```

不要公开订阅 URL、节点名称、节点地址、个人公网 IP、完整 Shadowrocket 日志、会议名称、参会人、聊天内容或录音内容。

## 官方网络资料

- [飞书：如何在企业内网下保障飞书会议室正常使用](https://www.feishu.cn/hc/zh-CN/articles/921458789503-%E5%A6%82%E4%BD%95%E5%9C%A8%E4%BC%81%E4%B8%9A%E5%86%85%E7%BD%91%E4%B8%8B%E4%BF%9D%E9%9A%9C%E9%A3%9E%E4%B9%A6%E4%BC%9A%E8%AE%AE%E5%AE%A4%E6%AD%A3%E5%B8%B8%E4%BD%BF%E7%94%A8)
- [腾讯会议：企业防火墙配置域名和 IP 指引](https://meeting.tencent.com/support/topic/1929/)
- [腾讯云：TRTC 应对防火墙限制](https://cloud.tencent.com/document/faq/647/34399)
