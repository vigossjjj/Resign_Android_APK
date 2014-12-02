#!/usr/bin/python 
#coding:utf-8
'''
Created on 2014年7月22日

@author: Yunpeng Jiang
'''
import sys,os,datetime,shutil

#签名配置
KEYSTORE="~/.android/debug.keystore"
KEYALISE="androiddebugkey"
KEYPWD="android"
KEYALISEPWD="android"

CurrentDIR=sys.path[0]
CurrentTIME=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

APK = sys.argv[1]
DECOMPILE_PATH = APK[:-4]
APK_NAME=DECODE_FOLDER=(os.path.basename(APK)).split(".apk")[0]
APKTOOL = os.path.join(CurrentDIR,"apktool","apktool.jar")
# ZIPALIGN = os.path.join(CurrentDIR,"apktool","zipalign")

if __name__ == '__main__':
	print "反编译APK包..."
	#反编译
	DECOMPILE_CMD="java -jar "+APKTOOL+" d -r -s -f "+APK+" "+DECOMPILE_PATH
	os.popen(DECOMPILE_CMD)
	
	#在重新打包前可以做一写特殊的操作，比如替换当前APK的so

	print "重编译APK文件夹打包..."
	#编译APK打包
	COMPILE_CMD="java -jar "+APKTOOL+" b "+DECOMPILE_PATH
	os.popen(COMPILE_CMD)
	
	print "重签名APK包..."
	#重签名
	unsigned_apk = os.path.join(DECOMPILE_PATH,"dist",APK_NAME+".apk")
	signed_apk = os.path.join(DECOMPILE_PATH+"_signed_"+CurrentTIME+".apk")
	REGSINED_CMD = "jarsigner -verbose -storepass "+KEYALISEPWD+" -keypass "+KEYPWD+" -keystore "+KEYSTORE+" -signedjar "+signed_apk+" "+unsigned_apk+" "+KEYALISE
	os.popen(REGSINED_CMD)
	
	print "优化APK包..."
	# 优化APK
	aligned_apk = os.path.join(CurrentDIR,"resigned_apks","resigned_"+APK_NAME+".apk")
	ALIGN_CMD = "zipalign -v -f 4 "+signed_apk+" "+aligned_apk
	os.popen(ALIGN_CMD)
	#删除文件
	folder = DECOMPILE_PATH
	if os.path.exists(folder):
		shutil.rmtree(folder)
	if os.path.exists(signed_apk):
		os.remove(signed_apk)
	print "完成APK重签名=========="
	print aligned_apk