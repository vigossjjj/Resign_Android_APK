Resign_Android_APK
==================

a resign apk tool for android

使用此工具可对APK文件进行重签名。
注意：若待签名APK有签名保护，签名后APK无法正常打开但签名是成功的。

### 环境配置

需要配置`sdk/build-tools/${version}`到系统环境变量，确保aapt与zipalign的路径可以找到

### 使用说明

签名工具为python与shell两个版本

1. 将待签名APK文件拷贝到项目根目录
2. 编辑 **resign_apk.sh** 或 **resign_apk.py**中的签名配置,默认使用 `~/.android/debug.keystore`
3. Run `./resign_apk.sh ${your_apk}` or `./resign_apk.py ${your_apk}`
4. 重签名后的APK默认生成路径`./resigned_apks/resigned_${your_apk}`
