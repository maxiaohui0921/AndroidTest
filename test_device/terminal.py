#-*-coding:utf-8-*-
#__author__='maxiaohui'
from test_device.android import androidDevices
import time,os,re
from config import config
from adb import deviceHandler,myLogging

#当前测试机可以进行的基本功能操作
class frDevice(androidDevices):

    #从任何界面返回到取景器界面或者idle界面
    def backToIdle(self):
        while not self.resourceExists("com.opnext.face:id/sv_camera"):
            self.clickByClass_Index("android.widget.ImageView",0)
            self.clickByClass_Index("android.widget.Button",0)

    #滚轮调整时间的开始和结束时间
    def adjustTime(self,startT,endT):
        # h=self.deviceConnected(resourceId='com.opnext.setting:id/tv_start').sibling(className='android.widget.NumberPicker',index=1).child(resourceId='android:id/numberpicker_input').info['text']
        # m=self.deviceConnected(resourceId='com.opnext.setting:id/tv_start').sibling(className='android.widget.NumberPicker',index=2).child(resourceId='android:id/numberpicker_input').info['text']
        # h=self.deviceConnected(resourseId='com.opnext.setting:id/tv_end').sibling(className='android.widget.NumberPicker',index=1).child(resourceId='android:id/numberpicker_input').info['text']
        # m=self.deviceConnected(resourseId='com.opnext.setting:id/tv_end').sibling(className='android.widget.NumberPicker',index=2).child(resourceId='android:id/numberpicker_input').info['text']
        startH,startM=startT[:2],startT[3:]
        endH,endM=endT[:2],endT[3:]
        while self.deviceConnected(resourceId='com.opnext.setting:id/tv_start').sibling(className='android.widget.NumberPicker',index=1).child(resourceId='android:id/numberpicker_input').info['text']!=startH:
            time.sleep(1)
            self.deviceConnected.swipe(318, 680, 318, 620, steps=10)
        while self.deviceConnected(resourceId='com.opnext.setting:id/tv_start').sibling(className='android.widget.NumberPicker',index=2).child(resourceId='android:id/numberpicker_input').info['text']!=startM:
            time.sleep(1)
            self.deviceConnected.swipe(427, 680, 427, 620, steps=10)
        while self.deviceConnected(resourceId='com.opnext.setting:id/tv_end').sibling(className='android.widget.NumberPicker',index=1).child(resourceId='android:id/numberpicker_input').info['text']!=endH:
            time.sleep(1)
            self.deviceConnected.swipe(610, 680, 610, 620, steps=10)
        while self.deviceConnected(resourceId='com.opnext.setting:id/tv_end').sibling(className='android.widget.NumberPicker',index=2).child(resourceId='android:id/numberpicker_input').info['text']!=endM:
            time.sleep(1)
            self.deviceConnected.swipe(720, 680, 720, 620, steps=10)

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

    #本地导入license
    def upLicense(self,number):
        self.clickByResourceId("com.opnext.setting:id/tv_about_device")
        oldLicense = self.getTextByResourceId('com.opnext.setting:id/tv_maxmember')
        print("导入license之前，人数是：%s"%oldLicense)
        for times in range(3):
            self.clickByResourceId("com.opnext.setting:id/rl_maxmember")
        self.clickByResourceId('com.opnext.setting:id/btn_import_license')
        time.sleep(1)
        self.clickByText("授权证书")  #不许按照以下的规则取放置license文件，否则找不到
        time.sleep(2)
        self.clickByText(config.deviceSN)
        time.sleep(2)
        self.clickByText(str(number))
        time.sleep(2)
        self.clickByResourceId("com.opnext.setting:id/library_selected")
        self.clickByResourceId("com.opnext.setting:id/library_btn_import")
        self.clickByClass_Index("android.widget.ImageView", 0)
        self.clickByClass_Index("android.widget.ImageView", 0)
        newLicense=self.getTextByResourceId('com.opnext.setting:id/tv_maxmember')
        print("导入license之后，人数是：%s"%newLicense)

    #获取人员容量
    def getPersonCapacity(self):
        dataSource=self.getTextByResourceId("com.opnext.setting:id/tv_persons_capacity")
        num = re.findall('\d+', dataSource)
        personNumber=num[0]
        capacityNumer=num[1]
        return personNumber,capacityNumer

    #修改默认人员规则
    def editDefualPRule(self):
        self.clickByText("默认人员规则")
        self.inputByResourceId("com.opnext.setting:id/add_name","上班时间")
        if self.getCheckStatusByResource("com.opnext.setting:id/cb_face"):
            print("人脸方式通行")
        if self.getCheckStatusByResource("com.opnext.setting:id/radio_idcard"):
            print("人脸+身份证通行")
        if self.getCheckStatusByResource("com.opnext.setting:id/radio_passport"):
            print('人脸+护照通行')
        if self.getCheckStatusByResource("com.opnext.setting:id/radio_ic"):
            print("人脸+IC卡通行")
        if self.getCheckStatusByResource("com.opnext.setting:id/radio_entrance"):
            print("人脸+门禁卡通行")
        self.clickByText("默认时间段")
        self.inputByResourceId("com.opnext.setting:id/edit_time_name","上班时间")
        if not self.getCheckStatusByResource("com.opnext.setting:id/cb_all"):
            self.clickByResourceId("com.opnext.setting:id/cb_all")
        self.clickByResourceId("com.opnext.setting:id/cb_six")
        self.clickByResourceId("com.opnext.setting:id/cb_seven")
        self.adjustTime("09:00","18:00")
        if self.getTextByResourceId("com.opnext.setting:id/dropdown_text")!="允许通行":
            self.clickByResourceId("com.opnext.setting:id/dropdown_text")
            self.clickByText("允许通行")
        time.sleep(1)
        self.clickByResourceId('com.opnext.setting:id/save')
        self.clickByResourceId('com.opnext.setting:id/tv_save')

    #批量导入人员
    def importPerson(self,number,photo,pRule="默认人员规则"):  #U盘的结构必须按照规定格式进行排列才能跑当前case
        print("当前人员状态:%s"%self.getTextByResourceId('com.opnext.datatool:id/person_progress_text'))
        self.clickByResourceId('com.opnext.datatool:id/add_people')
        self.deviceConnected(text=pRule).left(resourceId='com.opnext.setting:id/img_select').click()
        self.clickByResourceId('com.opnext.setting:id/btn_keep_show')
        time.sleep(3)
        self.clickByText("导入人员")
        time.sleep(3)
        self.clickByText(str(number))
        time.sleep(3)
        self.clickByText("%s_全列_%s.xlsx"%(str(number),photo))
        time.sleep(3)
        self.clickByResourceId("com.opnext.datatool:id/btn_next")
        time.sleep(3)
        self.clickByText("导入人员")
        time.sleep(3)
        self.clickByText(str(number))
        time.sleep(3)
        self.deviceConnected(text='照片').left(resourceId='com.opnext.datatool:id/selected').click()
        time.sleep(3)
        self.clickByResourceId('com.opnext.datatool:id/btn_next')
        while self.resourceExists("com.opnext.datatool:id/ll_wait"):
            time.sleep(1)
        print("导入成功人数:%s"%self.getTextByResourceId("com.opnext.datatool:id/tv_sucessed"))
        print("导入失败人数:%s"%self.getTextByResourceId("com.opnext.datatool:id/tv_failed"))

    #修改人脸识别模式
    def editValidation(self, aim):   #1:N模式  1:1模式 混合模式
        self.clickByResourceId('com.opnext.setting:id/tv_face_recognize_setting')
        currentSetting=self.getTextByResourceId('com.opnext.setting:id/Validation_mode_text')
        print("之前验证模式:%s"%currentSetting)
        self.clickByText("验证模式")
        self.clickByText(aim)
        self.clickByResourceId('com.opnext.setting:id/actionbar_back')
        afterSetting=self.getTextByResourceId('com.opnext.setting:id/Validation_mode_text')
        print("修改后验证模式:%s"%afterSetting)

    #修改情景选择
    def editScenario(self,aim): #安全情景  快速情景 自定义情景
        self.clickByResourceId('com.opnext.setting:id/tv_face_recognize_setting')
        currentSetting = self.getTextByResourceId('com.opnext.setting:id/Scenario_selection_text')
        print("之前选择场景:%s" % currentSetting)
        self.clickByText("情景选择")
        self.clickByText(aim)
        self.clickByResourceId('com.opnext.setting:id/actionbar_back')
        afterSetting = self.getTextByResourceId('com.opnext.setting:id/Scenario_selection_text')
        print("修改场景为:%s" % afterSetting)

    #获取默认设置
    def getDefaultSettings(self):
        self.clickByResourceId('com.opnext.setting:id/tv_face_recognize_setting')
        self.clickByText("情景选择")
        self.clickByResourceId('com.opnext.setting:id/radio_auto')
        self.clickByResourceId('com.opnext.setting:id/tv_set')
        print(" 默认活体检测可见光阈值:%s" % self.getTextByResourceId('com.opnext.setting:id/value_live_light'))
        print(" 默认活体检测近红外阈值:%s" % self.getTextByResourceId('com.opnext.setting:id/value_live_Nir'))
        print(" 1:N模式可见光阈值：%s" % self.getTextByResourceId('com.opnext.setting:id/value_light_thresholdN'))
        self.scrollToend()
        print((" 1:1模式可见光阈值:%s" % self.getTextByResourceId('com.opnext.setting:id/value_light_threshold1')))

    #编辑自定义设置的参数
    def setSelfDefineParas(self):
        self.clickByResourceId('com.opnext.setting:id/tv_face_recognize_setting')
        self.clickByText("情景选择")
        self.clickByResourceId('com.opnext.setting:id/radio_auto')
        self.clickByResourceId('com.opnext.setting:id/tv_set')
        #设置一个参数
        def setValue(checkResource,aimValue,upButton,dwButton):
            while int(self.getTextByResourceId(checkResource)[:-1]) > aimValue:
                self.clickByResourceId(dwButton)
            while int(self.getTextByResourceId(checkResource)[:-1]) < aimValue:
                self.clickByResourceId(upButton)
        #设置活体检测可见光
        setValue('com.opnext.setting:id/value_live_light',0,'com.opnext.setting:id/add_live_light','com.opnext.setting:id/reduce_live_light',)
        #设置活体检测近红外
        setValue('com.opnext.setting:id/value_live_Nir',0,'com.opnext.setting:id/add_live_Nir','com.opnext.setting:id/reduce_live_Nir')
        #设置1:N的可见光
        setValue('com.opnext.setting:id/value_light_thresholdN',0,'com.opnext.setting:id/add_light_thresholdN','com.opnext.setting:id/reduce_light_thresholdN')

if __name__=="__main__":
    a=androidDevices("192.168.29.250:5555")
    a.clickByText("人脸识别设置")