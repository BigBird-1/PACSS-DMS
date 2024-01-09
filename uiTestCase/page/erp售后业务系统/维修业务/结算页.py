# -*- coding:utf-8 -*
# @FileName:   结算页.py
# @Author:     刘峰
# @CreateTime: 2022/7/26 15:26

from base.base_page import BasePage


class BalancePage(BasePage):

    # 结算按钮
    balance_button = ("xpath", "//*[@id='settlement-container']/div[1]/button[1]/span")

    # 使用优惠券按钮
    use_discount_coupon = ("xpath", "//span[text()='使用优惠券']")

    # 维修建议输入框
    maintain_suggest = ("xpath", "//label[@for='repairAdvice']/../div/div/textarea")

    # 结算成功提示语
    pay_success = ("xpath", "//p[@class='el-message__content']")


    """
        优惠券窗口
    """
    # 小保养
    little_maintain = ("xpath", "//li[contains(text(), '小保养')]")
    # 序号为1的套餐
    number_one = ("xpath", "//div[text()='A保']")
    # 序号1的材料
    material_one = ("xpath", "//*[text()='匹配材料列表']/../../div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div[text()='.641010R500']")
    # 确定按钮
    confirm_button = ("xpath", "//div[@aria-label='优惠券']/div[2]/div/div/button[2]")
    # 返回按钮
    back_button = ("xpath", "//div[@aria-label='优惠券']/div[2]/div/div/button[1]")

    # 结算
    def payBalance(self, suggest, isusediscount=False):
        self.input(self.maintain_suggest, suggest, 0.5)

        if isusediscount:
            self.click(self.use_discount_coupon, 1)
            self.click(self.little_maintain)
            self.click(self.number_one)
            self.click(self.material_one)
            self.click(self.confirm_button)
            self.click(self.back_button)

        self.click(self.balance_button, 3)
