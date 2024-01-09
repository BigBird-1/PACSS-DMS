# -*- coding:utf-8 -*
# @FileName:   费用结算页.py
# @Author:     刘峰
# @CreateTime: 2022/7/26 15:20

from base.base_page import BasePage


class SettlementPage(BasePage):

    # URL
    url = BasePage.SERVER + "#/erp/settlement/settlement"

    # 工单号输入框
    order_number = ("xpath", "//label[text()='工单号']/../div/div/input")
    # 查询按钮
    search_button = ("xpath", "//button/span[text()='查询']")
    # 查询出一条数据的编辑按钮
    edit_button = ("xpath", "//span[text()=' 编辑 ']")

    # 跳转到结算页
    def skipToSettlement(self, ordernumber):
        self.open(self.url)
        self.wait(1)
        self.input(self.order_number, ordernumber)
        self.click(self.search_button)
        self.wait(1)
        self.click(self.edit_button)
        self.wait(3)