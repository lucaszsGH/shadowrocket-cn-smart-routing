# Contributing

欢迎提交兼容性修复、公共域名补充和文档改进。这个仓库面向中国大陆 Shadowrocket 用户，首要目标是：国内与局域网尽量直连，海外服务使用首页当前手动选择的节点，同时不给用户引入订阅、账号和隐私风险。

## 先选 Issue 还是 Pull Request

- 只有现象、尚不确定规则怎么改：提交[分流问题](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=routing-problem.yml)；
- 已知需要新增或调整公开域名：提交[规则建议](https://github.com/lucaszsGH/shadowrocket-cn-smart-routing/issues/new?template=rule-request.yml)，或直接发 Pull Request；
- 怀疑包含可利用漏洞、凭证或其他敏感内容：不要发公开 Issue，先阅读 [SECURITY.md](SECURITY.md)。

## 建议流程

1. Fork 本仓库并从最新 `main` 创建独立分支；
2. 一个 Pull Request 只解决一个问题，不混入无关格式化或个人配置；
3. 修改规则时说明真实用户场景、期望 `DIRECT` 或 `PROXY`，以及规则优先级；
4. 按 Pull Request 模板补充真机或可复现的验证证据；
5. 提交前查看完整 diff，确认没有私人信息；
6. 等待 CI 和维护者复核。

## 必须遵守的边界

1. 不提交订阅 URL、机场或节点信息、二维码、账号凭证、个人公网 IP、私有主机名、完整日志或聊天/会议内容；
2. 保持 `FINAL,PROXY` 为最后一条有效规则；
3. 不把个人订阅、固定节点名、自动选区、TUN、MITM、脚本或默认广告拦截加入公共配置；
4. 避免未经验证的大型规则集，新增第三方远程规则时说明来源、许可证、用途和回退方式；
5. 银行、支付、登录、国内会议、影音、游戏和局域网属于高影响场景，相关变更必须说明误伤风险和回退方式；
6. 不把本项目描述为账号风控规避、匿名、IP 纯净度或零延迟保证。

## 本地验证

每次修改都运行：

```bash
python3 scripts/validate_shadowrocket.py
python3 scripts/validate_repository.py
```

如果新增或调整了远程规则 URL，再运行：

```bash
python3 scripts/validate_shadowrocket.py --network
```

文档和静态脚本通过不等于真机可用。涉及路由的变更仍应在 Shadowrocket 配置模式下验证国内、海外和局域网的真实访问。

## 评审原则

- 优先接受能解释用户价值、范围小、可回退并有验证证据的变更；
- 维护者可以要求拆分过大的 Pull Request，或拒绝证据不足、隐私风险过高的规则；
- `.github/CODEOWNERS` 会请求维护者评审，但是否强制通过由 GitHub 远端仓库规则决定。
