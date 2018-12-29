#-*-coding:utf-8-*-
#__author__='maxiaohui'
import requests
import json
from config import config

def testAPI(method,url,data={},header={},params='',host=config.host):

    try:  # 判断传参类型如果是json格式
        if header['content-type'].find('json') >= 0:
            data = json.dumps(data)
    except KeyError:
        pass
    response=''
    url=host+url
    if method == ("post" or "POST"):  # 以下是执行测试
        response = requests.post(url, data=data, params=params, headers=header,verify=False)
    elif method in ("get", "GET"):
        response = requests.get(url, data=data, params=params, headers=header,verify=False)
    elif method == "put":
        response = requests.put(url, data=data, params=params, headers=header,verify=False)
    elif method == "delete":
        response = requests.delete(url, data=data, params=params, headers=header,verify=False)
    return response

def responseHandle(response):   #对api接口执行返回的response进行处理
    statusCode = response.status_code    #api接口执行状态码
    #if response.headers['content-type'].find("application/json") >= 0:   # 对于不同的返回进行不同处理，有时候返回的不是json，例如图片，这里不再做处理
    responseData = response.content.decode('utf-8').replace("'", "")    # 字符串类型，用loads变成字典
    try:
        message = response.json().get('msg')
    except KeyError:                                                     #当接口出现问题时，response取message的值返回回来，正常结果是取的是msg值返回回来
        print("当前接口有问题，log如下：")
        print(json.dumps(json.loads(responseData),ensure_ascii=False,indent=4))
        message = response.json().get('message')
    responseDict=json.loads(responseData)
    return statusCode,message,responseDict #返回的responseData是一个字典值

if __name__ == "__main__":  #当前脚本运行实例
    method="get"
    url="/agoldbase_rom_new/bb_dev_3g_dailybuild/"
    swHost="http://192.168.100.136:8000"
    response=testAPI(method,url,host=swHost)
    print(response.text)


