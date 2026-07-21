# 快速开始

## 你只需要准备

- iPhone、iPad或Mac；
- 已安装Shadowrocket；
- 自己的代理订阅或节点；
- 一个已经验证可用的手动节点。

CN Direct不提供节点或订阅，也不会自动替你选择国家或节点。

## 唯一推荐安装方式

先在Shadowrocket中导入并更新自己的订阅，在首页手动选择一个可用节点。

然后复制下面的稳定地址：

```text
https://raw.githubusercontent.com/lucaszsGH/shadowrocket-cn-smart-routing/main/configs/shadowrocket/CN-Direct-DeepWheel.conf
```

在Shadowrocket的配置页通过远程URL添加，并使用`CN-Direct-DeepWheel.conf`。

## 开启一次

1. 打开“配置”列表，点击`CN-Direct-DeepWheel.conf`的**文件名称**；
2. 在弹出菜单中点击“使用配置”；
3. 返回首页，把“全局路由”设为“配置”；
4. 打开Shadowrocket；
5. 在“设置 → 订阅”开启“配置自动后台更新”和“更新通知”；
6. 将更新间隔设为3天，并确认系统“后台App刷新”已允许Shadowrocket。

需要手动检查时，同样点击配置文件名称，在弹出的菜单里选择“更新”；不是在右侧寻找信息符号。更新后可点击“预览”核对顶部版本。

以后日常使用只需要在首页手动更换节点。配置更新不等于订阅节点更新；节点订阅仍按你的服务商设置更新。

> 配置内也写入了同一稳定`update-url`，但远程URL仍是唯一推荐安装方式。iOS和macOS决定后台任务何时真正运行；开启后台更新不代表每次更新都会立即执行，强制退出Shadowrocket后后台更新也可能暂停。

## 推荐系统选项

```text
强制路由：关闭
包括所有网络：关闭
包括本地网络：关闭
包括 APNs：关闭
```

这些选项用于减少对局域网和系统服务的接管，不代表关闭Shadowrocket的Packet Tunnel。

## 最小验收

启用后依次检查：

1. 百度或常用国内网站；
2. 微信、飞书或钉钉；
3. 一次飞书或微信语音通话；
4. 一个银行App首页；
5. 一个国内视频；
6. ChatGPT或Claude；
7. GitHub；
8. 局域网设备或打印机。

若国内服务异常，先切回原配置或关闭Shadowrocket，再查看[排查指南](troubleshooting.md)。

本地文件、iCloud Drive和AirDrop只用于远程URL无法导入时的恢复，不是默认安装方式。候选配置内含稳定`update-url`，但恢复导入后的自动更新仍需Shadowrocket正确识别该地址并开启后台更新。

涉及飞书会议、妙记、腾讯会议、会记或微信语音时，使用[国内实时通信与会议分流测试矩阵](realtime-communications.md)。
