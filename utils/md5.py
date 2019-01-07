#-*-coding:utf-8-*-
#__author__='maxiaohui'

import hashlib

a = "superadmin"
b = hashlib.md5()
b.update(a.encode(encoding='utf-8'))
print('MD5加密前：'+ a)
print('MD5加密后：'+b.hexdigest())

if __name__ == "__main__":  #当前脚本运行实例
    pass