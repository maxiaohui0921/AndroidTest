#-*-coding:utf-8-*-
#__author__='maxiaohui'
from utils import apitest,filesHandler
import unittest
from config import config

class webserver(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01login_correct(self):
        r=apitest.testAPI("get","/api/account/login",params={"password":"2580"})
        config.cookies=r.cookies
        print(r.json())
        self.assertIn("success",r.text)

    # @unittest.skip("跳过当前测试")
    def test_02login_error(self):
        r = apitest.testAPI("get", "/api/account/login", params={"password": "324323"})
        print(r.json())
        self.assertIn('login_password_error',r.text)

    # @unittest.skip("跳过当前测试")
    def test_03add_batch(self):
        r=apitest.testAPI("get","/api/persons/batch",cookies=config.cookies)
        print(r.json())

    def test_04uploadPic(self):
        f=open(filesHandler.randomChoiceFile(config.imageFolder),"rb")
        files={"file":("blob",f,"image/jpeg")}
        r=apitest.testAPI("post","/api/upload/image",cookies=config.cookies,files=files)
        print(r.json())
        f.close()


if __name__ == "__main__":  #当前脚本运行实例
    unittest.main()