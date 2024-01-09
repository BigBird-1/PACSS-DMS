# -*- coding:utf-8 -*
# @FileName:   配件维修领料页.py
# @Author:     刘峰
# @CreateTime: 2022/7/25 15:21

from base.base_page import BasePage


class RepairOutPage(BasePage):

    # 配件维修领料页url
    url = BasePage.SERVER + "#/erp/parts/repairOut/repairOutOrderList"

    # 工单号输入框
    order_number_input = ("xpath", "//label[text()='工单号']/../div/div/input")
    # 查询
    search_button = ("xpath", "//div[@class='search-form-btn']/button[3]")
    # 根据工单号查询出的唯一一条数据的编辑按钮
    edit_button = ("xpath", "//span[text()='编辑 ']")

    # 跳转到编辑维修领料
    def skipToMaintainPick(self, order_number):
        self.open(self.url)
        self.wait(3)
        self.input(self.order_number_input, order_number)
        self.click(self.search_button)
        self.wait(1)
        self.click(self.edit_button)
        self.wait(3)

