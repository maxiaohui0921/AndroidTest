#-*-coding:utf-8-*-
#__author__='maxiaohui'
import os,re
from utils.excel import easyExcel
from config import config

#5192 root     20   0  13% R     1   9232K   2988K  fg top  把# K移除
def cpuFromLineToList(line):  #传入的是未处理过的字符串
    lineList=line.split()
    for i in [4,7,8]:
        lineList[i]=int(lineList[i][:-1])
    return lineList

def memoryFromLineToList(line):
    size=re.findall("(.*)K:", line)[0].replace(",","")
    package=re.findall("K: (com.*) \(",line)[0]
    pidNumber=re.findall("pid (\d+)",line)[0]
    return [size,package,pidNumber]


def cpuTxtToExcel(txtFile):
    excelName=os.path.splitext(os.path.split(txtFile)[1])[0]+".xlsx"
    excelFile=os.path.join(config.log_path,excelName)
    excel=easyExcel()
    xsheet=excel.addSheet(excelName[:-5])
    excel.writeRow(xsheet, config.topTitle.split(), 1)
    lines=open(txtFile).readlines()
    rowId=2
    for line in lines:
        excel.writeRow(xsheet, cpuFromLineToList(line), rowId)
        rowId+=1
    excel.saveAs(excelFile)
    print(excelFile)

def memoryTxtToExcel(txtFile):
    excelName = os.path.splitext(os.path.split(txtFile)[1])[0] + ".xlsx"
    excelFile = os.path.join(config.log_path, excelName)
    excel = easyExcel()
    xsheet = excel.addSheet(excelName[:-5])
    excel.writeRow(xsheet, ["Memory","Package","PID"], 1)
    lines = open(txtFile).readlines()
    rowId = 2
    for line in lines:
        excel.writeRow(xsheet, memoryFromLineToList(line), rowId)
        rowId += 1
    excel.saveAs(excelFile)
    print(excelFile)

if __name__ == "__main__":  #当前脚本运行实例
    txtF="F:\\log1\\memory_0115154833.txt"
    memoryTxtToExcel(txtF)