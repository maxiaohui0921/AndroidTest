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

    # 获取元素是否被选中了
    def getCheckStatusByResource(self,resourceId):
        return self.deviceConnected(resourceId=resourceId).info['checked']

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

    #滑动屏幕，找到菜单并点击
    def scrollClickByResource(self,resouceId):
        toLow = False
        toFind = False
        line1 = self.getDumpFile()
        while not toLow:
            if self.resourceExists(resouceId):
                toFind = True
                # print("找到%s"%item)
                self.clickByResourceId(resouceId)
                break
            self.swapeToUp()
            line2 = self.getDumpFile()
            if line2 != line1:
                line1 = line2
            else:
                toLow = True
        if not toFind:
            print("没有找到%s" % resouceId)
        return toFind

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

if __name__ == "__main__":  #当前脚本运行实例
    pass