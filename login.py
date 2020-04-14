from Register import Register
from selenium import webdriver
import unittest
import time
from Register import Register
x = input("输入你的驱动地址")
driver = webdriver.Chrome(x)
web = 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage'
class Test(unittest.TestCase):
    #测试用例前置动作
    def setUp(self):
        print("test start:")
    #测试用例后置动作
    def tearDown(self):
        print("test end")
    def test1(self):
        c = Register(driver)
        title = c.test1(web)
        self.assertEqual(title,"邮箱/手机号码密码登录")
    def test2(self):
        c = Register(driver)
        title = c.test2(web)
        self.assertEqual(title,"找回密码")
    def test3(self):
        c = Register(driver)
        title = c.test3(web)
        self.assertEqual(title,"注册")
    def test4(self):
        c = Register(driver)
        title = c.test4(web)
        self.assertEqual(title,"帐号不能为空")
    def test5(self):
        c = Register(driver)
        title = c.test5(web)
        self.assertEqual(title,"密码不能为空")
    def test6(self):
        c = Register(driver)
        title = c.test6(web)
        self.assertEqual(title,"账号不存在")
    def test7(self):
        c = Register(driver)
        title = c.test7(web)
        self.assertEqual(title,"密码错误")
    def test8(self):
        c = Register(driver)
        title = c.test8(web)
        self.assertEqual(title,"速涡手游加速器-充值")
    def test9(self):
        c = Register(driver)
        title = c.test9(web)
        self.assertEqual(title,"速涡手游加速器-充值")
    def test10(self):
        c = Register(driver)
        title = c.test10(web)
        self.assertEqual(title,"手机号码密码验证码海外用户注册注册发送验证码登录")
    def test11(self):
        c = Register(driver)
        title = c.test11(web)
        self.assertEqual(title,"阿富汗(+93)")
    def test12(self):
        c = Register(driver)
        title = c.test12(web)
        self.assertEqual(title,"登录")
    def test13(self):
        c = Register(driver)
        title = c.test13(web)
        self.assertEqual(title,"手机号不能为空")
    def test14(self):
        c = Register(driver)
        title = c.test14(web)
        self.assertEqual(title,"用户名不能为空")
    def test15(self):
        c = Register(driver)
        title = c.test15(web)
        self.assertEqual(title,"手机号码格式不正确")
    def test16(self):
        c = Register(driver)
        title = c.test16(web)
        self.assertEqual(title,"验证码不能为空")
    def test17(self):
        c = Register(driver)
        title = c.test17(web)
        self.assertEqual(title,"该手机号已经注册过帐号")
    def test18(self):
        c = Register(driver)
        title = c.test18(web)
        self.assertEqual(title,"密码不能为空")
    def test19(self):
        c = Register(driver)
        title = c.test19(web)
        self.assertEqual(title,"请先获取验证码")

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Test("test1"))
    suit.addTest(Test("test2"))
    suit.addTest(Test("test3"))
    suit.addTest(Test("test4"))
    suit.addTest(Test("test5"))
    suit.addTest(Test("test6"))
    suit.addTest(Test("test7"))
    suit.addTest(Test("test8"))
    suit.addTest(Test("test9"))
    suit.addTest(Test("test10"))
    suit.addTest(Test("test11"))
    suit.addTest(Test("test12"))
    suit.addTest(Test("test13"))
    suit.addTest(Test("test14"))
    suit.addTest(Test("test15"))
    suit.addTest(Test("test16"))
    suit.addTest(Test("test17"))
    suit.addTest(Test("test18"))
    suit.addTest(Test("test19"))

    runner = unittest.TextTestRunner()
    runner.run(suit)