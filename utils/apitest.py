#-*-coding:utf-8-*-
#__author__='maxiaohui'
import requests
import json,time,warnings,urllib3
from config import config
from requests.cookies import RequestsCookieJar
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

    timestamp=int(round(time.time() * 1000))
    params={"uname":"superadmin","pass":"080915df04565b0a47dd5889d2eedb5d","t":"1546572473407"}
    cookies={"bx_user_lang":"zh-CN"}
    # cookie_jar = RequestsCookieJar()
    # cookie_jar.set(redirect_uri="https%253A%252F%252F172.16.20.219%252F%2523%252Fmain", bx_user_lang="zh-CN", refresh_time="1546422174243",JSESSIONID='CE66E797CC83E3235FBA1EC2B31E2094',authTimeoutId=2,OAUTH_SESSIONID='6704E511C4C4073C16C399A180356063',ACCESS_URL='/oauth2/authorize?client_id=bbox-service&response_type=code&redirect_uri=https%3A%2F%2F172.16.20.219%2F%23%2Fmain')
    # cookie_jar.set("redirect_uri","https%253A%252F%252F172.16.20.219%252F%2523%252Fmain")
    # cookie_jar.set("bx_user_lang","zh-CN")
    # cookie_jar.set('refresh_time',"1546422174243")
    # cookie_jar.set('JSESSIONID','CE66E797CC83E3235FBA1EC2B31E2094')
    # cookie_jar.set('authTimeoutId','2')
    # cookie_jar.set('OAUTH_SESSIONID','6704E511C4C4073C16C399A180356063')
    # cookie_jar.set('ACCESS_URL','/oauth2/authorize?client_id=bbox-service&redirect_uri=https%3A%2F%2F172.16.20.219%2F%23%2Fmain&response_type=code')
    # cookie_jar.set('ACCESS_URL', 'redirect_uri=https%3A%2F%2F172.16.20.219%2F%23%2Fmain')

    rs1=requests.post(config.host+"/sso/_login",data=params,verify=False,cookies=cookies,allow_redirects=False)
    print(rs1.cookies)
    # cookies['redirect_uri']=rs1.cookies['redirect_uri']
    # cookies['authTimeoutId'] =rs1.cookies['authTimeoutId']
    #
    # params2={"callbackUrl":"https%3A%2F%2F172.16.20.219%2F%23%2Fmain"}
    # rs2 = requests.get(config.host + "/account/login", data=params2, verify=False, cookies=cookies, allow_redirects=True)
    # cookie_jar.set(rs1.cookies)
    # print(rd1)
    # rd=requests.get(rd1,verify=False,allow_redirects=False,cookies=cookie_jar)


