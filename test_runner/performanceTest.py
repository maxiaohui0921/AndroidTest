#-*-coding:utf-8-*-
#__author__='maxiaohui'

#当前只能自动抓取log，自动分析结果
#下一步：Smoke基本功能实现自动化之后，可以全面实现自动化

from adb import loggerHandler,deviceLogger
from config import config
import time

def runFr1N():
    print("请测试：在1：N模式下，连续刷脸")
    pro=deviceLogger.getLogcat(config.deviceId,"desktop29",config.faceRecognizationKey)
    time.sleep(65)
    pro[0].terminate()
    print("    测试log文件：%s"%pro[1])
    loggerHandler.analyzeLog(pro[1],config.oneByNPass)

def runFr11():
    print("请测试：在1：1模式下，连续刷脸")
    pro=deviceLogger.getLogcat(config.deviceId,"desktop29",config.faceRecognizationKey)
    time.sleep(65)
    pro[0].terminate()
    print("    测试log文件：%s"%pro[1])
    loggerHandler.analyzeLog(pro[1],config.oneByonePass)

def runImportLocal():
    print("请测试：本地导入人员")
    pro = deviceLogger.getLogcat(config.deviceId, "desktop29", config.importLocalKey)
    time.sleep(1800)  #这里默认是半小时
    pro[0].terminate()
    print("    测试log文件：%s" % pro[1])
    loggerHandler.analyzeLog(pro[1], config.importLocal)

def runExportLocal():
    print("请测试：本地导出人员")
    pro = deviceLogger.getLogcat(config.deviceId, "desktop29", config.exportLocalKey)
    time.sleep(1800)  # 这里默认是半小时,后期需要根据实际情况进行条件判断自动决定测试时间
    pro[0].terminate()
    print("    测试log文件：%s" % pro[1])
    loggerHandler.analyzeLog(pro[1], config.exportLocal)

def runSaasIssue():
    print("请测试：Saas下发人员")
    pro = deviceLogger.getLogcat(config.deviceId, "desktop29", config.issueBySaasKey)
    time.sleep(5*60*60)  # 这里默认是4小时,后期需要根据实际情况进行条件判断自动决定测试时间
    pro[0].terminate()
    print("    测试log文件：%s" % pro[1])
    loggerHandler.analyzeLog(pro[1], config.saasIssueSuccess)

if __name__ == "__main__":  #当前脚本运行实例
    runSaasIssue()
    #runFr11()