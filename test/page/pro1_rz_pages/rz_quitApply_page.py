from time import sleep
from selenium.webdriver.common.by import By
from test.common.page import Page
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config


class QuitApplyLocators(Page):
    """
    人资系统：离职申请界面使用的控件定位内容
    """
    quitApply_button = (By.XPATH,"//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage4')]") #离职申请按钮
    quitEmail = (By.XPATH,"//input[@type='TEXT' and @name='personalEmail']") #个人邮箱
    quitReasons_checkBox = (By.XPATH,"//input[starts-with(@value,'找到更好的工作机会')]") #离职原因复选框
    quitDescribe = (By.XPATH,"//textarea[starts-with(@name,'leaveReasonDes')]") #说明框
    quitOutstanding = (By.XPATH,"//textarea[starts-with(@name,'outstanding')]") #任职业绩
    quitFuturePlanning = (By.XPATH, "//textarea[starts-with(@name,'futurePlanning')]") #今后的职业规划
    quitOtherSuggestions = (By.XPATH, "//textarea[starts-with(@name,'otherSuggestions')]") #其他建议
    quitAdd_button = (By.XPATH,"//*[contains(text(),'新增')]") #新增按钮
    quitDeliver = (By.XPATH,"//table[@class='listTable' and @width='778']/tbody/tr/td[2]") #交接事项外部框
    quitDeliver_1 = (By.XPATH,"//input[@type='TEXT'and @name='contentName']") #交接事项内嵌框
    quitDeliver_content = (By.XPATH,"//table[@class='listTable' and @width='778']/tbody/tr/td[3]") #具体交接内容外部框  #//input[starts-with(@id,'vp_hr_portal_myApply_web_JGImage6')] 查找id属性中开始位置包含'vp_hr_portal_myApply_web_JGImage6'关键字的页面元素
    quitDeliver_content_1 = (By.XPATH, "//input[@type='TEXT'and @name='content']")  #具体交接内容内嵌框
    quitSubmit_button = (By.XPATH, "//*[contains(text(),'保存并提交')]")  # 提交按钮


    def enter_quitApply_button(self):
        '''定位离职申请按钮'''
        try:
            self.find_element(*self.quitApply_button).click()
        except Exception as e:
            print('离职申请按钮未找到，原因%s'%e)

    def quitApply_Email(self):
        '''更改Email'''
        try:
            self.find_element(*self.quitEmail).clear()
            self.find_element(*self.quitEmail).send_keys("abc@qq.com")
        except Exception as e:
            print('无法定位个人邮箱 %s' %e)
    def quitApply_Reason(self):
        '''勾选离职原因'''
        try:
            self.find_element(*self.quitReasons_checkBox).click()
        except Exception as e:
            print("无法勾选复选框 %s" %e)
        '''   
        print(len(checkBox))
        for a in checkBox:
            a.click()
        '''

    def quitApply_Describe(self):
        '''填写离职说明'''
        try:
            self.find_element(*self.quitDescribe).send_keys(u'测试离职说明')
        except Exception as e:
            print("无法定位说明框 %s" %e)

    def quitApply_Outstanding(self):
        '''任职业绩文本框'''
        return self.find_element(*self.quitOutstanding).send_keys(u'测试业绩')

    def quitApply_FuturePlanning(self):
        '''今后的职业规划文本框'''
        return self.find_element(*self.quitFuturePlanning).send_keys(u'测试职业规划')

    def quitApply_OtherSuggestions(self):
        '''其他建议文本框'''
        return self.find_element(*self.quitOtherSuggestions).send_keys(u'测试其它建议')

    def quitApply_AddOperation(self):
        '''新增操作'''
        try:
            self.find_element(*self.quitAdd_button).click()
        except Exception as e:
            print("无法定位新增按钮 %s" %e)

    def quitApply_Deliver(self):
        '''交接事项名称'''
        try:
            self.find_element(*self.quitDeliver).click()
            self.find_element(*self.quitDeliver).click()
            self.find_element(*self.quitDeliver_1).send_keys(u'测试交接事项')
        except Exception as e:
            print('无法定位交接事项 %s' %e)

    def quitApply_Deliver_content(self):
        '''具体交接内容'''
        try:
            self.find_element(*self.quitDeliver_content).click()
            self.find_element(*self.quitDeliver_content).click()
            self.find_element(*self.quitDeliver_content_1).send_keys(u'测试具体交接内容')
        except Exception as e:
            print('无法定位具体交接内容 %s' %e)

    def quitApply_Submit(self):
        '''保存&提交按钮'''
        try:
            self.find_element(*self.quitSubmit_button).click()
        except Exception as e:
            print('无法定位提交按钮 %s' %e)

if __name__ == '__main__':
    URL = Config().get('URL1')
    page = RZLoginPage(browser_type='Chrome').get(URL, maximize_window=False)
    page.userlogin()
    result = QuitApplyLocators(page)
    result.enter_quitApply_button()
    sleep(3)
    result.quitApply_Email()
    sleep(2)
    result.quitApply_Reason()
    sleep(1)
    result.quitApply_Describe()
    sleep(1)
    result.quitApply_Outstanding()
    sleep(1)
    result.quitApply_FuturePlanning()
    sleep(1)
    result.quitApply_OtherSuggestions()
    sleep(1)
    result.quitApply_AddOperation()
    sleep(3)
    result.quitApply_Deliver()
    sleep(2)
    result.quitApply_Deliver_content()
    sleep(2)
    result.quitApply_Submit()


