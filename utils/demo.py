#-*-coding:utf-8-*-
#__author__='maxiaohui'
from uiautomator import Device

deviceId="192.168.29.250:5555"
d=Device(deviceId)
d(resourceId="com.opnext.setting:id/ll_face_recognize").click()