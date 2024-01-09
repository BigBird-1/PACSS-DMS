# -*- coding:utf-8 -*
# @FileName:   报到入职确认页.py
# @Author:     刘峰
# @CreateTime: 2022/8/20 17:17

from base.base_page import BasePage

class EmployConfirmPage(BasePage):

    url = BasePage.SERVER + "#/ehr/recruitment/employManage/employConfirm"

    姓名 = "//label[text()='姓名']/../div/div/input"
    查询按钮 = "//button/span[text()='查询']"

    入职确认按钮 = "//button/span[text()='入职确认']"
    提示继续入职的确认按钮 = "//div[@class='el-message-box__btns']/button[2]"
    提示3年劳动合同的确认按钮 = "//div[@class='el-message-box__btns']/button[2]"
    人员档案按钮 = "//button/span[text()='人员档案']"

    第一行勾选框 = "//tbody/tr[1]/td[1]/div/span/span[2]"
    第一行数据 = "//table[@class='vxe-table--body']/tbody/tr[1]"
    # 点击入职确认按钮后提示
    操作成功 = "//p[@class='el-message__content']"

    # 查询报到入职单
    def searchRegisterEntry(self, name, isclear=False):
        self.open(self.url, 2)
        self.input(self.姓名, name, isclear, wait=0.5)
        self.click(self.查询按钮, 1)

    # 跳转到人员档案维护-修改页
    def skipToPsnArchivesEdit(self, name):
        self.searchRegisterEntry(name)
        self.click(self.第一行数据, 0.5)
        self.click(self.人员档案按钮, 1)

    # 点击入职确认
    def clickEmployConfirm(self, name, isclear=False):
        self.searchRegisterEntry(name, isclear)
        self.click(self.第一行勾选框, 0.5)
        self.click(self.入职确认按钮, 0.5)
        self.click(self.提示继续入职的确认按钮, 0.5)
        self.click(self.提示3年劳动合同的确认按钮, 2)