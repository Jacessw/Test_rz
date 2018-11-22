import unittest
from utils.config import CASE_PATH,REPORT_PATH
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
import sys
sys.path.append('F:\\Python\\Test_frame-master\\utils') #指定当前目录

class RunTools:
    def chooseDirCases(self,casedir,pattern):
        '''
        根据指定目录获取匹配的测试用例
        :param casedir:测试用例目录路径
        :param pattern:匹配模式
        :return:测试用例集
        '''
        discover_cases = unittest.defaultTestLoader.discover(casedir,pattern=pattern)
        return discover_cases

if __name__ == '__main__':
    casepath = CASE_PATH
    report = REPORT_PATH + '\\report.html'
    runtools = RunTools()
    all_cases = runtools.chooseDirCases(casepath,'test_rz_06_quitApply.py')
    print(all_cases)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='同望人资系统', description='所有测试情况')
        runner.run(all_cases)
    e = Email(title='测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='313948303@qq.com',
              server='smtp.qq.com',
              sender='313948303@qq.com',
              password='wlunpmmlmhcsbghe',
              path=report
              )
    e.send()