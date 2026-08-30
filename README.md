# 不拖延 Android 官方发布

这里是“不拖延”学生效率工具箱的公开发布仓库，只存放 Android 正式安装包、版本说明和应用内更新清单，不包含开发源码或签名密钥。

## 当前版本

- 版本：V0.4.0（Build 5）
- Android 包名：`com.butuoyan.toolbox`
- 最低系统：Android 7.0（API 24）
- APK：在右侧 Releases 中下载 `butuoyan-v0.4.0-android.apk`
- APK SHA-256：`508A3741567403F4634403DAF753310E1F65D8F695E69F3A2AA6FBC3C20F84A3`
- 签名证书 SHA-256：`CCE69E0DB63AE2D44825DAC92C1301D6DDB389A4EA9341D090A34FDBF6A79FB0`

## 安装说明

1. 从 GitHub Release 下载 APK。
2. 在 Android 设置中允许浏览器或文件管理器“安装未知应用”。
3. 打开 APK 并按系统提示确认安装。

早期 V0.2 本地测试包使用 Android 调试证书，与 V0.3 之后的正式证书不同，不能直接覆盖安装。首次切换到正式版前请确认测试版中没有需要保留的数据，然后卸载测试版再安装正式版。V0.3、V0.3.1 和 V0.4.0 使用同一签名，可以正常覆盖更新并保留本地数据。

V0.4.0 新增完整本地数据备份、文件预检与安全恢复、全局快速添加任务、首次使用引导和本地数据版本管理。安装后建议打开“我的 → 数据安全与备份”，先导出一份完整备份。

## 应用内更新

应用会同时尝试以下公开清单检查 Android 新版本，任一线路成功即可继续：

`https://faine-oss.github.io/butuoyan-app/update.json`

`https://raw.githubusercontent.com/faine-oss/butuoyan-app/main/update.json`

主线路使用本仓库的 GitHub Pages，备用线路直接读取 GitHub Raw；二者使用不同的公开入口。

更新检查只读取公开版本信息，不上传任务、计划或五分钟启动记录。APK 下载完成后仍由 Android 核对应用签名并要求用户确认安装。

## 安全校验

在 Windows PowerShell 中可以运行：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\butuoyan-v0.4.0-android.apk"
```

计算结果应与本页以及 `update.json` 中公布的 SHA-256 完全一致。
