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

#adb -s 192.168.29.248:5555 shell top -d 5 | grep -E 'beeboxes|opnext'
def captureCPU(gap,pkg):
    filename = config.log_path+"\\"+"cpu_"+fail_date+fail_time+".txt"
    cpulog_file = open(filename, 'w')
    cmd_cpu = "adb -s %s shell top -d %d | grep -E '%s'" % (config.deviceId,gap,pkg )

    pro = subprocess.Popen(cmd_cpu, stdout=cpulog_file, stderr=subprocess.PIPE)
    return pro,filename

#获取内存信息
#adb shell dumpsys meminfo | findstr "beeboxes opnext RAM"
def captureMemory(gap,keyworks):
    filename = config.log_path + "\\" + "memory_" + fail_date + fail_time + ".txt"
    cpulog_file = open(filename, 'w')
    cmd_meminfo = "adb -s %s shell dumpsys meminfo -d %d | grep -E '%s'" % (config.deviceId, gap, keyworks)
    print(cmd_meminfo)
    pro = subprocess.Popen(cmd_meminfo, stdout=cpulog_file, stderr=subprocess.PIPE)
    return pro, filename

#获取屏幕
def captureScreen(filename):
    cmd_capture = "adb -s %s shell screencap /sdcard/DCIM/%s.png" % (config.deviceId, filename+"_"+fail_date+"_"+fail_time)
    #print(cmd_capture)
    pic_name=filename+"_"+fail_date+"_"+fail_time
    print("生成了错误图片："+pic_name+"  文件路径："+config.log_path)
    subprocess.Popen(cmd_capture, shell=True)
    time.sleep(3)
    cmd_pull = "adb -s %s pull /sdcard/DCIM/%s.png %s" % (config.deviceId, pic_name,config.log_path)
    #print("运行pull命令："+cmd_pull)
    subprocess.Popen(cmd_pull, shell=True)
    time.sleep(1)
    cmd_rm = "adb -s %s shell rm /sdcard/DCIM/%s.png" % (config.deviceId, pic_name)
    #print("运行rm命令："+cmd_rm)
    subprocess.Popen(cmd_rm, shell=True)

if __name__=="__main__":  #当前脚本运行实例
    # pro=getLogcat(config.deviceId,"desktop29",config.faceRecognizationKey)
    # time.sleep(20)
    # pro[0].terminate()
    # print(pro[1])

    # pro=captureCPU(5,"beeboxes|opnext")
    # time.sleep(20)
    # pro[0].terminate()
    # print(pro[1])

    # captureScreen("fr")

    pro=captureMemory(5,"beeboxes|opnext|RAM")
    time.sleep(20)
    pro[0].terminate()
    print(pro[1])