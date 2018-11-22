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
    trApply_button = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage5')]")#调动申请按钮
    trApply_imp_button = (By.XPATH,"//*[contains(text(),'调入部门')]")#调入部门弹框
    trApply_choose_department = (By.XPATH, "//*[@class='JGBaseGridTallCellSelected' and contains(text(),'企业管理部')")  # 选择调入的部门
    trApply_imp_comfirm = (By.XPATH, "//*[@id='isc_1CH'] and @class='JGButtonOver'")  # 调入部门确定按钮
    trApply_imp_button1 = (By.XPATH, "//*[contains(text(),'调入职位')]")  # 调入职位弹框
    trApply_imp_position = (By.XPATH, "//*[@class='JGBaseGridLineTallCellSelected' and contains(text(),'架构师')]")  #调入职位
    trApply_imp_comfirm2 = (By.XPATH, "//*[@class='JGButton' and contains(text(),'确定')]")  # 调入职位确定按钮
    trApply_reason = (By.XPATH, "//*[@name='moveReason' and @class='JGFormTextError')]")  #调动原因
    trApply_add = (By.XPATH, "//*[@class='JGButton' and contains(text(),'新增')]")  # 新增按钮
    trApply_handover = (By.XPATH, "//*[@id='isc_1SHtable']/tbody/tr/td[2]/div")  #交接事项名称
    trApply_sp_content = (By.XPATH, "//*[@id='isc_1SHtable']/tbody/tr/td[3]/div")  #具体交接内容




    def enter_re_button(self):
        '''定位调动申请按钮'''
        try:
            self.find_element(*self.trApply_button).click()
        except Exception as e:
            print('调动申请按钮未找到，原因%s'%e)

    def enter_re_depart(self):
        '''点击调入部门'''
        try:
            self.find_element(*self.trApply_imp_button).click()
        except Exception as e:
            print('选择调入部门按钮未找到，原因%s'%e)

    def choose_re_depart(self):
        '''选择调入部门'''
        try:
            self.find_element(*self.trApply_choose_department).click()
            self.find_element(*self.trApply_imp_comfirm).click()
        except Exception as e:
            print('选择调入部门按钮未找到，原因%s'%e)

    def enter_re_position(self):
        '''输入调入职位'''
        try:
            self.find_element(*self.trApply_imp_button1).click()
            self.find_element(*self.trApply_imp_position).click()
            self.find_element(*self.trApply_imp_comfirm2).click()
        except Exception as e:
            print('调入职位按钮未找到，原因%s' % e)

    def enter_re_reason(self):
        "输入调动原因"
        return self.find_element(*self.trApply_reason).send_keys(u'测试调动申请')

    def select_re_handover(self):
        '''输入交接事项名称'''
        '''输入具体交接内容'''
        try:
            self.find_element(*self.trApply_add).click() #双击事件
            self.find_element(*self.trApply_add).click()
            self.find_element(*self.trApply_handover).click()
            self.find_element(*self.trApply_handover).click()
        except Exception as e:
            print('输入交接事项名称未找到，原因%s' % e)

        try:
            self.find_element(*self.trApply_sp_content).click()
            self.find_element(*self.trApply_sp_content).click()
        except Exception as e:
            print('具体交接内容未找到，原因%s' % e)


if __name__ == '__main__':
    URL = Config().get('URL1')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
    page.userlogin()
    result = reApplyLocators(page)
    result.enter_re_button()
    sleep(1)
    result.enter_re_depart()
    sleep(1)
    result.enter_re_position()
    sleep(1)
    result.enter_re_reason()






