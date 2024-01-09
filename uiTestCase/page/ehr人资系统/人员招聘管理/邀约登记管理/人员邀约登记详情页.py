# -*- coding:utf-8 -*
# @FileName:   人员邀约登记详情页.py
# @Author:     刘峰
# @CreateTime: 2022/8/17 13:55

from base.base_page import BasePage

class InviteDetailPage(BasePage):

    保存按钮 = "//button/span[text()='保存']"

    邀约日期 = "//label[@for='invitation_date']/../div/div/input"
    姓名 = "//label[@for='psnname']/../div/div/input"
    手机 = "//label[@for='phone']/../div/div/input"
    邀约部门 = "//label[text()='邀约部门']/../div/div/div/input"
    应聘岗位 = "//label[@for='position_id']/../div/div/div/input"
    是否应邀 = "//label[text()='是否应邀']/../div/div/div/input"
    拟面试日期 = "//label[@for='interview_date']/../div/div/input"
    拟面试时间 = "//label[@for='interview_time']/../div/div/input"
    性别 = "//label[@for='sex']/../div/div/div/input"
    渠道 = "//label[@for='invitation_channel']/../div/div/div/input"
    最高学历 = "//label[@for='education_id']/../div/div/div/input"
    毕业院校 = "//label[@for='school']/../div/div/input"
    专业 = "//label[@for='major']/../div/div/input"

    # 保存后成功提示
    操作成功 = "//p[@class='el-message__content']"

    # 新增人员邀约，前置条件：已跳转到新增页
    def addInvite(self, invite_data, name, phone, dept, post, if_invite, interview_date, interview_time, sex, channel,
                  education_id, school, major):
        self.input(self.邀约日期, invite_data)
        self.click(self.姓名)     # 关掉时间框
        self.input(self.姓名, name)
        self.input(self.手机, phone, wait=2)
        self.select(self.邀约部门, dept)
        self.select(self.应聘岗位, post)
        self.select(self.是否应邀, if_invite)
        self.input(self.拟面试日期, interview_date)
        self.input(self.拟面试时间, interview_time)
        self.select(self.性别, sex)
        self.select(self.渠道, channel)
        self.select(self.最高学历, education_id)
        self.input(self.毕业院校, school)
        self.input(self.专业, major)
        self.click(self.保存按钮, wait=1)


