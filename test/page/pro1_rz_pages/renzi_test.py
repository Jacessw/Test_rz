
import time
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from selenium import webdriver
from selenium.webdriver.common.by import By

excel = DATA_PATH + '/renzi.xlsx'
datas = ExcelReader(excel).data
for d in datas:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('http://10.1.27.52:9011/')
    driver.find_element(By.XPATH,"//input[@widgetcode='JGTextBox1']").send_keys(d['username'])
    driver.find_element(By.XPATH,"//input[@widgetcode='JGPasswordBox1']").send_keys(d['password'])
    driver.find_element(By.XPATH,"//*[@widgetcode='JGButton1']").click()
    time.sleep(1)
    # fail_text = driver.find_element(By.ID, "dialog_content_div").text
    # print("----->%s" % fail_text)
    # if fail_text:
    #     print("fail_text %s" % fail_text)
    #
    # else:
    #     sucess_text = driver.find_element(By.XPATH, "//span[contains(text(),'登录时间')] ").text
    #     print('sucess_text %s' % sucess_text)
    # driver.quit()


    driver.find_element(By.XPATH,"//*[@name='startDate'and @class='JGFormIconTextError']").send_keys('20170821')
