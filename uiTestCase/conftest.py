# -*- coding:utf-8 -*
# @FileName:   conftest.py
# @Author:     刘峰
# @CreateTime: 2022/7/22 16:06

"""
    前置登录操作，每次执行一个py文件都会自动执行一次
"""
import json
import pytest, allure
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains

from base.base_page import BasePage
from page.登录页面 import LoginPage


# @pytest.fixture(scope="module", autouse=False)
def login():

    # with allure.step("前置操作：登录；"):
    try:
        ca = DesiredCapabilities.CHROME
        ca["goog:loggingPrefs"] = {"performance": "ALL"}

        option = webdriver.ChromeOptions()
        option.page_load_strategy = 'none'
        # 去掉账号密码弹窗
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs['profile.password_manager_enable'] = False
        option.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(desired_capabilities=ca, options=option)

        lg = LoginPage(driver)
        lg.login("HD340400", "MBDJ", "165531")

        # 获取返回值中x值
        logs = driver.get_log("performance")
        for i in range(len(logs)):
            message = json.loads(logs[i]['message'])
            message = message['message']['params']
            request = message.get('request')
            if request is None:
                continue

            url = request.get('url')
            if (BasePage.SERVER + "apigateway/admin/user/createImgValidate") in url:
                print(message['requestId'])
                content = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message['requestId']})
                print(content)
                xx = json.loads(content['body'])['data']['x']
                break

        # 根据x值进行滑动
        aa = lg.locate(("xpath", "//i[@class='el-icon-d-arrow-right']"))
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(aa).perform()
        action_chains.drag_and_drop_by_offset(aa, xx, 0).perform()
        action_chains.release().perform()
        lg.wait(3)
    except Exception as e:
        print(e)
        driver.quit()

    # yield driver
    # driver.quit()

login()