class Register:
    def __init__(self,driver):
        self.driver = driver
    def test1(self,web):
        import time
        '''进入网址'''
        self.driver.get(web)
        time.sleep(2)
        value = self.driver.execute_script("return $('.SnailInput').attr('placeholder');")
        value2 = self.driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div[2]/input").get_attribute("placeholder")
        value3 = self.driver.find_element_by_css_selector('[type = "submit"]').text
        return value+value2+value3
        self.driver.quit()
    def test2(self,web):
        "跳转至忘记密码界面"
        import time
        self.driver.get(web)
        self.driver.find_element_by_class_name("GoResetPassword").click()
        time.sleep(2)
        skiptitle = self.driver.title
        title = self.driver.find_element_by_class_name("InputTitleText").text
        return title
        self.driver.quit()
    def test3(self,web):
        "跳转至注册界面"
        import time
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        title = self.driver.find_element_by_css_selector('[class = "InputTitleText"]').text
        return title
    def test4(self,web):
        "无内容直接登录"
        import time
        self.driver.get(web)
        time.sleep(2)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton LoginBtn"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test5(self,web):
        "有账号1无密码登录"
        import time
        self.driver.get(web)
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(1)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton LoginBtn"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test6(self,web):
        "有账号1密码1登录，密码错误"
        import time
        self.driver.get(web)
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(1)
        passsword = self.driver.find_element_by_css_selector('[name = "Password"]')
        passsword.click()
        passsword.clear()
        passsword.send_keys("1")
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton LoginBtn"]').click()
        time.sleep(2)
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test7(self,web):
        "正确账号11位，错误密码，登录验证"
        import time
        self.driver.get(web)
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(13199044512)
        passsword = self.driver.find_element_by_css_selector('[name = "Password"]')
        passsword.click()
        passsword.clear()
        passsword.send_keys("1")
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton LoginBtn"]').click()
        time.sleep(2)
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test8(self,web):
        "正确账号11位，正确密码123，登录验证"
        import time
        self.driver.get(web)
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(13199044512)
        passsword = self.driver.find_element_by_css_selector('[name = "Password"]')
        passsword.click()
        passsword.clear()
        passsword.send_keys("123")
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton LoginBtn"]').click()
        time.sleep(2)
        title = self.driver.execute_script("return $ ('.PageTitle').attr('value');")
        return title

    def test9(self, web):
        "正确邮箱，正确密码，登录验证"
        import time
        self.driver.get(web)
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys("test1@qq.com")
        passsword = self.driver.find_element_by_css_selector('[name = "Password"]')
        passsword.click()
        passsword.clear()
        passsword.send_keys("123")
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton LoginBtn"]').click()
        time.sleep(2)
        title = self.driver.execute_script("return $ ('.PageTitle').attr('value');")
        return title
    def test10(self,web):
        "跳转至注册界面,并进行检查"
        import time
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        value = self.driver.execute_script("return $ ('.SnailInput').attr('placeholder');")
        value1 = self.driver.execute_script('return $ ("[name = Password]").attr("placeholder");')
        value3 = self.driver.execute_script('return $ ("[name = code]").attr("placeholder");')
        value4 = self.driver.find_element_by_css_selector('[class = "InputWarningA"]').text
        value5 = self.driver.find_element_by_css_selector('[class = "InputSubmitButton RegisterBtn"]').text
        value6 = self.driver.find_element_by_css_selector('[class = "SendCode RegisterSendCode"]').text
        value7 = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/p[2]/a").text
        return  value+value1+value3+value4+value5+value6+value7

    def test11(self, web):
        "跳转至海外注册界面,并进行检查"
        import time
        from selenium.webdriver.support.select import  Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        click = self.driver.find_element_by_css_selector('[class = "country-code"]')
        s = Select(click).first_selected_option.text
        return s
    def test12(self, web):
        "跳转至登录界面,并进行检查"
        import time
        from selenium.webdriver.support.select import  Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/p[2]/a").click()
        title = self.driver.find_element_by_css_selector('[class = "InputTitleText"]').text
        return title

    def test13(self, web):
        "直接点击注册"
        import time
        from selenium.webdriver.support.select import Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton RegisterBtn"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test14(self, web):
        "直接点击发送验证码"
        import time
        from selenium.webdriver.support.select import  Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('[class = "SendCode RegisterSendCode"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title

    def test15(self, web):
        "手机号输入1直接注册"
        import time
        from selenium.webdriver.support.select import Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(1)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton RegisterBtn"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test16(self,web):
        "输入11位手机，直接注册"
        import time
        from selenium.webdriver.support.select import Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(12345678910)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton RegisterBtn"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title

    def test17(self, web):
        "输入11位手机号，发送验证码"
        import time
        from selenium.webdriver.support.select import Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(13199044512)
        self.driver.find_element_by_css_selector('[class = "SendCode RegisterSendCode"]').click()
        time.sleep(2)
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title

    def test18(self, web):
        "输入11位手机号，验证码位123，后登录"
        import time
        from selenium.webdriver.support.select import Select
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(12345678910)
        verify = self.driver.find_element_by_css_selector('[class = "SnailInput CodeInput"]')
        verify.click()
        verify.clear()
        verify.send_keys(123)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton RegisterBtn"]').click()
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        return title
    def test19(self, web):
        "输入11位手机号，,密码123，验证码位123，后登录"
        import time
        self.driver.get(web)
        self.driver.find_element_by_css_selector('[class = "InputWarningA"]').click()
        time.sleep(2)
        user = self.driver.find_element_by_css_selector('[name = "Username"]')
        user.click()
        user.clear()
        user.send_keys(13199044512)
        password = self.driver.find_element_by_css_selector('[name = "Password"]')
        password.click()
        password.clear()
        password.send_keys(123)
        verify = self.driver.find_element_by_css_selector('[class="SnailInput CodeInput"]')
        verify.click()
        verify.clear()
        verify.send_keys(123)
        self.driver.find_element_by_css_selector('[class = "InputSubmitButton RegisterBtn"]').click()
        time.sleep(2)
        title = self.driver.find_element_by_css_selector('[class = "ErrorMsg"]').text
        print(title)
        return title


