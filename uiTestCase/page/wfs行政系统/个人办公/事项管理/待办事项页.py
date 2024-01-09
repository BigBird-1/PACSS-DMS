# -*- coding:utf-8 -*
# @FileName:   待办事项页.py
# @Author:     刘峰
# @CreateTime: 2022/8/20 14:06

from base.base_page import BasePage

class TodoListPage(BasePage):

    url = BasePage.SERVER + "#/wfs/office/todoList"

    单据编号 = "//label[text()='单据编号']/../div/div/input"
    查询按钮 = "//button/span[text()='查询']"
    第一行办理按钮 = "//tbody/tr[1]/td[2]/div/button/span[text()='办理']"

    # 查询待办事项
    def searchTodo(self, receipt_number):
        self.open(self.url, 5)
        self.input(self.单据编号, receipt_number, 0.5)
        self.click(self.查询按钮, 3)

    # 跳转到审批页面
    def skipToApproval(self, receipt_number):
        self.searchTodo(receipt_number)
        self.click(self.第一行办理按钮, 2)
