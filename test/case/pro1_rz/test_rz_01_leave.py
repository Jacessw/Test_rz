import unittest
from time import sleep

from test.page.pro1_rz_pages.rz_leave_page import LeaveAppLocators
from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.config import Config


class RZCase(unittest.TestCase):
    """
    人资系统单元测试
    """
    URL = Config().get('URL')

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = RZLoginPage().get(self.URL, maximize_window=False,implicitly_wait=20)

    def sub_tearDown(self):
        self.page.quit()

    #@unittest.skip('测试跳过')
    def test_01_leave_application(self):
        '''请假申请单元测试'''
        self.sub_setUp()
        self.page = RZLoginPage(self.page)
        self.page.userlogin()
        sleep(1)
        loginname = self.page.result_name()
        if "欢迎您" in loginname:
            leaveappliction = LeaveAppLocators(self.page)
            sleep(2)
            leaveappliction.enter_leave_butten()
            sleep(4)
            leaveappliction.enter_leave_type()
            sleep(2)
            leaveappliction.enter_leave_reason()
            sleep(2)
            leaveappliction.enter_date_time()
            ele = leaveappliction.sucess_content
            print(ele)
            self.assertIn('提交成功', ele)
            self.sub_tearDown()
        else:
            self.assertIn('提交成功',loginname)

if __name__ == '__main__':
    unittest.main()