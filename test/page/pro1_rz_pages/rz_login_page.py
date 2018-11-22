from selenium.webdriver.common.by import By
from test.common.page import Page
import time
from utils.config import Config

class RZLoginPage(Page):
    '''登录功能涉及的按钮定位'''
    loc_search_username = (By.XPATH,"//input[@widgetcode='JGTextBox1']")
    loc_search_password = (By.XPATH,"//input[@widgetcode='JGPasswordBox1']")
    loc_login_button = (By.XPATH,"//*[@widgetcode='JGButton1']")
    loc_login_sucess = (By.XPATH, "//span[contains(text(),'登录时间')] ")
    loc_login_fail = (By.ID, "dialog_content_div")

    def userlogin(self, username='wangting', password=8):
        '''
        系统登录设置两个变量
        :param username:获取excel的username,默认登录的账号chenyc
        :param password:获取exce的password，默认登录账号的密码
        :return:完成登录操作
        '''
        self.find_element(*self.loc_search_username).send_keys(username)
        self.find_element(*self.loc_search_password).send_keys(password)
        self.find_element(*self.loc_login_button).click()
        time.sleep(3)

    def result_name(self):
        '''
        Selenium WebDriver 只会与可见元素交互，所以获取隐藏元素的文本总是会返回空字符串
        在某些情况下，我们需要获取隐藏元素的文本。这些内容可以使用element.attribute('attributeName'),
        通过textContent, innerText, innerHTML等属性获取。

        :return: 依据excel登录用例获取登录成功或者失败返回结果给主程序unittest做判断
        '''
        fail_text = self.find_element(*self.loc_login_fail).get_attribute('innerHTML')

        if fail_text:
            return fail_text
        else:
            sucess_text = self.find_element(*self.loc_login_sucess).text
            return sucess_text

    def get_login_name(self):
        '''
        依据默认登录成功的账号获取成功登录的text，方便后续做业务场景
        :return:
        '''
        login_text = self.find_element(*self.loc_login_sucess).text
        return login_text

if __name__ == '__main__':
        URL = Config().get('URL')
        page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
        page.userlogin()
        print(page.get_login_name())
        page.quit()
