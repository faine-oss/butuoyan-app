# 不拖延 Android 官方发布

这里是“不拖延”学生效率工具箱的公开发布仓库，只存放 Android 正式安装包、版本说明和应用内更新清单，不包含开发源码或签名密钥。

## 当前版本

- 版本：V0.3.0（Build 3）
- Android 包名：`com.butuoyan.toolbox`
- 最低系统：Android 7.0（API 24）
- APK：在右侧 Releases 中下载 `butuoyan-v0.3.0-android.apk`
- APK SHA-256：`3546BC881DDC548518EA20796A83634AE8CF8D043E97E95A3A4C5FF68B407BB1`
- 签名证书 SHA-256：`CCE69E0DB63AE2D44825DAC92C1301D6DDB389A4EA9341D090A34FDBF6A79FB0`

## 安装说明

1. 从 GitHub Release 下载 APK。
2. 在 Android 设置中允许浏览器或文件管理器“安装未知应用”。
3. 打开 APK 并按系统提示确认安装。

早期 V0.2 本地测试包使用 Android 调试证书，与 V0.3 正式证书不同，不能直接覆盖安装。首次切换到正式版前请确认测试版中没有需要保留的数据，然后卸载测试版再安装正式版。V0.3 及后续正式版会保持同一签名，可正常覆盖更新。

## 应用内更新

应用读取以下公开清单检查 Android 新版本：

`https://raw.githubusercontent.com/faine-oss/butuoyan-app/main/update.json`

更新检查只读取公开版本信息，不上传任务、计划或五分钟启动记录。APK 下载完成后仍由 Android 核对应用签名并要求用户确认安装。

## 安全校验

在 Windows PowerShell 中可以运行：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\butuoyan-v0.3.0-android.apk"
```

计算结果应与本页以及 `update.json` 中公布的 SHA-256 完全一致。
