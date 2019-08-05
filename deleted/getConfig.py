#-*-coding:utf-8-*-
#__author__='maxiaohui'

configPath=r"D:\01.Projects\file\config"

def openConfig(filePath):
    f=open(filePath)
    return f.readlines()

def getConfig(filePath,prop):
    lines = openConfig(filePath)
    value=""
    for line in lines:
        if line.startswith(prop):
            value=line[line.find("=")+1:]
            break
    return value

###执行方法如下：
# d=getConfig(configPath,"deviceId")
# print(d)
