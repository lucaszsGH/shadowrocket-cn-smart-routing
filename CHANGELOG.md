# Changelog

## Unreleased

- 增加精简的 Pull Request 模板与 CODEOWNERS，方便用户提交问题和改进；
- 补充贡献与维护者安全说明，明确隐私边界和远端仓库设置。

## 0.2.0 - 2026-07-21

- 产品展示名升级为`CN Direct by DeepWheel`，以“国内直连。海外照常代理。”作为单一消费者承诺；
- 新增规范配置路径`configs/shadowrocket/CN-Direct-DeepWheel.conf`，旧Raw路径继续保留且与新文件字节一致，避免已导入用户失效；
- 将GitHub Raw远程URL设为唯一推荐安装方式，本地文件、iCloud Drive和AirDrop降为恢复手段；
- 实测GitHub会过滤`shadowrocket://`自定义协议链接，因此移除不可依赖的一键按钮，避免用户点击无响应；
- 明确配置自动更新的前提：稳定更新地址、Shadowrocket配置后台更新、系统后台App刷新，并说明不保证固定时刻执行；
- 在配置中内嵌稳定`update-url`，让文件恢复导入也保留更新地址，同时继续把远程URL作为唯一推荐路径；
- 候选版经过macOS与iPhone实际导入、启用及手动更新验证后，正式发布为`0.2.0`；
- 用锁定ChinaMax快照的124,653条匹配规则、112,138条域名规则和12,436条IP网段说明覆盖体量，同时明确数字不等于App数或完整覆盖保证；
- 依据macOS Shadowrocket真机界面纠正操作路径：点击配置文件名称后选择“使用配置”“更新”或“预览”，不再误导用户寻找右侧信息符号；
- 按`lucas-deepwheel-brand-apply`增加所见即所得的安装与更新图示，并完成7组SVG/PNG尺寸及全尺寸人工检查；
- 完成macOS本地候选的真实导入、启用、国内外冒烟、局域网旁路及手动更新标记验证；公开Raw导入与手动“更新 → 预览版本”已真机通过，系统后台调度时机继续观察；

- 合并 Mac、iPhone 和公开仓库为唯一 `cn-smart-routing.conf`，设备差异交给 Shadowrocket 本身管理；
- 通用大陆覆盖从精选 China 规则升级为 ChinaMax，覆盖银行、支付、运营商、影音、游戏、域名和 IP；
- 去除 ChinaMax 已包含的钉钉、微信、字节、腾讯、网易和 TapTap 重复远程引用，保留关键实时通信显式规则和 Steam 国区补充；
- 增加 Copilot、Docker、npm、Python、JetBrains、Notion、Slack、Teams、Discord 和 OneDrive 的前置代理规则；
- 版本升级为 `0.2.0-rc.1`，并保留银行 App 可能检测系统 VPN 的明确限制；
- 将运行时第三方规则锁定到已验证提交，避免上游移动分支在未发布新版本时改变用户分流；
- 增加最小 `manifest.json`，记录版本、配置校验值、支持范围与固定上游版本；
- 对照 GitHub 现有飞书规则补齐 8 个上游未覆盖的稳定域名后缀，并记录许可证与固定提交来源；
- 增加可选实时通信上游审计：比较飞书域名覆盖与腾讯会议官方 JSON 防火墙清单，不直接引入无许可证或易漂移的大型媒体 IP 表；
- 增加国内实时通信保障层：显式覆盖飞书 WSS/会议信令、腾讯会议、妙记/会记及相关录制同步域名；
- 保持国内媒体流 `DIRECT`、未知海外流量 `PROXY` 的边界，不使用宽泛 UDP 直连或易漂移的个人用户媒体 IP 表；
- 增加飞书、腾讯会议和微信语音的真机测试矩阵、最小脱敏记录格式及静态回归校验；
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
