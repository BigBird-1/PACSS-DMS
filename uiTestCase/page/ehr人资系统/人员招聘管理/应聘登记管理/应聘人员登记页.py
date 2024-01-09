# -*- coding:utf-8 -*
# @FileName:   应聘人员登记页.py
# @Author:     刘峰
# @CreateTime: 2022/8/17 17:04

from uiTestCase.base.base_page import BasePage


class RecruitListPage(BasePage):

    url = BasePage.SERVER + "#/ehr/recruitment/recruitManage/recruitList"

    姓名 = "//label[text()='姓名']/../div/div/input"
    查询按钮 = "//button/span[text()='查询']"
    增加按钮 = "//button/span[text()='增加']"
    编辑按钮 = "//button/span[text()='编辑']"

    全选框 = "//span[@title='全选/取消']/span[2]"

    # 跳转到应聘人员登记-新增页
    def skipToRecruitAdd(self):
        self.open(self.url, 2)
        self.click(self.增加按钮, 2)

    # 查询人员登记单
    def searchRecruit(self, name):
        self.open(self.url, 2)
        self.input(self.姓名, name)
        self.click(self.查询按钮, 2)

    # 跳转到应聘人员登记-编辑页
    def skipToRecruitEdit(self, name,phone):
        self.searchRecruit(name)
        # 根据手机号选中人员
        self.clickByText(phone)
        self.click(self.编辑按钮, 2)



