#-*-coding:utf-8-*-
#__author__='maxiaohui'
from config import config
from test_device.deviceTest import frDevice

def scrolSearchPerson(name):
    device34=frDevice(config.deviceId)
    device34.enterPersonManager()
    isFind=device34.scrollSearch(name)
    if isFind:
        print("找到%s了"%name)
    else:
        print("没有找到%s"%name)

if __name__ == "__main__":  #当前脚本运行实例
    scrolSearchPerson("家里")