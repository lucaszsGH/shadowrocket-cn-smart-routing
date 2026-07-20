## 这次修改解决什么问题？

<!--
请用普通用户能理解的方式说明场景、现象和预期结果。
Please describe the user scenario, observed problem and expected result.
-->

## 修改类型

- [ ] 分流规则 / Routing rule
- [ ] 文档 / Documentation
- [ ] 验证脚本或 CI / Validation or CI
- [ ] 其他 / Other

## 预期路由

- [ ] `DIRECT`：中国大陆或局域网服务直连
- [ ] `PROXY`：海外服务走 Shadowrocket 首页当前手动选择的节点
- [ ] 仅文档或工具变更，不改变路由

涉及的公开服务或域名：

<!-- 只填写公开服务名或公开域名，不要填写带参数的完整 URL、私有主机名或 IP。 -->

## 中国大陆使用影响

请勾选已经评估的场景；不相关可留空并在下方说明。

- [ ] 银行与支付
- [ ] 飞书、钉钉、微信、企业微信及在线会议
- [ ] 国内视频、音乐与直播
- [ ] 国内游戏
- [ ] 局域网、打印机、NAS 或远程控制
- [ ] Wi-Fi / 5G 切换、睡眠唤醒或长期开启

影响说明：

## 测试证据

- 设备与系统：
- 网络：Wi-Fi / 5G / 其他
- Shadowrocket 模式：配置 / Rule
- 观察到的路由与结果：

已运行：

- [ ] `python3 scripts/validate_shadowrocket.py`
- [ ] 如修改了远程规则引用，已运行 `python3 scripts/validate_shadowrocket.py --network`
- [ ] `FINAL,PROXY` 仍是最后一条有效规则

## 风险与回退

<!-- 说明最可能的误伤、如何发现，以及如何恢复到修改前。 -->

## 隐私与公开安全确认

- [ ] 本 PR 不包含订阅 URL、节点地址、节点名称、二维码或机场信息。
- [ ] 本 PR 不包含密码、Cookie、Token、API Key、登录链接或其他凭证。
- [ ] 本 PR 不包含个人公网 IP、私有主机名、设备标识、完整日志、浏览/会议/聊天内容。
- [ ] 如需举例，我只使用公开服务名、公开域名或已经脱敏的最小片段。

> 勾选框是提交者声明，不代表自动验证已经覆盖全部隐私风险。提交前请再次人工检查 diff。
