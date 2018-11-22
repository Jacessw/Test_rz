import unittest
from time import sleep
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from test.page.pro1_rz_pages.rz_reApply_page import reApplyLocators
from utils.config import Config


class RZCase(unittest.TestCase):
    URL = Config().get('URL')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = RZLoginPage().get(self.URL, maximize_window=False,implicitly_wait=20)

    def sub_tearDown(self):
        self.page.quit()

    def test_02_oa_application(self):
        '''调出申请单元测试'''
        self.sub_setUp()
        self.page = RZLoginPage(self.page)
        self.page.userlogin()
        reapplication = reApplyLocators(self.page)
        reapplication.enter_reApply_button()
        sleep(2)
        reapplication.enter_reApply_button()
        sleep(2)
        reapplication.reApply_click_depart()
        sleep(2)
        reapplication.reApplydepart()
        sleep(4)
        reapplication.reApplyposition()
        sleep(2)
        reapplication.reApplyreason()
        sleep(2)
        reapplication.reApply_add()
        sleep(2)
        reapplication.reApply_Deliver()
        sleep(2)
        reapplication.reApply_Deliver_content()
        sleep(2)
        reapplication.reApply_Submit()
        self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()