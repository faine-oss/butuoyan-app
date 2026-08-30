# 不拖延 Android 官方发布

这里是“不拖延”学生效率工具箱的公开发布仓库，只存放 Android 正式安装包、版本说明和应用内更新清单，不包含开发源码或签名密钥。

## 当前版本

- 版本：V0.4.1（Build 6）
- Android 包名：`com.butuoyan.toolbox`
- 最低系统：Android 7.0（API 24）
- 手机直接下载：`https://faine-oss.github.io/butuoyan-app/downloads/butuoyan-v0.4.1-android.apk`
- GitHub 备用下载：在右侧 Releases 中下载 `butuoyan-v0.4.1-android.apk`
- APK SHA-256：`6D7B9C0C795667C6A2A3BF82FD64E12029E9FEC32992F916DF1B5CEB4FB40A6B`
- 签名证书 SHA-256：`CCE69E0DB63AE2D44825DAC92C1301D6DDB389A4EA9341D090A34FDBF6A79FB0`

## 安装说明

1. 优先打开 `https://faine-oss.github.io/butuoyan-app/` 直接下载 APK；主线路无需打开 GitHub Release 页面。
2. 在 Android 设置中允许浏览器或文件管理器“安装未知应用”。
3. 打开 APK 并按系统提示确认安装。

早期 V0.2 本地测试包使用 Android 调试证书，与 V0.3 之后的正式证书不同，不能直接覆盖安装。首次切换到正式版前请确认测试版中没有需要保留的数据，然后卸载测试版再安装正式版。V0.3、V0.3.1、V0.4.0 和 V0.4.1 使用同一签名，可以正常覆盖更新并保留本地数据。

V0.4.1 将手机主下载线路切换为 GitHub Pages 直接 APK，并保留 GitHub Release 备用线路。安装后建议打开“我的 → 数据安全与备份”，先导出一份完整备份。

## 应用内更新

应用会同时尝试以下公开清单检查 Android 新版本，任一线路成功即可继续：

`https://faine-oss.github.io/butuoyan-app/update.json`

`https://raw.githubusercontent.com/faine-oss/butuoyan-app/main/update.json`

主更新清单使用本仓库的 GitHub Pages，备用清单直接读取 GitHub Raw；APK 主线路也由 Pages 直接提供，GitHub Release 只作备用。

更新检查只读取公开版本信息，不上传任务、计划或五分钟启动记录。APK 下载完成后仍由 Android 核对应用签名并要求用户确认安装。

## 安全校验

在 Windows PowerShell 中可以运行：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\butuoyan-v0.4.1-android.apk"
```

计算结果应与本页以及 `update.json` 中公布的 SHA-256 完全一致。
