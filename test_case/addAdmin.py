#-*-coding:utf-8-*-
#__author__='maxiaohui'
from config import config
from test_device.deviceTest import frDevice

device34=frDevice(config.deviceId)
device34.enterSetting()
device34.addAdmin("马晓晓12")

