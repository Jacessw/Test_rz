import unittest

from test.page.pro1_rz_pages.rz_login_page import RZLoginPage
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger


class TestRenZi(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = RZLoginPage(browser_type='Chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.userlogin(d['username'],d['password'])
                try:
                    self.page = RZLoginPage(self.page) # 页面跳转到result page
                    loginname = self.page.result_name()
                    target_value = d['target_value']
                    self.assertIn(target_value, loginname)
                    logger.info(loginname)
                except AssertionError as e:
                    logger.warning(e)
                self.sub_tearDown()

if __name__ == '__main__':
    #unittest.main()
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='同望人资系统', description='test')
        runner.run(TestRenZi('test_login'))