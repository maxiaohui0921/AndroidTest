#-*-coding:utf-8-*-
#__author__='maxiaohui'

#device information
deviceId="192.168.29.248:5555"
devicePsw="2580"
deviceSN='FC241118370034'

#log information
log_path='F:\\log'

#adb keyword
faceRecognizationKey="MatchProcessor"
issueBySaasKey="PRETTY_LOGGER"
importLocalKey='AddPeopleModel'
exportLocalKey=""    #还不是很清楚

#event keywords  从log中分析数据时使用
oneByonePass="match: success = 0"  #识别成功的次数    失败的次数不准确
oneByNPass="statusCode = 0"  #识别成功的次数
saasIssueSuccess="add person, result: 0"
importLocal="add people"
exportLocal=""

#logcommand
logcmd_fr = "adb -s %s adb -v time |grep %s" % (deviceId,faceRecognizationKey)
logcmd_saas_issue = "adb -s %s adb -v time |grep %s" % (deviceId,issueBySaasKey)
logcmd_import = "adb -s %s adb -v time |grep %s" % (deviceId,importLocalKey)
logcmd_import = "adb -s %s adb -v time |grep %s" % (deviceId,exportLocalKey)
