import time
import re
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


def to_three(str1, str2, str3):
    driver.find_element_by_xpath("//div[@class='main-menu']/div[contains(text(), '{}')]".format(str1)).click()
    time.sleep(2)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//ul[@id='fir_ul']//p[contains(text(), '{}')]".format(str2))).perform()
    time.sleep(1)
    driver.find_elements_by_xpath("//ul[@id='fir_ul']//p[contains(text(), '{}')]".format(str3))[0].click()
    time.sleep(2)


to_three('销售管理', '库存管理', '在途车辆管理')
driver.find_element_by_xpath("//span[text()='新增']").click()
time.sleep(3)
# ---------------------------------------------------------------------------------------------------------------


def input_select(str1, str2):
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).send_keys(str2)
    driver.find_element_by_xpath("//span[contains(text(), '{}')]".format(str2)).click()


def input_box(str1, str2):
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).click()
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).clear()
    driver.find_element_by_xpath("//label[text()='{}']/following-sibling::div[1]/div/div/input".format(str1)).send_keys(str2)
# --------------------------------------------------------------------------------------------------------------


driver.find_element_by_xpath("//label[text()='业务类型']/following-sibling::div[1]/div").click()
time.sleep(0.5)
driver.find_element_by_xpath("//span[text()='厂家采购入库']").click()  # 选择业务类型
# input_select('业务类型', '厂家采购入库')
# --------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//label[text()='供应商']/following-sibling::div[1]/div/span").click()
time.sleep(3)
ActionChains(driver).double_click(driver.find_element_by_xpath("//div[text()='888888888888']")).perform()  # 选择供应商
time.sleep(2)
# ----------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//label[text()='产品代码']/following-sibling::div[1]/div/span").click()
time.sleep(3)
driver.find_element_by_xpath("//label[text()='品牌']/following-sibling::div[1]/div").click()
time.sleep(0.5)
driver.find_element_by_xpath("//span[text()='凯迪拉克']").click()
driver.find_element_by_xpath("//span[text()='查询']").click()
time.sleep(3)
ActionChains(driver).double_click(driver.find_element_by_xpath("//div[text()='FPZ-000006 FWS-000003 FNS-000003']")).perform()
time.sleep(3)
# -------------------------------------------------------------------------------------------------------------------
input_select('排放标准', '国六')  # 选择排放标准
input_select('运输方式', '公路')  # 选择运输方式
input_select('资金来源', '银行融资')  # 选择资金来源
input_select('车辆类型', '国产车')  # 选择车辆类型
input_select('发运地', '上海')  # 选择发运地
driver.find_element_by_xpath("//label[text()='厂家实际提车日期 ']/following-sibling::div[1]/div/input").click()
driver.find_element_by_xpath("//label[text()='厂家实际提车日期 ']/following-sibling::div[1]/div/input").send_keys(current_date)
# -------------------------------------------------------------------------------------------------------------------
input_box('采购价格', '616524.00')
input_box('标准提车佣金', '31112.00')
# -------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//span[text()='增加行']").click()
time.sleep(0.5)
driver.find_element_by_xpath(
    "//div[@class='vxe-table--body-wrapper body--wrapper']/table/tbody/tr[1]/td[3]/div/div/input").send_keys(vin)
driver.find_element_by_xpath(
    "//div[@class='vxe-table--body-wrapper body--wrapper']/table/tbody/tr[1]/td[3]/div/div/input").send_keys(Keys.TAB)
time.sleep(5)
driver.find_element_by_xpath("//span[text()='保存']").click()
time.sleep(5)
# --------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//div[@class='bread_nav']/ul//span[contains(text(), '在途车辆管理')]").click()
input_select('VIN', vin)
driver.find_element_by_xpath("//span[text()='查询']").click()
time.sleep(3)
# -------------------------------------------------------------------------------------------------------------------
driver.find_element_by_xpath("//div[contains(text(), '{}')]".format(vin)).click()
driver.find_element_by_xpath("//span[contains(text(), '批量转入库单')]").click()
time.sleep(3)
driver.find_element_by_xpath("//span[contains(text(), '保存')]").click()
time.sleep(1.5)
# --------------------------------------------------------------------------------------------------------------------
# alert_x = (By.XPATH, "//p[contains(text(), '转入库单成功')]")
# if WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(alert_x)):
text1 = driver.find_element_by_xpath("//p[contains(text(), '转入库单成功')]").text
print(text1)
num = text1[:12]
print(type(num), num)
time.sleep(2)
# # --------------------------------------------------------------------------------------------------------------------
to_three('销售管理', '库存管理', '车辆入库')
driver.find_element_by_xpath("//label[text()='入库单号']/following-sibling::div[1]/div/input").click()
driver.find_element_by_xpath("//label[text()='入库单号']/following-sibling::div[1]/div/input").send_keys(str(num))
driver.find_element_by_xpath("//label[text()='入库单号']/following-sibling::div[1]/div/span").click()
time.sleep(2)
# ----------------------------------------------------------------------------------------------------------------------
ActionChains(driver).double_click(driver.find_element_by_xpath("//div[contains(text(), '{}')]".format(num))).perform()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(text(), '{}')]".format(vin)).click()
driver.find_element_by_xpath("//span[contains(text(), '批量验收')]").click()
time.sleep(1)
input_select('验收结果', '验收已通过')
input_select('质损状态', '正常')
driver.find_element_by_xpath("//span[text()='确认']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(text(), '{}')]".format(vin)).click()
driver.find_element_by_xpath("//span[text()='提交审核']").click()
time.sleep(2)
# ----------------------------------------------------------------------------------------------------------------------
to_three('行政管理', '个人办公', '代办事项')
















