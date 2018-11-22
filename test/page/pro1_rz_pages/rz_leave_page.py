from datetime import datetime, timedelta ,time
from time import sleep

from selenium.webdriver.common.by import By

from test.common.page import Page
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config


class LeaveAppLocators(Page):
    """
    人资系统：请假申请界面使用的控件定位内容
    """
    leave_butten = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage1') and @class='img-responsive default pull-left']") #请假申请按钮
    leave_type = (By.XPATH,"//*[contains(text(),'事假')]")  #必填项申请假别选择事假
    leave_reason = (By.XPATH,"//*[@class='JGFormTextError'and @name='Cause']") #必填项请假原因
    startdate = (By.XPATH,"//input[starts-with(@id,'isc') and @name='startDate']") #开始时间
    enddate = (By.XPATH,"//input[starts-with(@id,'isc')and @name='endDate']")#结束时间
    LeaveSubmit = (By.XPATH,"//*[contains(text(),'提交')]")#请假提交按钮
    LeaveSubmitContent = (By.XPATH,"//div[@id='dialog_content_div'and @class='content']")#请假申请提交提示框内容

    def enter_leave_butten(self):
        "定位请假申请按钮"
        #self.find_element(*self.leave_butten).click()
        try:
            self.find_element(*self.leave_butten).click()
        except Exception as e:
            print('请假申请按钮未找到，原因%s'%e)


    def enter_leave_type(self):
        "输入请假类型"
        try:
            self.find_element(*self.leave_type).click()
        except Exception as e:
            print('请假类型未找到，原因%s' % e)

    def enter_leave_reason(self):
        "输入请假原因"
        return self.find_element(*self.leave_reason).send_keys(u'测试请假申请')

    def enter_date_time(self):
        my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        x = 0
        while my_date:

            # 赋值当前时间给开始时间和结束时间
            self.find_element(*self.startdate).clear()
            sleep(1)
            self.find_element(*self.enddate).clear()
            sleep(1)
            self.find_element(*self.startdate).send_keys(my_date)
            sleep(2)
            self.find_element(*self.enddate).send_keys(my_date)
            sleep(2)
            self.find_element(*self.LeaveSubmit).click()
            sleep(4)
            self.content = self.driver.find_element(*self.LeaveSubmitContent).get_attribute('innerHTML')
            print(self.content)
            sleep(4)
            if self.content == '提交成功':
                self.sucess_content = self.content
                break
            else:
                x = x + 1
                my_date = (datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d") #timedelta(days)实例支持加减乘除操作

if __name__ == '__main__':
    URL = Config().get('URL')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False,implicitly_wait=20)
    page.userlogin()
    result = LeaveAppLocators(page)
    sleep(2)
    result.enter_leave_butten()
    sleep(2)
    result.enter_leave_type()
    sleep(2)
    result.enter_leave_reason()
    sleep(2)
    result.enter_date_time()






