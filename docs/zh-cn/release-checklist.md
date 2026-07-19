# 公开发布检查清单

## 发布前

- [ ] 确认GitHub账号/组织与`shadowrocket-cn-smart-routing`仓库名；
- [ ] 检查Git author姓名和邮箱是否适合公开；
- [ ] 运行静态验证；
- [ ] 运行17个远程规则URL验证；
- [ ] 运行敏感信息扫描；
- [ ] 确认没有订阅URL、节点、二维码或个人路径；
- [ ] 核对`VERSION`、配置注释、Changelog和中英文README版本一致；
- [ ] 运行`python3 scripts/render-intro-assets.py`，确认四张中英文介绍图均为1600×900；
- [ ] 以GitHub README宽度和原尺寸分别人工检查介绍图；
- [ ] 在Shadowrocket中通过最终Raw URL真实导入、编译和启用；
- [ ] 测试国内、AI、开发、局域网和回退；
- [ ] 确认README中的Raw URL已使用最终公开仓库地址。

## 发布后

- [ ] 创建首个版本标签；
- [ ] 在Release说明中列出兼容设备、验收范围和已知限制；
- [ ] 确认GitHub Actions通过；
- [ ] 用未配置过该仓库的新设备或干净环境复测导入步骤；
- [ ] 不承诺账号不受限制、节点可用性或第三方规则永久可用。
