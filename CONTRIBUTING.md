# Contributing

欢迎提交兼容性修复、域名补充和文档改进。

提交前请：

1. 不包含订阅、节点、凭证或完整敏感日志；
2. 保持`FINAL,PROXY`为最后一条有效规则；
3. 说明新增规则解决的具体场景；
4. 运行`python3 scripts/validate_shadowrocket.py`；
5. 对新增远程规则运行`python3 scripts/validate_shadowrocket.py --network`；
6. 避免加入未经验证的大型规则集、脚本或HTTPS解密。

涉及银行、支付、登录、会议或游戏的变更，应说明误伤风险和回退方式。
