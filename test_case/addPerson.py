#-*-coding:utf-8-*-
#__author__='maxiaohui'

from config import config
from test_device.terminal import frDevice
from test_data import personDataGener

def addPerson(id,name):
    device34=frDevice(config.deviceId)
    device34.enterPersonManager()
    device34.addPerson(id,name)

if __name__ == "__main__":  #当前脚本运行实例
    addPerson("111005",personDataGener.generName())