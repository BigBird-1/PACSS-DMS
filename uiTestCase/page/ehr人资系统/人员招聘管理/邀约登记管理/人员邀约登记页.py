# -*- coding:utf-8 -*
# @FileName:   人员邀约登记页.py
# @Author:     刘峰
# @CreateTime: 2022/8/17 13:40

from base.base_page import BasePage

class InviteListPage(BasePage):

    url = BasePage.SERVER + "#/ehr/recruitment/inviteManage/inviteList"

    增加按钮 = "//button/span[text()='增加']"

    # 跳转到员邀约登记-新增页
    def skipToInviteAdd(self):
        self.open(self.url, 2)
        self.click(self.增加按钮, 1)

