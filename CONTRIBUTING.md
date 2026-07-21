# Contributing

欢迎修正规则、补充公开域名或改进文档。

## 最简单的参与方式

- 只知道哪里不好用：提交[分流问题](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=routing-problem.yml)；
- 知道要补哪个公开域名：提交[规则建议](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=rule-request.yml)，也可以直接发 Pull Request；
- 涉及凭证或其他敏感信息：不要公开提交，先看 [SECURITY.md](SECURITY.md)。

## 提交 Pull Request

1. 一个 Pull Request 只解决一个问题；
2. 说明希望它走 `DIRECT` 还是 `PROXY`；
3. 提供最小、脱敏的验证结果；
4. 运行 `python3 scripts/validate_shadowrocket.py`。

如果修改了远程规则地址，再运行：

```bash
python3 scripts/validate_shadowrocket.py --network
```

## 必须遵守

- 不提交订阅、节点、二维码、账号凭证、个人公网 IP、私有主机名、完整日志或聊天/会议内容；
- 正式配置以 `configs/shadowrocket/CN-Direct-DeepWheel.conf` 为真源，并同步旧兼容路径 `configs/shadowrocket/cn-smart-routing.conf`；
- 保持 `FINAL,PROXY` 为最后一条有效规则；
- 不加入个人 TUN、MITM、脚本、固定节点、自动选区或默认广告拦截；
- 新增第三方远程规则时说明来源、许可证、用途和回退方式；
- 涉及银行、支付、登录、会议、游戏或局域网时，说明误伤风险和回退方式。
