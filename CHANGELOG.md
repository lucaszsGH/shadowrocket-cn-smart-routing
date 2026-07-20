# Changelog

## Unreleased

- 增加中文优先的 Pull Request 模板，要求说明用户场景、预期路由、真机证据、风险回退与隐私检查；
- 增加 CODEOWNERS、仓库级安全校验脚本及 CI 门禁，为公开共创提供可追踪的维护者复核；
- 补充贡献流程、条件式私密漏洞报告指引，以及 `main` Ruleset 与 Private vulnerability reporting 的管理员设置清单；
- 公开仓库更名为`shadowrocket-cn-smart-routing`，把正式软件名放入默认搜索字段；
- README 首屏补充“Shadowrocket configuration for mainland China / Shadowrocket 小火箭配置与分流规则”的自然语言定位；
- 更新 GitHub 描述、Topics 和 Raw 导入地址，提升 Shadowrocket、config、rules、China routing 等检索入口；
- 保留产品名`CN Smart Routing`以及既有配置文件名，避免为了搜索破坏用户使用习惯。
- 增加 DeepWheel 1280×640 GitHub Social Preview，并纳入本地与 CI 尺寸校验；
- 增加中英文相似项目定位对比，说明本项目与大规模规则库、去广告套件和上游规则生态的边界；
- 增加 CI / Release / License 徽章与隐私保护型 Issue 表单，降低首次判断和反馈成本。

## 0.1.0-rc.1 - 2026-07-19

- 首个公开发布候选版本；
- 项目命名统一为`CN Smart Routing` / `cn-smart-routing`；
- 采用`configs/<client>/`多客户端可扩展结构；
- 支持iPhone、iPad和macOS Shadowrocket；
- 国内办公、支付、银行、影音、游戏和局域网优先直连；
- AI、开发及未知海外流量走首页手动节点；
- 不包含订阅、节点、自动选择或凭证；
- 增加静态验证脚本、公开使用说明和第三方声明。
- 按 Lucas-DeepWheel 公开仓库格式增加中英文 README、可编辑 SVG 与 1600×900 PNG 介绍资产；
- 公开说明改为消费者优先：先说明使用价值、三步上手和能力边界，再展开技术细节。
