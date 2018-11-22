from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By
from test.common.page import Page
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config

class OutApplyLocators(Page):
    """
    人资系统：外出申请界面使用的控件定位内容
    """
    outApply_button = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage6')]") #外出申请按钮
    outReasons_text = (By.XPATH,"//textarea[@name='outReasons'and @class='JGFormTextError']") #外出原因文本框
    oa_startDate = (By.XPATH,"//input[starts-with(@id,'isc') and @name='startDate']") #开始时间
    oa_endDate = (By.XPATH,"//input[starts-with(@id,'isc')and @name='endDate']") #结束时间
    oa_startDate_Form = (By.XPATH,"//input[starts-with(@id,'isc') and @name='startDate']") #开始时间控件
    oa_endDate_Form = (By.XPATH,"//input[starts-with(@id,'isc') and @name='endDate']") #结束时间控件
    oa_startFrame = (By.XPATH,"//input[starts-with(@id,'isc_196') and @classname,'JGFormIconText'])") #开始时段
    oa_endFrame = (By.XPATH,"//input[starts-with(@id,'isc_19J') and @classname,'JGFormIconText']")#结束时段
    oa_submit_content = (By.XPATH, "//*[@id='dialog_content_div'and @class='content']") #提交后的对话框
    oa_submit = (By.XPATH,"//*[contains(text(),'提交')]")
    #//input[starts-with(@id,'vp_hr_portal_myApply_web_JGImage6')] 查找id属性中开始位置包含'vp_hr_portal_myApply_web_JGImage6'关键字的页面元素

    def enter_outApply_button(self):
        '''定位外出申请按钮'''
        try:
            self.find_element(*self.outApply_button).click()
        except Exception as e:
            print('外出申请按钮未找到，原因%s'%e)


    def outApply_reason(self):
        '''输入外出原因'''
        return self.find_element(*self.outReasons_text).send_keys(u'测试外出申请')

    def enter_date_time(self):
        '''选择开始日期'''

        my_date = datetime.strftime(datetime.now(), '%Y-%m-%d')
        x = 0
        while my_date:
            # 赋值当前时间给开始时间和结束时间
            self.find_element(*self.oa_startDate).clear()
            sleep(1)
            self.find_element(*self.oa_endDate).clear()
            sleep(1)
            self.find_element(*self.oa_startDate).send_keys(my_date)
            sleep(3)
            self.find_element(*self.oa_endDate).send_keys(my_date)
            sleep(3)
            self.find_element(*self.oa_submit).click()
            sleep(3)
            self.content = self.driver.find_element(*self.oa_submit_content).text
            print(self.content)
            sleep(5)

            if self.content == '提交成功':
                self.success_content = self.content
                break
            else:
                self.find_element(*self.oa_startDate_Form).clear()
                self.find_element(*self.oa_endDate_Form).clear()
                x = x + 1
                my_date = (datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d")#timedelta(days)实例支持加减乘除操作

if __name__ == '__main__':
    URL = Config().get('URL1')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
    page.userlogin()
    result = OutApplyLocators(page)
    result.enter_outApply_button()
    sleep(1)
    result.outApply_reason()
    sleep(1)
    result.enter_date_time()


