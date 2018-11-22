import unittest
from time import sleep
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from test.page.pro1_rz_pages.rz_outApply_page import OutApplyLocators
from utils.config import Config


class RZCase(unittest.TestCase):
    URL = Config().get('URL')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = RZLoginPage().get(self.URL, maximize_window=False,implicitly_wait=20)

    def sub_tearDown(self):
        self.page.quit()

    def test_02_oa_application(self):
        '''外出申请单元测试'''
        self.sub_setUp()
        self.page = RZLoginPage(self.page)
        self.page.userlogin()
        oaapplication = OutApplyLocators(self.page)
        oaapplication.enter_outApply_button()
        sleep(2)
        oaapplication.outApply_reason()
        oaapplication.enter_date_time()
        ele = oaapplication.success_content
        self.assertIn('提交成功', ele)
        self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()