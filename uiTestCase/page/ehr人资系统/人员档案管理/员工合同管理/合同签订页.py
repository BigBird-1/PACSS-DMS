# -*- coding:utf-8 -*
# @FileName:   合同签订页.py
# @Author:     刘峰
# @CreateTime: 2022/8/20 16:06

from base.base_page import BasePage

class ContractSignPage(BasePage):

    url = BasePage.SERVER + "#/ehr/contract/contractSign"

    人员姓名 = "//label[text()='人员姓名']/../div/div/input"
    查询按钮 = "//button/span[text()='查询']"

    增加按钮 = "//button/span[text()='增加']"
    生效按钮 = "//button/span[text()='生效']"
    提示生效合同的确定按钮 = "//div[@class='el-message-box__btns']/button[2]"

    第一行数据 = "//table[@class='vxe-table--body']/tbody/tr[1]"
    # 点击生效按钮后提示
    操作成功 = "//p[@class='el-message__content']"

    # 跳转到合同签订新增页
    def skipToContractSignAdd(self):
        self.open(self.url, 1)
        self.click(self.增加按钮, 1)

    # 查询合同签订单
    def searchContractSign(self, name):
        self.open(self.url, 1)
        self.input(self.人员姓名, name)
        self.click(self.查询按钮, 1)

    # 合同签订，点击生效，前置条件：查询出相应合同
    def comeIntoforce(self, name):
        self.searchContractSign(name)
        self.click(self.第一行数据, 0.5)
        self.click(self.生效按钮, 0.5)
        self.click(self.提示生效合同的确定按钮, 2)
