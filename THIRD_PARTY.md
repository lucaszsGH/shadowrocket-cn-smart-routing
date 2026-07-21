# 第三方资源

本配置通过远程URL引用以下项目的公开规则文件：

## blackmatrix7/ios_rule_script

- 项目：https://github.com/blackmatrix7/ios_rule_script
- 许可证：GPL-2.0
- 锁定提交：`e69663d642551aa3e0164a656179335a896127ad`
- 使用方式：运行时通过`RULE-SET`或`DOMAIN-SET`引用上述固定提交的Raw URL
- 默认大陆覆盖：`ChinaMax.list`与`ChinaMax_Domain.list`
- 海外保护：AI、开发和办公服务的小型专项规则集，优先级位于ChinaMax之前
- 本仓库不复制、不打包、不重新发布其规则文件

使用者应同时阅读并遵守第三方项目的许可证、特别声明和适用法律。正式配置不跟随移动分支自动变化；后续仅在问题修复或计划发布时审查并更新固定提交。第三方仓库仍可能被移动、删除或停止维护，本仓库不对其持续可用性作保证。

## icewithcola/Clash-Rule-Set

- 项目：https://github.com/icewithcola/Clash-Rule-Set
- 参考文件：https://github.com/icewithcola/Clash-Rule-Set/blob/6baf0076c10bc87b9f9d30221254fdbd97f0f221/feishu.yaml
- 许可证：Unlicense
- 使用方式：参考该文件中来自飞书公开网络资料的域名条目，选择性补充当前 ByteDance 上游规则未覆盖的稳定域名
- 本仓库不在运行时引用 Clash YAML，也不复制其中的 IP 列表

选择性整理的目的是保留 Shadowrocket 原生格式和关键实时通信保护层，避免把格式不兼容、来源不明或易漂移的动态媒体 IP 直接导入用户配置。
