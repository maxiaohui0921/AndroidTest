#-*-coding:utf-8-*-
#__author__='maxiaohui'

import subprocess
import time,random,os
import datetime
from config import config

fail_date=datetime.date.today().strftime('%m%d')
fail_time=time.strftime('%H%M%S')
timeTag=fail_date+fail_time

def getLogcat(deviceID=config.deviceId,deviceName='',keyword=''):
    filename = config.log_path+"\\"+deviceName+"_"+keyword+"_"+fail_date+fail_time+".txt"
    # print(filename)
    logcat_file = open(filename, 'w')
    if keyword=='':
        logcmd = "adb -s %s logcat -v time" % (deviceID)
    else:
        logcmd = "adb -s %s logcat -v time |grep %s" % (deviceID,keyword)
    # print("执行的adb命令："+logcmd)
    pro = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE)
    return pro,filename

def stopPro(pro):
    pro.terminate()

#adb -s 192.168.29.248:5555 shell top -d 5 | grep -E 'beeboxes|opnext'
def captureCPU(gap):
    filename = config.log_path+"\\"+"cpu_"+fail_date+fail_time+".txt"
    cpulog_file = open(filename, 'w')
    cmd_cpu = "adb -s %s shell top -d %d | grep -E 'beeboxes|opnext'" % (config.deviceId,gap )
    pro = subprocess.Popen(cmd_cpu, stdout=cpulog_file, stderr=subprocess.PIPE)
    return pro,filename

#获取内存信息
#adb shell dumpsys meminfo | findstr "beeboxes opnext RAM"
def captureMemory():
    filename = config.log_path + "\\" + "memory_" + fail_date + fail_time + ".txt"
    cpulog_file = open(filename, 'w')
    cmd_meminfo = "adb -s %s shell dumpsys meminfo | grep -E 'beeboxes|opnext'" % config.deviceId
    # print(cmd_meminfo)
    times=1
    while times<15:
        subprocess.Popen(cmd_meminfo, stdout=cpulog_file, stderr=subprocess.PIPE)
        times+=1
        time.sleep(10)
    return filename

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

#定义一个函数的抓取log的装饰器，在跑测试之前抓取adblog，在测试结束之后停止adblog
def getAdbLog(test):
    def logResult(*args,**kwargs):  #args是一个列表
        pro,filename=getLogcat(config.deviceId,config.deviceSN,config.logKeyWord)
        test(*args,**kwargs)
        time.sleep(5)
        stopPro(pro)
    return logResult

@getAdbLog
def runMonkey(timeHour):
    #time是用s做单位
    sendTimes=int(timeHour*3600*13.96)
    seed=random.choice(range(100))
    timeTagMonkey = datetime.date.today().strftime('%m%d') + time.strftime('%H%M%S')
    os.chdir(config.log_path)
    os.mkdir(timeTagMonkey)
    monkeyLog=config.log_path+'\\'+timeTagMonkey
    cmd='adb -s %s shell monkey -v -v -v  --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 300 -s %d %d 1>%s\info%s.txt 2>%s\error%s.txt'%(config.deviceId,seed,sendTimes,monkeyLog,timeTag,monkeyLog,timeTag)
    print(cmd)
    subprocess.Popen(cmd, shell=True)
    time.sleep(timeHour*3600)


if __name__=="__main__":  #当前脚本运行实例
    #runMonkey(0.1)

    # pro,filename=captureCPU(5)
    # time.sleep(60)
    # stopPro(pro)

    # captureMemory()

    pro,file=getLogcat(keyword="resultType")
    time.sleep(20)
    stopPro(pro)
