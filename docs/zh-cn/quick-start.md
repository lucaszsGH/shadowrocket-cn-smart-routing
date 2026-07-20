# 快速开始

## 你需要准备什么

- iPhone、iPad或Mac；
- 已安装Shadowrocket；
- 自己的代理节点或订阅；
- 一个可以正常使用的手动节点。

本项目不提供节点或订阅。

## 导入节点

先在Shadowrocket中导入并更新自己的订阅，然后在首页手动选择一个节点。不要在尚未选择可用节点时启用本配置。

## 导入配置

下载`configs/shadowrocket/cn-smart-routing.conf`。

可以使用：

- 文件或iCloud Drive；
- AirDrop；
- GitHub Raw URL；
- Shadowrocket配置页支持的其他导入方式。

## 启用

1. 打开“配置”；
2. 选择`cn-smart-routing.conf`；
3. 点击“使用配置”；
4. 返回首页；
5. 将“全局路由”切换到“配置”；
6. 开启Shadowrocket。

## 推荐设置

```text
强制路由：关闭
包括所有网络：关闭
包括本地网络：关闭
包括 APNs：关闭
```

这些设置的目的是避免强制接管局域网和系统服务，不代表关闭Packet Tunnel。

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

涉及飞书会议、妙记、腾讯会议、会记或微信语音时，使用[国内实时通信与会议分流测试矩阵](realtime-communications.md)。
