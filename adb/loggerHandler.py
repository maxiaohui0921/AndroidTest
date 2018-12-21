#-*-coding:utf-8-*-
#__author__='maxiaohui'
#自动分析人脸识别结果的log，计算性能数据
import os
import time
import datetime
import re
from adb import deviceLogger
from config import config

#使用正则表达式获取time字符串
def getTimeStrByRe(line):
    mat = re.search(r"(\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})",line)
    return time.strftime("%Y-")+mat.group(0)

#获取time字符串  多用于打印log显示需要
def getTimeStr(line):
    arr = line.split()
    time1 = "2018-" + arr[0] + " " + arr[1][:-4]
    return time1

#获取timesstamp  多用于计算时间差值
def getTimeTagFromLog(line):
    time1=getTimeStrByRe(line)
    timeArray=datetime.datetime.strptime(time1,"%Y-%m-%d %H:%M:%S")
    timeStamp=int(time.mktime(timeArray.timetuple()))
    return timeStamp

#获取两行记录的时间差值
def getTimeGap(line1,line2):
    gapSeconds=abs(getTimeTagFromLog(line1)-getTimeTagFromLog(line2))
    return gapSeconds

def analyzeLog(logfile,keyword):
    lines=open(logfile).readlines()
    successTimes=1  #测试成功的次数
    sTime=0   #测试成功的累积时间

    duplicateLines=[]
    for i in range(len(lines)):   #移除无用的log
        if lines[i].find(keyword)>=0:
            duplicateLines.append(lines[i])
    lines=duplicateLines

    for i in range(1,len(lines)) :
        if lines[i].find(keyword)>=0:  #算出成功记录的时间
            successTimes+=1
            gapTime=getTimeGap(lines[i],lines[i-1])
            sTime+=gapTime

    #打印出结果
    startTime=getTimeStrByRe(lines[0])
    endTime=getTimeStrByRe(lines[-1])
    print("    测试起始时间：%s--->%s"%(startTime,endTime))
    if successTimes>1:
        print("    成功次数：%s，平均时长秒:%.3f"%(successTimes,sTime/successTimes))

if __name__=="__main__":  #当前脚本运行实例
    pro=deviceLogger.getLogcat(config.deviceId,"desktop29",config.faceRecognizationKey)
    time.sleep(10)
    pro[0].terminate()
    print(pro[1])
    analyzeLog(pro[1],config.oneByNPass)