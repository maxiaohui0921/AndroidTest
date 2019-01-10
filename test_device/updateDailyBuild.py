#-*-coding:utf-8-*-
#__author__='maxiaohui'
from test_device import terminal
from config import config

t=terminal.frDevice(config.deviceId)
t.updateDailyBuild()

if __name__ == "__main__":  #当前脚本运行实例
    pass