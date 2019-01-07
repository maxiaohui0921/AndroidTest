#-*-coding:utf-8-*-
#__author__='maxiaohui'
import subprocess
import re,os,time
from adb import myLogging as log

#检查当前电脑连接的设备id，可检测到多台设备
def byteToStr(b):
    str(b, encoding="utf-8")
    bytes.decode(b)
    return b.decode()

#获取当前电脑连接的设备ID
def getDeviceList():
    cmd_devices = "adb devices"
    pro = subprocess.Popen(cmd_devices,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out,err=pro.communicate()
    out=byteToStr(out)
    deviceList=re.findall(r"(\d{3}.\d{3}.\d{2,3}.\d{2,3}:\d{4})",out)
    if out.find("offline")>=0:
        print("当前设备连接offline，请手动关闭开启usb debug")
        deviceList=[]
    elif len(deviceList)==0:
        print("当前电脑没有连接上任何终端设备，尝试自动连接")
    return deviceList

#自动检查设备是否断连，如果断连需要重新连接当前设备
def checkConnected(deviceId):
    check=False
    while not check:
        deviceList=getDeviceList()
        if deviceId in deviceList:
            check=True
        else:
            os.popen("adb connect %s"%deviceId)
            os.popen("adb root")
            os.popen("adb remount")
            os.popen("adb connect %s" % deviceId)

            # print(byteToStr(logs))

def pushOtaFile(file):
    cmd="adb push %s /sdcard/update.zip"%file
    print(cmd)
    os.popen(cmd)
    #判断文件是否push完成
    fileFinished=False
    filesize0=0
    while not fileFinished:
        time.sleep(10)
        fileSize1=int(os.popen("adb shell ls -s /sdcard/update.zip").read().split()[0])
        if fileSize1-filesize0>0:
            filesize0=fileSize1
            print("-",end="")
        else:
            fileFinished=True
            print("文件上传成功，可以开始升级了")

if __name__=="__main__":  #当前脚本运行实例
    #print(getDeviceList())
    # checkConnected("192.168.29.248:5555")
    b=os.popen("adb shell ls -s /sdcard/update.zip").read().split()[0]
    print(b)