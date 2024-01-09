# -*- coding:utf-8 -*
# @FileName:   录用申请页.py
# @Author:     刘峰
# @CreateTime: 2022/8/19 11:34

from base.base_page import BasePage

class EmployApplyPage(BasePage):

    url = BasePage.SERVER + "#/ehr/recruitment/employManage/employApply"

    应聘人姓名 = "//label[text()='应聘人姓名']/../div/div/input"
    查询按钮 = "//button/span[text()='查询']"

    增加按钮 = "//button/span[text()='增加']"
    提交按钮 = "//div[@class='vxe-button--wrapper']/button/span[text()='提交']"
    提示核对应聘信息的确定按钮 = "//div[@class='el-message-box__btns']/button[2]/span"

    第一行的单据编号 = "//tbody/tr/td[2]/div/span[@class='vxe-cell--label']"
    第一行审批状态 = "//tbody/tr/td[7]/div/span[@class='vxe-cell--label']"

    # 跳转到录用申请-新增页
    def skipToEmployApplyAdd(self):
        self.open(self.url, 2)
        self.click(self.增加按钮, 1)

    # 查询录用申请单
    def searchEmployApply(self, name, isclear=False):
        self.open(self.url, 2)
        self.input(self.应聘人姓名, name, isclear, wait=0.5)
        self.click(self.查询按钮, 1)

    # 提交录用申请单
    def commitEmployApply(self, name):
        self.searchEmployApply(name)
        number = self.getText(self.第一行的单据编号)
        self.click(self.第一行的单据编号, 0.5)
        self.click(self.提交按钮)
        self.click(self.提示核对应聘信息的确定按钮, 2)
        return number
