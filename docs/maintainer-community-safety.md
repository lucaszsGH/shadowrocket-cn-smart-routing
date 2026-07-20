# 社区共创安全设置

这份清单供仓库维护者使用。它记录公开协作的最低安全设置，不是普通用户安装 Shadowrocket 配置的必经步骤。

## 当前边界

- 仓库文件只能准备 Pull Request 模板、CODEOWNERS、验证脚本和说明；
- GitHub Ruleset 与 Private vulnerability reporting 是远端仓库设置，必须由仓库管理员单独启用；
- 合并本文件不代表远端设置已经生效；
- 每次修改远端设置后，都要通过一次无害测试确认真实行为。

## 1. 保护 `main`

建议创建名为 `protect-main` 的 Branch ruleset：

1. 打开仓库 **Settings → Rules → Rulesets → New branch ruleset**；
2. Target branches 选择默认分支 `main`；
3. 先保持规则为草稿，核对后再设为 Active；
4. 开启 **Require a pull request before merging**；
5. 暂不要求批准数量，也不启用“必须由 Code Owner 批准”。当前只有一位维护者时，强制自我批准可能让正常合并受阻；
6. 开启 **Require status checks to pass**，选择 CI job `validate`；
7. 初期不强制分支必须保持最新，以避免第三方 PR 因无关提交反复更新；
8. 保持 **Block force pushes**，并阻止删除 `main`；
9. 为仓库管理员保留可审计的 bypass；如果界面提供 **For pull requests only**，优先使用该范围；
10. 保存前再次确认目标只有 `main`，不会影响贡献者自己的功能分支。

官方说明：

- [创建仓库 Ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [可用的 Ruleset 规则](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [Required status checks 排障](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/troubleshooting-required-status-checks)

### 验收

1. 从测试分支创建一个只改文档的 Pull Request；
2. 确认 `validate` 出现在检查列表并通过；
3. 确认不能绕过 PR 直接把普通分支合并进 `main`；
4. 确认管理员 bypass 可见且每次使用都需要主动选择；
5. 不执行真实 force push 或删除 `main` 来做破坏性测试。

## 2. 开启私密漏洞报告

1. 打开仓库 **Settings → Security → Code security and analysis**；
2. 找到 **Private vulnerability reporting** 并启用；
3. 回到仓库 **Security** 页面，确认出现 **Report a vulnerability**；
4. 不需要提交真实敏感数据来测试入口；只确认表单可见即可；
5. 启用并现场确认后，再更新 `SECURITY.md`，明确写成“已启用”。

官方说明：[私密报告仓库安全漏洞](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately?learn=security_advisories&learnProduct=code-security)

## 3. 日常维护

- 合并前阅读完整 diff，不只依赖提交者勾选隐私声明；
- 路由修改必须有 CI 结果；新增远程规则还要做网络可达性检查；
- 涉及银行、支付、会议、游戏或局域网时，要求提供最小化真机证据和回退方法；
- 不在公开评论中要求贡献者上传订阅、节点、二维码、完整日志或个人网络信息；
- 如果误提交敏感信息，先限制扩散并轮换相关凭证；仅删除最新版本通常不足以清除 Git 历史。
