#-*-coding:utf-8-*-
#__author__='maxiaohui'
from uiautomator import Device
import time,os
from config import config
from adb import deviceHandler,myLogging

#本文件对uiautomator里的一些基本操作做了一些简易化的包装，使用起来更加容易记忆
class androidDevices(object):

    def __init__(self,deviceId):
        self.deviceId=deviceId
        deviceHandler.checkConnected(deviceId)  #保证连接正常,如果断了重新连接一下
        self.deviceConnected = Device(self.deviceId)
        myLogging.showLog("info","测试设备： %s"%deviceId)

    def clickByResourceId(self,resourceId):   #根据recourceId进行点击
        # print("点击resouce:"+resourceId)
        # time.sleep(1)
        self.deviceConnected(resourceId=resourceId).click()

    def clickByText(self,text):
        # time.sleep(1)#根据文本内容进行点击
        # print("点击文本："+text)
        self.deviceConnected(text=text).click()

    def clickByClass_Index(self,classN,indexN):
        time.sleep(1)
        if self.deviceConnected(index=indexN,className=classN).exists:   #先判断是否存在，如果存在进行点击
            self.deviceConnected(index=indexN,className=classN).click()

    def getTextByResourceId(self,reourceId):    #根据resourceId返回文本信息，用于文本内容判断
        info = self.deviceConnected(resourceId=reourceId).info
        return info['text']

    def resourceExists(self,resourceId):
        status=self.deviceConnected(resourceId=resourceId).exists
        # if status:
        #     print(resourceId+",在当前UI界面,存在")
        # else:
        #     print(resourceId + ",在当前UI界面,不存在")
        return status

    # 手指向上滑动
    def swapeToUp(self):
        time.sleep(1)
        self.deviceConnected.swipe(300, 1107, 300, 550, steps=10)

    # 手指向下滑动
    def swapeToDown(self):
        time.sleep(1)
        self.deviceConnected.swipe(300, 130, 300, 1111, steps=10)

    # 输入文字
    def inputByResourceId(self,resourceId,text):
        # time.sleep(1)
        self.deviceConnected(resourceId=resourceId).set_text(text)
        time.sleep(1)
        self.clickByXY(742, 669)  # 让键盘消失

    # 获取文本信息
    def getTextByResourceId(self,resourceId):
        return self.deviceConnected(resourceId=resourceId).info['text']

    # 点击坐标
    def clickByXY(self,x,y):
        # time.sleep(2)
        self.deviceConnected.click(x,y)

    # 获取dump获取元素.用于判断唯一
    def searchItem(self,item):
        self.deviceConnected.dump("abc.xml")
        file = os.path.join(os.getcwd(), "abc.xml")
        line=open(file,"rb").readlines()[0]
        location=deviceHandler.byteToStr(line).find(item)
        os.remove(file)
        return location

    #获取到当前屏幕的所有str
    def getDumpFile(self):
        self.deviceConnected.dump("abc.xml")
        file = os.path.join(os.getcwd(), "abc.xml")
        line = open(file, "rb").readlines()[0]
        line = deviceHandler.byteToStr(line)
        os.remove(file)
        return line

    #滑动到屏幕底部
    def scrollToend(self):
        time.sleep(1)
        toLow = False
        line1 = self.getDumpFile()
        while not toLow:
            self.swapeToUp()
            line2 = self.getDumpFile()
            if line2 != line1:
                line1=line2
            else:
                # print("滑动到屏幕底部了")
                toLow=True
        time.sleep(1)

    #滑动屏幕寻找special字符串
    def scrollSearch(self,item):
        toLow = False
        toFind=False
        line1 = self.getDumpFile()
        while not toLow:
            location=line1.find(item)
            if location>=0:
                toFind=True
                # print("找到%s"%item)
                break
            self.swapeToUp()
            line2=self.getDumpFile()
            if line2!=line1:
                line1=line2
            else:
                toLow=True
        if not toFind:
            print("没有找到%s"%item)
        return toFind

    #滚动查找多个字符串验证
    def scrollSearchMore(self,paraList):
        toLow = False
        toFind = False
        line1 = self.getDumpFile()
        while not toLow:
            for item in paraList:
                if line1.find(item):
                    # print("找到%s"%item)
                    paraList.remove(item)
            if not paraList:
                # print("都找到了")
                break
            self.swapeToUp()
            line2 = self.getDumpFile()
            if line2 != line1:
                line1 = line2
            else:
                toLow = True
        if paraList:
            print("没有找到%s" % str(paraList))

