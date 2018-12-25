#-*-coding:utf-8-*-
#__author__='maxiaohui'
import unittest
import warnings
import random
from config import config
from test_data import personDataGener
from test_device.terminal import frDevice
from adb.deviceLogger import getAdbLog


class smokeTest(unittest.TestCase):

    #定义要跑测试的机器
    device34=frDevice(config.deviceId)

    def setUp(self):
        #设备的初始状态都是人脸识别UI界面
        pass

    def tearDown(self):
        #返回人脸识别UI界面
        self.device34.backToIdle()

    @unittest.skip(u"无条件跳过当前测试")
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

    # @unittest.skip(u"无条件跳过当前测试")
    def test_005getDevicesInfo(self):
        print("测试检查设备基本信息")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        sw,config.sn,lic=self.device34.getDeviceInfo()
        print("本机版本:%s"%sw)
        print("本机序列号:%s"%config.sn)
        print("本机默认license：%s"%lic)

    # @unittest.skip(u"无条件跳过当前测试")
    def test_006updateLicense(self):
        print("更新license")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.upLicense(300)

    # @unittest.skip(u"无条件跳过当前测试")
    def test_007getPersonCapacity(self):
        print("获取人员使用容量")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        pn,cn=self.device34.getPersonCapacity()
        print("当前终端常客人数:%s"%pn)
        print("当前终端容量人数:%s"%cn)

    # @unittest.skip(u"无条件跳过当前测试")
    def test_008editDefaultPRule(self):
        print("编辑默认人员规则")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.scrollClickByResource('com.opnext.setting:id/tv_person_rules')
        self.device34.editDefualPRule()

    # @unittest.skip(u"无条件跳过当前测试")
    def test_009importPeoples(self):
        print("批量导入人员")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterPersonManager()
        self.device34.importPerson(100,"有照片","小米")

    # @unittest.skip(u"无条件跳过当前测试")
    def test_010updateValidation(self):
        print("更改验证模式")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.editValidation("1:1模式")

    # @unittest.skip(u"无条件跳过当前测试")
    def test_011updateScenario(self):
        print("更改场景设置")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.editScenario("自定义情景")   #选中某个情景

    # @unittest.skip(u"无条件跳过当前测试")
    def test_012getDefaultSetting(self):
        print("获取自定义情景默认设置值")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.getDefaultSettings()

    def test_013setDefualtSetting(self):
        print("设置自定义情景默认设置值为0")
        warnings.simplefilter("ignore", ResourceWarning)
        self.device34.enterSetting()
        self.device34.setSelfDefineParas()

if __name__=="__main__":
    unittest.main()