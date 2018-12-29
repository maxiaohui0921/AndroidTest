#-*-coding:utf-8-*-
#__author__='maxiaohui'
from utils import apitest
import re
import datetime,time,os
from config import config
from adb import deviceHandler

todayTag=datetime.datetime.fromtimestamp(time.time()).strftime('%m%d')

def downloadLatestDailyBuild():
    method = "get"
    url = "/agoldbase_rom_new/bb_dev_3g_dailybuild/"
    swHost = "http://192.168.100.136:8000"

    html = apitest.testAPI(method, url, host=swHost).text
    latestBuild=re.findall(r'<a.*?href=.*?>(.*?)<\/a>',html)[-1]

    if not latestBuild.find(todayTag)>=0:
        print("没有当天的最新build")
        otaFile=""
    else:
        url=url+latestBuild+"OTA/"
        html = apitest.testAPI(method, url, host=swHost).text
        downloadBuild = re.findall(r'<a.*?href=.*?>(.*?ota.zip)<\/a>', html)[0]
        url=url+downloadBuild
        #执行下载
        print("开始下载文件，请等待。。。")
        res=apitest.testAPI(method, url, host=swHost)
        res.raise_for_status()
        otaFile=config.log_path+"\\"+downloadBuild
        newfile = open(otaFile, 'wb')  # 本地文件
        for chunk in res.iter_content(10240):
            newfile.write(chunk)
        newfile.close()
        print("下载完成")
    return otaFile

def updateDailyBuild(deviceId):
    file=downloadLatestDailyBuild()
    # file="F:\\log\\BFRT_3G_DVT_2.1.x.d.t.d_12290417-ota.zip"
    if file:
        deviceHandler.checkConnected(deviceId)
        deviceHandler.pushOtaFile(file)

if __name__ == "__main__":  #当前脚本运行实例
    updateDailyBuild(config.deviceId)