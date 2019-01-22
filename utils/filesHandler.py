#-*-coding:utf-8-*-
#__author__='maxiaohui'
import os  # 引入操作系统模块
import sys  # 用于标准输入输出
from config import config
import random

def search(path, name):
    for f in os.listdir(path):  # path 为根目录
        # print(f)
        if name==f:
            return True
    return False

def randomChoiceFile(path):  #任意选一个文件，返回文件全目录
    list=os.listdir(path)
    f=path+"\\"+random.choice(list)
    return f


if __name__ == "__main__":  #当前脚本运行实例
    path = config.imageFolder
    # name = "BFRT_3G_DVT_2.2.x.d.t.d_01080417-ota.zip"
    # answer = search(path, name)
    # if not answer:
    #     print("查无此文件")
    # else:
    #     print("已经有这个文件了")
    print(randomChoiceFile(path))
