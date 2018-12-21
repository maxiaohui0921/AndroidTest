#-*-coding:utf-8-*-
#__author__='maxiaohui'
import unittest
import warnings
import random

from config import config
from test_data import personDataGener
from test_device.deviceTest import frDevice


class smokeTest(unittest.TestCase):

    #定义要跑测试的机器
    device34=frDevice(config.deviceId)

    def setUp(self):
        #设备的初始状态都是人脸识别UI界面
        pass

    def tearDown(self):
        #返回人脸识别UI界面
        self.device34.backToIdle()

    # @unittest.skip(u"无条件跳过当前测试")
    def test_001addAdmin(self):
        print("测试添加管理员")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.addAdmin(personDataGener.generName())

    # @unittest.skip(u"无条件跳过当前测试")
    def test_002addPerson(self):
        print("测试添加人员")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterPersonManager()
        config.p1Name=personDataGener.generName()
        config.p1Id=str(random.choice(range(1000000,9999999)))
        self.device34.addPerson(config.p1Id,config.p1Name)

    # @unittest.skip(u"无条件跳过当前测试")
    def test_003reviewSearch(self):
        print("测试滚动搜索人员")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterPersonManager()
        self.device34.scrollSearch(config.p1Name)

    # @unittest.skip(u"无条件跳过当前测试")
    def test_004searchPerson(self):
        print("测试搜索找到人员")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterPersonManager()
        self.device34.searchPersonByName(config.p1Name)
        self.device34.clickByText(config.p1Id)
        self.device34.scrollSearchMore([config.p1Name,config.p1Id])

    def test_005getDevicesInfo(self):
        print("测试检查设备基本信息")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        sw,config.sn,lic=self.device34.getDeviceInfo()
        print("本机版本:%s"%sw)
        print("本机序列号:%s"%config.sn)
        print("本机默认license：%s"%lic)

if __name__=="__main__":
    unittest.main()