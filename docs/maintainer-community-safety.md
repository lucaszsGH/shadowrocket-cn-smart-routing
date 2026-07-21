# 维护者安全清单

本页只给仓库维护者使用，不是普通用户的安装步骤。

## 已核实状态

截至 2026-07-21：

- Secret scanning：已开启；
- Push protection：已开启；
- `main` Ruleset：尚未开启；
- Private vulnerability reporting：尚未确认开启。

这些是 GitHub 远端设置，合并代码不会自动改变。

## 建议补齐

### 1. 保护 `main`

进入 **Settings → Rules → Rulesets**，只针对 `main`：

- 要求通过 Pull Request 合并；
- 要求 CI 检查 `validate` 通过；
- 阻止 force push 和删除；
- 保留可审计的管理员绕过方式，避免单维护者仓库被锁死。

先用只改文档的测试 PR 验证，不要用删除分支或 force push 做破坏性测试。

### 2. 开启私密漏洞报告

进入 **Settings → Security → Code security and analysis**，开启 **Private vulnerability reporting**。然后回到 **Security** 页面，确认出现 **Report a vulnerability**。

## 日常审核

- 合并前阅读完整差异，不只看勾选框；
- 路由改动要有 CI 和真机结果；
- 不要求用户公开订阅、节点、二维码、完整日志或个人网络信息；
- 如果凭证误传，先立即轮换；只删除最新文件不足以清除 Git 历史。
