import unittest
from time import sleep

from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from test.page.pro1_rz_pages.rz_travel_page import TravelAppLocators
from utils.config import Config


class RZCase(unittest.TestCase):
    URL = Config().get('URL')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = RZLoginPage().get(self.URL, maximize_window=False,implicitly_wait=20)

    def sub_tearDown(self):
        self.page.quit()

    def test_03_travel_application(self):
        '''出差申请单元测试'''
        self.sub_setUp()
        self.page = RZLoginPage(self.page)
        self.page.userlogin()
        travelapplication = TravelAppLocators(self.page)
        travelapplication.enter_travel_butten()
        sleep(2)
        travelapplication.enter_travel_place()
        travelapplication.enter_travel_reason()
        travelapplication.enter_date_time()
        ele = travelapplication.sucess_content
        self.assertIn('提交成功', ele)
        self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()