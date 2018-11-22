import unittest
from time import sleep
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from test.page.pro1_rz_pages.rz_quitApply_page import QuitApplyLocators
from utils.config import Config


class RZCase(unittest.TestCase):
    URL = Config().get('URL')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = RZLoginPage().get(self.URL, maximize_window=False,implicitly_wait=20)

    def sub_tearDown(self):
        self.page.quit()

    def test_02_oa_application(self):
        '''离职申请单元测试'''
        self.sub_setUp()
        self.page = RZLoginPage(self.page)
        self.page.userlogin()
        qtapplication = QuitApplyLocators(self.page)
        qtapplication.enter_quitApply_button()
        sleep(2)
        qtapplication.quitApply_Email()
        sleep(1)
        qtapplication.quitApply_Reason()
        qtapplication.quitApply_Describe()
        sleep(2)
        qtapplication.quitApply_Outstanding()
        sleep(2)
        qtapplication.quitApply_FuturePlanning()
        sleep(2)
        qtapplication.quitApply_OtherSuggestions()
        sleep(2)
        qtapplication.quitApply_AddOperation()
        sleep(2)
        qtapplication.quitApply_Deliver()
        sleep(2)
        qtapplication.quitApply_Deliver_content()
        sleep(2)
        qtapplication.quitApply_Submit()
        self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()