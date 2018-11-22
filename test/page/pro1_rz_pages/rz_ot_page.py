from datetime import datetime, timedelta
from time import sleep

from selenium.webdriver.common.by import By

from test.common.page import Page
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config


class OtAppLocators(Page):
    """
    人资系统：加班申请界面使用的控件定位内容
    """
    ot_butten = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage2')]")#加班申请按钮
    ot_place = (By.XPATH,"//*[contains(text(),'公司内办公')]")#加班地点
    ot_type = (By.XPATH,"//*[contains(text(),'晚上加班')]")
    ot_reason = (By.XPATH,"//textarea[@name='overtimeReasons'and @class='JGFormTextError']")#加班原因
    ot_startdate =(By.XPATH,"//*[@name='startDate'and @class='JGFormIconTextError']")#加班开始时间JGFormIconTextError
    ot_enddate = (By.XPATH,"//*[@name='endDate'and @class='JGFormIconTextError']")#加班结束时间
    ot_submit = (By.XPATH,"//*[contains(text(),'提交')]")#加班提交按钮
    ot_submit_content = (By.XPATH,"//*[@id='dialog_content_div'and @class='content']")#加班申请提交提示框内容
    ot_startdate1 = (By.XPATH, "//*[@name='startDate'and @class='JGFormIconText']")
    ot_enddate1 = (By.XPATH, "//*[@name='endDate'and @class='JGFormIconText']")

    def enter_ot_butten(self):
        '''定位加班申请按钮'''
        try:
            self.find_element(*self.ot_butten).click()
        except Exception as e:
            print('加班申请按钮未找到，原因%s'%e)

    def enter_ot_place(self):
        '''输入加班类型'''
        try:
            self.find_element(*self.ot_place).click()
        except Exception as e:
            print('加班地点按钮未找到，原因%s'%e)

    def enter_ot_type(self):
        '''输入加班类型'''
        try:
            self.find_element(*self.ot_type).click()
        except Exception as e:
            print('加班类型按钮未找到，原因%s' % e)

    def enter_ot_reason(self):
        "输入加班原因"
        return self.find_element(*self.ot_reason).send_keys(u'测试加班申请')

    def enter_date_time(self):
        my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        x = 0

        while my_date:
            # 赋值当前时间给开始时间和结束时间

            self.find_element(*self.ot_startdate).clear()
            sleep(1)
            self.find_element(*self.ot_enddate).clear()
            sleep(1)
            self.find_element(*self.ot_startdate).send_keys(my_date)
            sleep(4)
            self.find_element(*self.ot_enddate).send_keys(my_date)
            sleep(4)
            self.find_element(*self.ot_submit).click()
            sleep(2)
            self.content = self.driver.find_element(*self.ot_submit_content).text
            print(self.content)
            sleep(7)
            if self.content == '提交成功':
                self.sucess_content = self.content
                break
            else:
                self.find_element(*self.ot_startdate1).clear()
                self.find_element(*self.ot_enddate1).clear()
                x = x + 1
                my_date = (datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d")

if __name__ == '__main__':
    URL = Config().get('URL1')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
    page.userlogin()
    result = OtAppLocators(page)
    result.enter_ot_butten()
    sleep(1)
    result.enter_ot_place()
    sleep(1)
    result.enter_ot_reason()
    sleep(1)
    result.enter_ot_type()
    result.enter_date_time()