class frDevice(androidDevices):

    #从任何界面返回到取景器界面或者idle界面
    def backToIdle(self):
        while not self.resourceExists("com.opnext.face:id/sv_camera"):
            self.clickByClass_Index("android.widget.ImageView",0)
            self.clickByClass_Index("android.widget.Button",0)

    #从初始配置界面进入设置界面
    def enterSetting(self):
        # print("进入设置界面")
        #判断是否有设置button，如果没有需要点击调出设置button
        status = self.resourceExists("com.opnext.face:id/iv_pull_up")
        if status:
            self.clickByResourceId("com.opnext.face:id/iv_pull_up")
        #点击设置按键
        time.sleep(1)
        self.clickByResourceId("com.opnext.face:id/iv_setting")
        #输入管理员密码，这里设置密码为2580
        for i in range(4):
            self.clickByText(config.devicePsw[i])
        time.sleep(3)

    # 进入人员管理界面
    def enterPersonManager(self):
        # print("进入人员管理界面")
        status = self.resourceExists("com.opnext.face:id/iv_pull_up")
        if status:
            self.clickByResourceId("com.opnext.face:id/iv_pull_up")
        # 点击人员管理按键
        self.clickByResourceId("com.opnext.face:id/iv_person_list")
        # 输入管理员密码，这里设置密码为2580
        for i in range(4):
            self.clickByText(config.devicePsw[i])

    # 当前函数是从设置界面开始的,先向上滑动到页面底部,找到管理员,添加管理员
    def addAdmin(self,name):
        myLogging.showLog("info","添加管理员")
        # print("添加管理员")
        self.scrollToend()
        self.clickByText("管理员")
        #点击右上角的添加按键
        self.clickByResourceId("com.opnext.setting:id/actionbar_rightImg")
        #添加管理员姓名密码
        self.inputByResourceId("com.opnext.setting:id/et_name", name)
        self.inputByResourceId("com.opnext.setting:id/et_password", "2580")
        self.scrollToend()
        self.inputByResourceId("com.opnext.setting:id/et_verify_password", "2580")
        #拍摄管理员照片，设备默认对准一张图片才能自动化拍摄
        self.clickByResourceId("com.opnext.setting:id/imge_add")
        #点击保存
        self.clickByResourceId("com.opnext.setting:id/tv_save")

    #添加一个人员
    def addPerson(self,id,name,doorCardId=None,icCardId=None,personRule=None,paraDatabase=None):
        myLogging.showLog("info", "添加人员：%s"%name)
        # print("添加人员：%s"%name)
        # 点击左上添加人员按键
        self.clickByResourceId("com.opnext.datatool:id/add_person")
        self.inputByResourceId("com.opnext.datatool:id/et_person_id",id)
        self.inputByResourceId("com.opnext.datatool:id/et_person_name",name)
        if doorCardId:
            self.inputByResourceId("com.opnext.datatool:id/et_gate_id",doorCardId)
        if icCardId:
            self.inputByResourceId("com.opnext.datatool:id/et_ic_id",icCardId)
        self.swapeToUp()
        if personRule:
            self.clickByResourceId("com.opnext.datatool:id/tv_item")
            self.clickByText(personRule)
        if paraDatabase:
            self.clickByResourceId("com.opnext.datatool:id/tv_item")
            self.clickByText(personRule)
        time.sleep(2)
        self.swapeToDown()
        self.clickByResourceId("com.opnext.datatool:id/iv_default_photo")
        time.sleep(4)   #等待4s拍摄图片
        self.clickByResourceId("com.opnext.datatool:id/btn_save_person")

    # 人很少的时候就可以这样搜索
    def searchPersonByName(self,name):
        myLogging.showLog("info","通过人名搜索人员：%s"%name)
        # print("通过人名搜索人员：%s"%name)
        self.clickByResourceId("com.opnext.datatool:id/iv_search")
        self.inputByResourceId("com.opnext.datatool:id/et_search",name)
        self.clickByResourceId("com.opnext.datatool:id/iv_search")
        if self.resourceExists("com.opnext.datatool:id/iv_face"):
            # print("搜出了相关人员")
            myLogging.showLog("info","搜出了相关人员")
        else:
            # print("没有找到相关人员")
            myLogging.showLog("warning", "搜出了相关人员")

    #搜索版本号/序列号
    def getDeviceInfo(self):
        self.clickByResourceId("com.opnext.setting:id/tv_about_device")
        sw=self.getTextByResourceId("com.opnext.setting:id/tv_software_version")
        sn=self.getTextByResourceId("com.opnext.setting:id/tv_device_sn")
        licenseMaxNumber=self.getTextByResourceId("com.opnext.setting:id/tv_maxmember")
        return sw,sn,licenseMaxNumber

    #查看license

if __name__=="__main__":
    a=androidDevices("192.168.29.250:5555")
    a.clickByText("人脸识别设置")