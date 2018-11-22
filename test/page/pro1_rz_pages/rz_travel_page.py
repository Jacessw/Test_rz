from datetime import datetime, timedelta
from time import sleep

from selenium.webdriver.common.by import By

from test.common.page import Page
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config


class TravelAppLocators(Page):
    """
    人资系统：出差申请界面使用的控件定位内容
    """
    travel_butten = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage3')]")#出差申请按钮
    travel_place = (By.NAME,"travelPlace")#出差地点
    travel_reason = (By.NAME,"travelReason")#出差事由
    travel_startdate = (By.XPATH,"//*[@name='startDate'and @class='JGFormIconTextError']")#开始时间
    travel_enddate = (By.XPATH,"//*[@name='endDate'and @class='JGFormIconTextError']")#结束时间
    travel_submit = (By.XPATH, "//*[contains(text(),'提交')]") #出差申请提交按钮
    travel_submit_content = (By.XPATH,"//*[@id='dialog_content_div'and @class='content']") #出差申请提交后弹窗内容
    travel_startdate1 = (By.XPATH, "//*[@name='startDate'and @class='JGFormIconText']")
    travel_enddate1 = (By.XPATH, "//*[@name='endDate'and @class='JGFormIconText']")

    def enter_travel_butten(self):
        '''定位出差申请按钮'''
        try:
            self.find_element(*self.travel_butten).click()
        except Exception as e:
            print('出差申请按钮未找到，原因%s'%e)


    def enter_travel_place(self):
        '''输入出差地点'''
        try:
            self.find_element(*self.travel_place).send_keys("广州")
        except Exception as e:
            print('出差地点按钮未找到，原因%s'%e)

    def enter_travel_reason(self):
        '''输入加班类型'''
        try:
            self.find_element(*self.travel_reason).send_keys("出差理由：工作调研")
        except Exception as e:
            print('出差事由按钮未找到，原因%s' % e)


    def enter_date_time(self):
        my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        x = 0
        while my_date:
            # 赋值当前时间给开始时间和结束时间
            self.find_element(*self.travel_startdate).clear()
            sleep(1)
            self.find_element(*self.travel_enddate).clear()
            sleep(1)
            self.find_element(*self.travel_startdate).send_keys(my_date)
            sleep(4)
            self.find_element(*self.travel_enddate).send_keys(my_date)
            sleep(4)
            self.find_element(*self.travel_submit).click()
            sleep(2)
            self.content = self.driver.find_element(*self.travel_submit_content).text #get_attribute('innerHTML')
            print("**************")
            print(self.content)
            sleep(7)
            if self.content == '提交成功':
                self.sucess_content = self.content
                break
            else:
                self.find_element(*self.travel_startdate1).clear()
                self.find_element(*self.travel_enddate1).clear()
                x = x + 1
                my_date = (datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d")

if __name__ == '__main__':
    URL = Config().get('URL')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
    page.userlogin()
    result = TravelAppLocators(page)
    result.enter_travel_butten()
    sleep(2)
    result.enter_travel_place()
    result.enter_travel_reason()
    result.enter_date_time()
    page.quit()






