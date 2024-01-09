# -*- coding:utf-8 -*
# @FileName:   登录页面.py
# @Author:     刘峰
# @CreateTime: 2022/7/19 10:17

"""
    登录页
"""
from base.base_page import BasePage


class LoginPage(BasePage):
    # 登录页URL
    url = BasePage.SERVER + "#/sso/login"

    # 提示语：恒信办公APP，扫码登录
    scan_login_text = ("xpath", "//h4[text()='恒信办公APP，扫码登录']")
    # 元素：切换登录
    switch_login = ("xpath", "//span[text()='切换登录']")
    # 元素：公司代码输入框
    company_code_input = ("xpath", "//input[@placeholder='请输入公司代码']")
    # 元素：用户名输入框
    username_input = ("xpath", "//input[@placeholder='请输入用户名/手机号']")
    # 元素：密码输入框
    password_input = ("xpath", "//input[@placeholder='请输入密码']")
    # 元素：登录按钮
    login_button = ("xpath", "//span[contains(text(), '线版本】')]")

    # 登录操作
    def login(self, companycode, username, password):
        self.open(self.url)
        # try:
        #     if '扫码登录' in self.getText(self.scan_login_text):
        #         self.click(self.switch_login)
        # except:
        #     pass
        self.input(self.company_code_input, companycode)
        self.input(self.username_input, username)
        self.input(self.password_input, password)
        self.click(self.login_button)
        self.wait(1)
