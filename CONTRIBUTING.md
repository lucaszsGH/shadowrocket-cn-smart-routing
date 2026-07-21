# Contributing

欢迎提交兼容性修复、域名补充和文档改进。

提交前请：

1. 不包含订阅、节点、凭证或完整敏感日志；
2. 保持`FINAL,PROXY`为最后一条有效规则；
3. 说明新增规则解决的具体场景；
4. 运行`python3 scripts/validate_shadowrocket.py`；
5. 对新增远程规则运行`python3 scripts/validate_shadowrocket.py --network`；
6. 避免加入未经验证的大型规则集、脚本或HTTPS解密。

正式修改请以`configs/shadowrocket/CN-Direct-DeepWheel.conf`为真源，并同步旧兼容路径`configs/shadowrocket/cn-smart-routing.conf`。校验器会阻止两者不一致，避免已通过旧Raw URL导入的用户中断更新。

涉及银行、支付、登录、会议或游戏的变更，应说明误伤风险和回退方式。
