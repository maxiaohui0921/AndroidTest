#-*-coding:utf-8-*-
#__author__='maxiaohui'
from config import config
from test_device.terminal import frDevice
from adb.deviceLogger import getAdbLog

@getAdbLog
def addAdmin(name):
    device34=frDevice(config.deviceId)
    device34.enterSetting()
    device34.addAdmin(name)

addAdmin("李丽丽")