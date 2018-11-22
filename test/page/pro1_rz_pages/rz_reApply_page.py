from datetime import datetime, timedelta
from time import sleep

from selenium.webdriver.common.by import By

from test.common.page import Page
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config


class reApplyLocators(Page):
    """
    人资系统：加班申请界面使用的控件定位内容
    """
    re_Apply_button = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage5')]")#调动申请按钮
    re_Imp_button = (By.XPATH,"//*[contains(text(),'调入部门')]")#调入部门弹框
    re_Choose_department = (By.XPATH, "//*[contains(text(),'企业管理部')]")  # 选择调入的部门
    re_Imp_comfirm = (By.XPATH, "//*[contains(text(),'确认')]")  # 调入部门确定按钮
    re_Imp_button_1 = (By.XPATH, "//*[contains(text(),'调入职位')]")  # 调入职位弹框
    re_Imp_position = (By.XPATH, "//*[contains(text(),'副总裁')]")  #调入职位
    re_Imp_comfirm_2 = (By.XPATH, "//*[contains(text(),'确定')]")  # 调入职位确定按钮
    re_Reason = (By.XPATH, "//textarea[@name='moveReason' and @class='JGFormTextError']")  #调动原因
    re_Add_button = (By.XPATH, "//*[contains(text(),'新增')]")  # 新增按钮
    re_Deliver = (By.XPATH, "//table[@class='listTable' and @width='610']/tbody/tr/td[2]")  #交接事项名称
    re_Deliver_IN = (By.XPATH, "//input[@type='TEXT'and @name='contentName']")  # 交接事项内嵌框
    re_Deliver_content = (By.XPATH, "//table[@class='listTable' and @width='610']/tbody/tr/td[3]")  #具体交接内容
    re_Deliver_content_IN = (By.XPATH, "//input[@type='TEXT'and @name='content']")  # 具体交接内容内嵌框
    re_Submit_button = (By.XPATH, "//*[contains(text(),'暂存')]")  # 暂存按钮



    def enter_reApply_button(self):
        '''调动申请按钮'''
        try:
            self.find_element(*self.re_Apply_button).click()
        except Exception as e:
            print('调动申请按钮未找到，原因%s'%e)

    def reApply_click_depart(self):
        '''点击调入部门'''
        try:
            self.find_element(*self.re_Imp_button).click()
        except Exception as e:
            print('选择调入部门按钮未找到，原因%s'%e)

    def reApplydepart(self):
        '''选择调入部门'''
        try:
            self.find_element(*self.re_Choose_department).click()
            self.find_element(*self.re_Imp_comfirm).click()
        except Exception as e:
            print('选择调入部门按钮未找到，原因%s'%e)

    def reApplyposition(self):
        '''输入调入职位'''
        try:
            self.find_element(*self.re_Imp_button_1).click()
            sleep(3)
            self.find_element(*self.re_Imp_position).click()
            self.find_element(*self.re_Imp_comfirm_2).click()
        except Exception as e:
            print('调入职位按钮未找到，原因%s' % e)

    def reApplyreason(self):
        '''输入调动原因'''
        return self.find_element(*self.re_Reason).send_keys(u'测试调动申请')

    def reApply_add(self):
        '''新增操作'''
        return self.find_element(*self.re_Add_button).click()

    def reApply_Deliver(self):
        '''输入交接事项名称'''
        try:
            self.find_element(*self.re_Deliver).click()
            self.find_element(*self.re_Deliver).click()
            self.find_element(*self.re_Deliver_IN).send_keys(u"测试交接事项名称")
        except Exception as e:
            print('输入交接事项名称未找到，原因%s' % e)

    def reApply_Deliver_content(self):
        '''输入具体交接内容'''
        try:
            self.find_element(*self.re_Deliver_content).click()
            self.find_element(*self.re_Deliver_content).click()
            self.find_element(*self.re_Deliver_content_IN).send_keys(u"测试具体交接内容")
        except Exception as e:
            print('具体交接内容未找到，原因%s' % e)

    def reApply_Submit(self):
        '''暂存按钮'''
        try:
            self.find_element(*self.re_Submit_button).click()
        except Exception as e:
            print('无法定位暂存按钮 %s' %e)

if __name__ == '__main__':
    URL = Config().get('URL')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
    page.userlogin()
    result = reApplyLocators(page)
    result.enter_reApply_button()
    sleep(2)
    result.reApply_click_depart()
    sleep(2)
    result.reApplydepart()
    sleep(4)
    result.reApplyposition()
    sleep(2)
    result.reApplyreason()
    sleep(2)
    result.reApply_add()
    sleep(2)
    result.reApply_Deliver()
    sleep(2)
    result.reApply_Deliver_content()
    sleep(2)
    result.reApply_Submit()








