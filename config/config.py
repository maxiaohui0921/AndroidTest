#-*-coding:utf-8-*-
#__author__='maxiaohui'

#device information
deviceId="192.168.28.203:5555"
devicePsw="2580"
deviceSN='FC2222'

#log information
log_path='F:\\log1'
logKeyWord=''

#adb keyword
faceRecognizationKey="MatchP"
issueBySaasKey="PRETT"
importLocalKey='AddPe'
exportLocalKey=""    #还不是很清楚

#event keywords  从log中分析数据时使用
oneByonePass="match: = 0"  #识别成功的次数    失败的次数不准确
oneByNPass="statusCode = 0"  #识别成功的次数
saasIssueSuccess="add person: 0"
importLocal="add people"
exportLocal=""

#logcommand
logcmd_fr = "adb -s %s adb -v time |grep %s" % (deviceId,faceRecognizationKey)
logcmd_saas_issue = "adb -s %s adb -v time |grep %s" % (deviceId,issueBySaasKey)
logcmd_import = "adb -s %s adb -v time |grep %s" % (deviceId,importLocalKey)
logcmd_import = "adb -s %s adb -v time |grep %s" % (deviceId,exportLocalKey)

#SaasHost
host="http://172.16.20.219"

monkeyLogKeyWord=['ANR in','CRASH','OOM','Exception','Monkey finished']
oomKeyWord=['GC_FOR_ALLOC','GC_EXPLICIT','GC_CONCURRENT','GC_BEFORE_OOM']
topTitle='PID USER PR NI CPU% S #THR VSS RSS PCY Name'

#本地机器，识别的时候成功和失败的关键字  1:1 1:N快速和安全都没有关系，都有这个字段
frPass='TERMINAL_PASS'
frFail='TERMINAL_FAILURE'

#webserver
webserverHost="http://192.168.28.1:8080"
imageFolder=r"F:\U盘\5000"