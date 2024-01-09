# -*- coding:utf-8 -*
# @FileName:   接车制单页.py
# @Author:     刘峰
# @CreateTime: 2022/7/23 15:07

"""
    接车制单页
"""
from base.base_page import BasePage


class CustomerReceptionPage(BasePage):

    # URL
    url = BasePage.SERVER + "#/erp/repair/customerReception"

    # 新增按钮
    add_button = ("xpath", "//span[text()='新增']")
    # 车牌号输入框
    license_number_input = ("xpath", "//label[text()='车牌号']/../div/div/input")
    # 工单号输入框
    order_number_input = ("xpath", "//label[text()='工单号']/../div/div/input")
    # 工单状态下拉框
    order_state_input = ("xpath", "//label[text()='工单状态']/../div/div/div/input")
    # 查询按钮
    search_button = ("xpath", "//div[@class='search-form-btn']/button[3]")
    # 查询结果的第一条数据的工单号
    order_number_text = ("xpath", "//*[@id='app']/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div")
    # 查询唯一结果的编辑按钮
    edit_button = ("xpath", "//span[text()='编辑']")
    # 查询出唯一数据中的提交结算按钮
    commit_account = ("xpath", "//span[text()='提交结算']")
    # 查询出唯一结果的取消提交结算按钮
    cancle_account = ("xpath", "//span[text()='取消提交结算']")

    # 消息提示框中的确定按钮
    confirm_button = ("xpath", "//div[@class='el-message-box__btns']/button[2]")

    # 工单提交结算成功提示语
    order_commit_success = ("xpath", "//p[@class='el-message__content']")

    # 工单取消提交结算成功提示语：修改成功
    cancle_commit_success = ("xpath", "//p[@class='el-message__content']")

    # 跳转到新增接车制单页面
    def skipToAdd(self):
        self.open(self.url)
        self.wait(5)
        self.click(self.add_button)
        self.wait(2)

    # 获取工单号
    def getOrderNumber(self):
        self.open(self.url)
        self.wait(2)
        self.click(self.search_button)
        return self.getText(self.order_number_text)

    # 条件查询
    def searchByCondition(self, ordernumber, orderstate=''):
        self.open(self.url)
        self.wait(5)
        self.input(self.order_number_input, ordernumber, True)
        if orderstate != '':
            self.select(self.order_state_input, orderstate)
        self.click(self.search_button)

    # 查询后，提交结算
    def commitAccount(self, ordernumber):
        self.searchByCondition(ordernumber)
        self.click(self.commit_account)
        self.click(self.confirm_button)
        self.wait(3)

    # 查询后，取消结算
    def cancleCommitAccount(self, ordernumber, orderstate):
        self.searchByCondition(ordernumber, orderstate)
        self.click(self.cancle_account)
        self.click(self.confirm_button)
        self.wait(2)

    # 查询后，点击进入编辑接车制单界面
    def skipToEdit(self, ordernumber):
        self.searchByCondition(ordernumber)
        self.click(self.edit_button)
        self.wait(3)

