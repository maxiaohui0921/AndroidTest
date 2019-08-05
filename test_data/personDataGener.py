#-*-coding:utf-8-*-
#__author__='maxiaohui'
import datetime
import random
import time
from datetime import date, timedelta

from utils.excel import easyExcel

#更新文件夹里的图片名称，并相应的修改名称和文件名称

#必须有一个模板
excelFile=r'D:\00.BeeBoxes_working\requirements\100.xlsx'

#随机生成姓名
def generName():
    a1=['张','金','李','王','赵',"牛","马","何","南","令狐","孙","猪","唐"]
    a2=['玉','明','龙','芳','军','玲','小',"士","司","冲","悟","亿","白","华","哥","下","美","贵"]
    a3=['轩','立','玲','子','国','',"节","奇","离","旋","一","七","会","朋","友"]
    a4=["","","","","午","","滴","禾","","土",""]
    name=random.choice(a1)+random.choice(a2)+random.choice(a3)+random.choice(a4)
    return name

#随机生成身份证号
def generId():
    id = "133029"
    id = id + str(random.randint(1970, 1998))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3','10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count % 11)]  # 算出校验码
    return id

def timeTag():  #获取时间参数
    t=time.time()
    hours=random.choice(range(20000))
    enterTime=datetime.datetime.fromtimestamp(t-60*60*hours).strftime('%Y/%m/%d')    #t是当前时间，t后面加上延后多少秒，就可以获得一个延后的时间戳，格式是'%Y-%m-%d %H:%M:%S'
    return enterTime

def writePeopleToTemplate(excel,sheet,person,rowID):
    excel.writeRow(sheet,person,rowID)

def generPersonInfo(n):
    excel=easyExcel(excelFile)
    sheet=excel.getSheet("导入表格")
    for i in range(1,n+1):
        name=generName()
        id="person"+str(i)
        pic="小云"+str(i)+".jpg"
        psw="111112222233333"+str(i)
        sex=random.choice(['Male','Female'])
        org="爱花科技"
        sinanews://params=%7B%22id%22%3A%22hytcerm8333715-comos-zx-cms%22%2C%22type%22%3A%22%22%2C%22isSilence%22%3A%220%22%2C%22skipAd%22%3A%220%22%7D::k=sinawap_clip*zx*zx*wm3049_0015_LAND_hytcerm8333715_uid5238806746*SN_0410001007*1564893292164*https%3A%2F%2Fzx.sina.cn%2Fe%2F2019-08-03%2Fzx-ihytcerm8333715.d.html%3FHTTPS%3D1%26wm%3D3049_0015%26hd%3D1*ustat___172.16.93.32_1564893280_0.50028700_end::ustat=__172.16.93.32_1564893280_0.50028700::opid=15648932922362187548 email='test'+str(i)+'@box.com'
        phoneNum=str(13900000000+i)
        icNum=str(100000000000000000000000000000+i)
        doorCardNum=str(10000000000000000+i)
        idCardNum=generId()
        position=random.choice(['测试工程师','开发工程师','项目经理','HR人员',"保洁人员","快递人员","manager"])
        comments="这是一个备注，用于测试"+str(i)
        extend1 = "extend1" + str(i)
        extend2 = "extend2" + str(i)
        extend3 = "extend3" + str(i)
        extend4 = "extend4" + str(i)
        extend5 = "extend5" + str(i)
        extend6 = "extend6" + str(i)
        extend7 = "extend7" + str(i)
        extend8 = "extend8" + str(i)
        extend9 = "extend9" + str(i)
        extend10 = "extend10" + str(i)
        people=[name,id,pic,psw,sex,org,email,phoneNum,icNum,doorCardNum,idCardNum,"默认1",position,comments,extend1,extend2,extend3,extend4,extend5,extend6,extend7,extend8,extend9,extend10]
        writePeopleToTemplate(excel,sheet,people,i+1)

#generPersonInfo(100)