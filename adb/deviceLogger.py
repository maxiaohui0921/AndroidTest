#-*-coding:utf-8-*-
#__author__='maxiaohui'

#!C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.4

import subprocess
import time
import datetime
from config import config

fail_date=datetime.date.today().strftime('%m%d')
fail_time=time.strftime('%H%M%S')

def getLogcat(deviceID,deviceName,keyword):
    filename = config.log_path+"\\"+deviceName+"_"+keyword+"_"+fail_date+fail_time+".txt"
    logcat_file = open(filename, 'w')
    logcmd = "adb -s %s adb -v time |grep %s" % (deviceID,keyword)
    # print("执行的adb命令："+logcmd)
    pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
    return pro,filename

def stopLogcat(pro):
    pro.terminate()

if __name__=="__main__":  #当前脚本运行实例
    pro=getLogcat(config.deviceId,"desktop29",config.faceRecognizationKey)
    time.sleep(20)
    pro[0].terminate()
    print(pro[1])



