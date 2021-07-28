import time
import re

import win32api
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from uiSelenium.login import LoginCs
from dataGenerated.randomData import random_vin


current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
current_date2 = time.strftime('%Y%m%d', time.localtime(time.time()))
vin = random_vin()
driver = LoginCs().login1()
# driver.implicitly_wait(10)
time.sleep(10)


def input_select(str1, str2):
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).send_keys(str2)
    driver.find_element_by_xpath("//span[contains(text(), '{}')]".format(str2)).click()


def input_box(str1, str2):
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).click()
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).clear()
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).send_keys(str2)


def input_box2(str1, str2):
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/input".format(str1)).click()
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/input".format(str1)).clear()
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/input".format(str1)).send_keys(str2)


def to_three(str1, str2, str3):
    driver.find_element_by_xpath("//div[@class='main-menu']/div[contains(text(), '{}')]".format(str1)).click()
    time.sleep(2)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//ul[@id='fir_ul']//p[contains(text(), '{}')]".format(str2))).perform()
    time.sleep(1)
    driver.find_elements_by_xpath("//ul[@id='fir_ul']//p[contains(text(), '{}')]".format(str3))[0].click()
    time.sleep(5)


to_three('销售管理', '订单管理', '预订单')
driver.find_element_by_xpath("//span[text()='新增']").click()
time.sleep(3)
# ----------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//span[text()='选择客户']").click()
time.sleep(15)
driver.find_element_by_xpath("//label[text()='关键字']/following-sibling::div[1]/div/input").click()
driver.find_element_by_xpath("//label[text()='关键字']/following-sibling::div[1]/div/input").send_keys("13632708208")
driver.find_element_by_xpath("//span[text()='查询']").click()
time.sleep(3)
ActionChains(driver).double_click(driver.find_element_by_xpath("//div[text()='136****8208']")).perform()
time.sleep(2)
if driver.find_element_by_xpath("//p[contains(text(), '该客户已存在未提交的预订单')]"):
    driver.find_element_by_xpath("//div[@class='el-message-box__btns']//span[contains(text(), '确定')]").click()
    time.sleep(2)
# ----------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//span[text()='选择车型']").click()
time.sleep(3)
driver.find_element_by_xpath("//label[text()='品牌']/following-sibling::div[1]/div").click()
time.sleep(0.5)
driver.find_element_by_xpath("//span[text()='凯迪拉克']").click()
driver.find_elements_by_xpath("//span[text()='查询']")[-1].click()
time.sleep(3)
ActionChains(driver).double_click(driver.find_element_by_xpath("//div[text()='FPZ-000006 FWS-000003 FNS-000003']")).perform()
time.sleep(3)
# ----------------------------------------------------------------------------------------------------------------------
input_select('结算方式', '一次付清')
input_box('车价', '678514.00')
input_box('订金', '118514.00')
if driver.find_element_by_xpath("//label[text()='预定交车日期']"):
    driver.find_element_by_xpath("//label[text()='预定交车日期']/following-sibling::div[1]/div/input").click()
    driver.find_element_by_xpath("//label[text()='预定交车日期']/following-sibling::div[1]/div/input").send_keys(
        current_date)
# ----------------------------------------------------------------------------------------------------------------------
win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -800)  # 滚动下滑
# ----------------------------------------------------------------------------------------------------------------------
input_box2('销售装潢项目', '安装车翅膀')
input_box('销售装潢金额', '12580.00')
# ----------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//label[text()='合同说明备注']/following-sibling::div[1]/div").click()
driver.find_element_by_xpath("//span[text()='关于个人信息保护，参见附件一']").click()
# ----------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//span[text()='保存']").click()
time.sleep(6)
order_no = driver.find_element_by_xpath("//legend[contains(text(), '开单人')]").text[-12:]
# ----------------------------------------------------------------------------------------------------------------------
# driver.find_elements_by_xpath("//div[@class='bread_nav']/ul//span[contains(text(), '预订单')]")[0].click()
# time.sleep(1)
# input_box2('关键字', order_no)
# driver.find_element_by_xpath("//span[text()='查询']").click()
# time.sleep(1)
# ----------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//span[text()='提交审核']").click()
time.sleep(5)
# ----------------------------------------------------------------------------------------------------------------------
to_three('行政管理', '个人办公', '代办事项')
input_box2('单据编号', order_no)
driver.find_element_by_xpath("//span[text()='查询']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[text()='办理']").click()
time.sleep(1)
# ----------------------------------------------------------------------------------------------------------------------
win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -800)  # 滚动下滑
# ----------------------------------------------------------------------------------------------------------------------
if driver.find_element_by_xpath("//span[contains(text(), '终   结')]"):
    driver.find_element_by_xpath("//span[contains(text(), '终   结')]").click()
else:
    for i in range(1000):
        driver.find_element_by_xpath("//span[text()='审核通过']").click()
        input_box2('单据编号', order_no)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='办理']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='审核通过']").click()
        driver.find_element_by_xpath("//div[@class='bread_nav']/ul//span[contains(text(), '代办事项')]").click()







