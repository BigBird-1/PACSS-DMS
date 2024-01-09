# -*- coding:utf-8 -*
# @FileName:   业务审批页.py
# @Author:     刘峰
# @CreateTime: 2022/8/20 14:30

from base.base_page import BasePage

class AuditBillPage(BasePage):

    审核通过按钮 = "//button/span[text()='审核通过']"
    终结按钮 = "//button/span[contains(text(), '终')]"

    """
        单据审核-通过/终结窗口
    """
    单据审核确定按钮 = "//div/button/span[text()='确定']"

    # 审批通过/终结（没有字段需要填写），前置条件：跳转到审批页面
    def approvalPass(self, isEnd=False):
        if isEnd:
            self.click(self.终结按钮, 1)
        else:
            self.click(self.审核通过按钮, 1)
        self.click(self.单据审核确定按钮, 2)
