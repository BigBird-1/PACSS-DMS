# -*- coding:utf-8 -*
# @FileName:   新收银台页.py
# @Author:     刘峰
# @CreateTime: 2022/7/26 15:51

from base.base_page import BasePage


class NewCashierDeskPage(BasePage):

    # URL
    url = BasePage.SERVER + "#/erp/settlement/cashierDesk"

    # 信息输入框
    info_input = ("xpath", "//input[@placeholder='请输入VIN后六位/车牌号/客户姓名']")
    # 查询按钮
    search_button = ("xpath", "//span[text()='查询']")

    # 收款按钮
    receipt_button = ("xpath", "//button/span[text()='收款']")
    # 全部勾选框
    all_check = ("xpath", "//*[@id='app']/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/table/thead/th[1]/label/span/span")
    # 现金收款输入框
    cash_receipt = ("xpath", "//div[text()='现金收款']/../div[2]/div/div/input")

    # 欠款金额数
    debt_money = ("xpath", "//span[text()='欠款金额']/../span[2]")

    # 提示框中的确定按钮
    confirm_button = ("xpath", "//div[@class='el-message-box__btns']/button[2]")

    """
        收款窗口
    """
    # 确定按钮
    confirm_button2 = ("xpath", "//span[text()='确认']")

    # 提示所有订单收款成功
    all_order_success = ("xpath", "//p[@class='el-message__content']")


    # 收银台收款
    def cashierDeskReceipt(self, info):
        self.open(self.url)
        self.wait(1)
        self.input(self.info_input, info)
        self.click(self.search_button)
        self.wait(8)

        self.click(self.all_check)
        self.wait(1)
        self.input(self.cash_receipt, self.getText(self.debt_money))
        self.click(self.receipt_button)
        self.click(self.confirm_button)
        self.wait(1)
        self.click(self.confirm_button2)
        self.wait(3)