# -*- coding:utf-8 -*
# @FileName:   合同签订编辑页.py
# @Author:     刘峰
# @CreateTime: 2022/8/20 16:12

from base.base_page import BasePage

class ContractSignEditPage(BasePage):

    保存按钮 = "//button/span[text()='保存']"
    选择人员按钮 = "//button/span[text()='选择人员']"

    合同开始日期 = "//label[@for='begindate']/../div/div/input"
    试用期工资 = "//label[@for='vprobsalary']/../div/div/input"
    签订原因 = "//label[@for='from']/../div/div/div/input"
    提示超过30天的确认按钮 = "//div[@class='el-message-box__btns']/button[2]"

    """
        选择人员窗口
    """
    选择人员确定按钮 = "//div/button/span[text()='确定']"
    人员姓名 = "(//label[text()='人员姓名']/../div/div/input)[2]"
    选择人员查询按钮 = "//button/span[text()='查询']"
    第一行数据 = "//table[@class='vxe-table--body']/tbody/tr[1]"

    # 新增合同签订，前置条件：跳转到合同签订新增页
    def addContractSign(self, name, begindate, reason):
        # 选择人员
        self.click(self.选择人员按钮, 2)
        self.input(self.人员姓名, name)
        self.click(self.选择人员查询按钮, 2)
        self.click(self.第一行数据, 0.5)
        self.click(self.选择人员确定按钮, 1)
        # 修改合同开始日期超过一个月，先写死2022-07-15
        self.input(self.合同开始日期, begindate, isclear=False)
        self.click(self.试用期工资)
        self.select(self.签订原因, reason)
        # 保存
        self.click(self.保存按钮, 0.5)
        self.click(self.提示超过30天的确认按钮, 2)

