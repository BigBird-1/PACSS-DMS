# -*- coding:utf-8 -*
# @FileName:   录用申请详情页.py
# @Author:     刘峰
# @CreateTime: 2022/8/19 11:46

from base.base_page import BasePage

class EmployDetailPage(BasePage):

    保存按钮 = "//div[@class='oe-btn-group']/button/span[text()='保存']"
    附件按钮 = "//button/span[text()='附件']"

    单据名称 = "//label[@for='bill_name']/../div/div/input"
    编制类型 = "//label[@for='wktype']/../div/div/div/input"
    录用部门 = "//tr/td[2]/div/div/div/div/div/input"
    录用岗位 = "//tr/td[3]/div/div/div/div/div/input"
    应聘人员 = "//tr/td[5]/div/div/div/div/div/input"
    人员类别 = "//tr/td[6]/div/div/div/div/div/input"
    工资数额 = "//tr/td[7]/div/div/div/div/input"
    是否精英行业 = "//tr/td[8]/div/div/div/div/div/input"
    试用期工资 = "//tr/td[13]/div/div/div/div/input"
    # 保存后提示
    保存成功 = "//p[@class='el-message__content']"

    """
        应聘人员选择窗口
    """
    人员姓名 = "//label[text()='人员姓名']/../div/div/input"
    查询按钮 = "//button/span[text()='查询']"
    应聘人员第一行勾选框 = "//tbody/tr[1]/td[1]/div/span[@class='vxe-cell--radio']/span[2]"
    应聘人员保存按钮 = "//div[@class='dialog-position']/button/span[text()='保存']"

    """
        附件管理窗口
    """
    身份证档案上传按钮 = "//tbody/tr[2]/td[2]/div/button/span[text()='上传']"
    原离职证明上传按钮 = "//tbody/tr[8]/td[2]/div/button/span[text()='上传']"
    体检报告上传按钮 = "//tbody/tr[9]/td[2]/div/button/span[text()='上传']"
    附件管理关闭按钮 = "//span[text()='附件管理']/../button[@aria-label='Close']"

    """
        上传文件窗口
    """
    选择文件按钮 = "//span[text()='选择文件']/../../input"
    上传文件确定按钮 = "//div[contains(text(), '上传文件')]/../../div[2]/div/button[1]"


    # 新增录用申请，前置条件：已跳转到新增页
    def addEmployApply(self, bill_name, wktype, name, dept, post, sort, salary, elite_industry, trial_salary, file_path1,
                       file_path2, file_path3):
        self.input(self.单据名称, bill_name)
        self.select(self.编制类型, wktype)
        self.click(self.应聘人员, 1)
        self.input(self.人员姓名, name)
        self.click(self.查询按钮, 1)
        self.click(self.应聘人员第一行勾选框)
        self.click(self.应聘人员保存按钮, 5)
        self.select(self.录用部门, dept)
        self.select(self.录用岗位, post)
        self.select(self.人员类别, sort)
        self.input(self.工资数额, salary)
        self.select(self.是否精英行业, elite_industry)
        self.input(self.试用期工资, trial_salary)
        # 上传附件
        self.click(self.附件按钮, 1)
        self.click(self.身份证档案上传按钮)
        self.input(self.选择文件按钮, file_path1, wait=1)
        self.click(self.上传文件确定按钮, 1)
        self.click(self.原离职证明上传按钮)
        self.input(self.选择文件按钮, file_path2, wait=1)
        self.click(self.上传文件确定按钮, 1)
        self.click(self.体检报告上传按钮)
        self.input(self.选择文件按钮, file_path3, wait=1)
        self.click(self.上传文件确定按钮, 1)
        self.click(self.附件管理关闭按钮, 1)
        # 保存
        self.click(self.保存按钮, 2)


