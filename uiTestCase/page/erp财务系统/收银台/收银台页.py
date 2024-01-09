# -*- coding:utf-8 -*
# @FileName:   收银台页.py
# @Author:     刘峰
# @CreateTime: 2022/8/9 13:53

from base.base_page import BasePage


class CashierDeskPage(BasePage):

    url = BasePage.SERVER + "#/erp/settlement/cashierList"

    # 展开搜索框
    unflod_button = ("xpath", "//button/span/i[@class='el-icon-arrow-down']")
    # 订单号输入框
    order_number_input = ("xpath", "//label[text()='订单号']/../div/div/input")
    # 查询按钮
    search_button = ("xpath", "//button/span[text()='查询']")
    # 全选框
    check_all = ("xpath", "//span[@title='全选/取消']/span[2]")
    # 收款按钮
    gathering_button = ("xpath", "//button/span[text()='收款']")

    """
        收款窗口
    """
    # 第一个收款方式下拉框
    gathering_type = ("xpath", "//table[@class='vxe-table--body']/tbody/tr/td[2]/div/div/div/input")
    # 第一个收款金额输入框
    gathering_money = ("xpath", "//table[@class='vxe-table--body']/tbody/tr/td[4]/div/div/input")
    # 欠款金额合计的金额
    debt_money = ("xpath", "//b[@class='orderReceiveSum']")
    # 收款按钮
    gathering_but = ("xpath", "//div[@class='without-btn-dialog']/div/button/span[text()='收款']")
    # 提示框中的确定按钮
    confirm_button = ("xpath", "//div[@class='el-message-box__btns']/button[2]")

    # 提示所有订单收款成功
    all_order_success = ("xpath", "//p[@class='el-message__content']")

    # 收款
    def gathering(self, ordernumber, gatheringtype):
        self.open(self.url)
        self.wait(5)
        # 查询
        self.click(self.unflod_button)
        self.input(self.order_number_input, ordernumber)
        self.click(self.search_button)
        self.wait(2)

        self.click(self.check_all)
        self.click(self.gathering_button)
        self.wait(3)

        self.select(self.gathering_type, gatheringtype)
        self.input(self.gathering_money, self.getText(self.debt_money), True)
        self.click(self.gathering_but)
        self.click(self.confirm_button)
        self.wait(3)

