#!/bin/sh
CurrDir=$(cd "$(dirname "$0")"; pwd)
cd ${CurrDir}
#签名配置
KEYSTORE=~/.android/debug.keystore
KEYALISE=androiddebugkey
KEYPWD=android
KEYALISEPWD=android

APK=`basename $1`
CURR_TIME=`date +"%Y%m%d%H%M%S"`
APK_NAME=`echo ${APK} | awk -F ".apk" '{print $1}'`
APKTOOL=./apktool/apktool.jar
DECOMPILE_PATH=./${APK_NAME}

echo "反编译APK包..."
java -jar $APKTOOL d -r -s -f $1 $APK_NAME

echo "编译APK打包"
java -jar $APKTOOL b $APK_NAME

echo "重签名APK包..."
unsigned_apk=./${APK_NAME}/dist/${APK_NAME}.apk
signed_apk=./${APK_NAME}_signed_${CURR_TIME}.apk
jarsigner -verbose -storepass ${KEYALISEPWD} -keypass ${KEYPWD} -keystore ${KEYSTORE} -signedjar ${signed_apk} ${unsigned_apk} ${KEYALISE}

echo "优化APK包..."
aligned_apk=./resigned_apks/resigned_${APK}
zipalign -v -f 4 ${signed_apk} ${aligned_apk}

echo "清理文件..."
if [ -e $DECOMPILE_PATH ]; then
	rm -r $DECOMPILE_PATH
fi

if [ -e $signed_apk ]; then
	rm -r $signed_apk
fi

echo "完成APK重签名==========\n"$aligned_apk
