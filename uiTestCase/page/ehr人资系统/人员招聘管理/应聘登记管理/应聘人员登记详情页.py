# -*- coding:utf-8 -*
# @FileName:   应聘人员登记详情页.py
# @Author:     刘峰
# @CreateTime: 2022/8/17 17:13

from uiTestCase.base.base_page import BasePage


class RecruitDetailPage(BasePage):

    保存按钮 = "//button/span[text()='保存']"
    手工修改按钮 = "//button/span[text()='手工修改']"
    选择人员按钮 = "//button/span[text()='选择人员']"
    打印应聘登记表 = "//button/span[text()='打印应聘登记表']"

    """
        基本信息Tab页
    """
    面试日期 = "//label[@for='reg_date']/../div/div/input"
    面试时间 = "//label[@for='reg_time']/../div/div/input"
    面试时间确定按钮 = "//div[@class='el-time-panel__footer']/button[text()='确定']"
    民族 = "//label[@for='nationality_id']/../div/div/div/input"
    身份证号 = "//label[@for='id']/../div/div/input"
    拟入职日期 = "//label[@for='indutydate']/../div/div/input"
    备注 = "//label[text()='备注']/../div/div/textarea"
    上传文件按钮 = "//button/span[text()='上传文件']"

    """
        选择人员窗口
    """
    姓名 = "//div[@id='oeSearchView']/form/div/div[1]/div/div/div/input"
    查询按钮 = "//button/span[text()='查询']"
    选择人员第一行勾选框 = "//tbody/tr[1]/td[1]/div/span[@class='vxe-cell--radio']/span[2]"
    选择人员确定按钮 = "//div[@class='el-dialog__body']/div/button/span[text()='确定']"

    """
        上传文件窗口
    """
    选择文件按钮 = "//span[text()='选择文件']/../../input"
    上传文件确定按钮 = "//div[@class='dialog-position']/button[1]"

    """
        面试信息Tab页
    """
    面试信息Tab页 = ("id", "tab-interviewInfo")
    提示框中确定打印按钮 = "//div[@class='el-message-box__btns']/button[2]/span[contains(text(), '确定')]"
    形象气质5分 = "//label[@for='image']/../div/div/label[1]"
    性格合适度5分 = "//label[@for='character']/../div/div/label[1]"
    沟通能力5分 = "//label[@for='communication']/../div/div/label[1]"
    专业经验5分 = "//label[@for='profession']/../div/div/label[1]"
    稳定性5分 = "//label[@for='stability']/../div/div/label[1]"
    能力心态5分 = "//label[@for='ability']/../div/div/label[1]"
    初试意见输入框 = "//p[contains(text(), '初试意见（行政人事部门）')]/../div[3]/div/div/textarea"
    初试面试人 = "//label[@for='first_interviewer']/../div/div/input"
    初试面试时间 = "//label[@for='first_interview_time']/../div/div/input"
    面试时间确定按钮 = "//div[@x-placement='top-start']/div[2]/button[2]"
    初试通过单选框 = "//label[@for='first_advance']/../div/div/label[1]/span[text()='通过']"
    复试意见输入框 = "//p[contains(text(), '复试意见（用人部门）')]/../div[6]/div/div/textarea"
    复试面试人 = "//label[@for='retest_interviewer']/../div/div/input"
    复试面试时间 = "//label[@for='retest_interview_time']/../div/div/input"
    复试通过单选框 = "//label[@for='retest_advance']/../div/div/label[1]/span[text()='通过']"
    终试意见输入框 = "//p[contains(text(), '终试意见（批复意见）')]/../div[9]/div/div/textarea"
    录用岗位 = "//label[@for='employ_position_id']/../div/div/div/input"
    试用期工资 = "//label[@for='wage']/..//div/div/input"
    终试面试人 = "//label[@for='final_interviewer']/..//div/div/input"
    终试面试时间 = "//label[@for='final_interview_time']/..//div/div/input"
    录用选择框 = "//label/span[text()='录用']"
    提示框中确认修改人员按钮 = "//div[@class='el-message-box__btns']/button[2]/span[contains(text(), '确定')]"
    # 保存后提示
    面试评估已通过 = "//p[@class='el-message__content']"

    """
        背调信息Tab页
    """
    证明人姓名 = "//label[@for='backinfo.certifier_name']/../div/div/input"
    证明人职务 = "//label[@for='backinfo.certifier_job']/../div/div/input"
    证明人联系方式 = "//label[@for='backinfo.certifier_phone']/../div/div/input"
    候选人职务 = "//label[@for='backinfo.candidate_job']/../div/div/input"
    候选人原任职公司名称 = "//label[@for='backinfo.orgin_company_name']/../div/div/input"
    候选人工作起始时间 = "//label[@for='backinfo.work_startdate']/../div/div/div[1]/input"
    候选人工作终止时间 = "//label[@for='backinfo.work_startdate']/../div/div/div[2]/input"
    晋升或降职情况 = "//label[@for='backinfo.promotion_demotion']/../div/div/textarea"
    实际工作职责 = "//label[@for='backinfo.job_duty']/../div/div/input"
    薪资范畴 = "//label[@for='backinfo.salary_category']/../div/div/input"
    背调记录人 = "//label[@for='backinfo.backinfo_psnname']/../div/div/div/input"
    对其工作风格管理能力的看法 = "//label[@for='backinfo.work_manage_ability']/../div/div/textarea"
    与其他同事相处的如何 = "//label[@for='backinfo.along_colleagues']/../div/div/textarea"
    离职原因 = "//label[@for='backinfo.resign_reason']/../div/div/textarea"
    与公司签订竞业条款 = "//label[@for='backinfo.sign_competition']/../div/div/label[1]/span[text()='是']"
    终止解除劳动合同 = "//label[@for='backinfo.terminate_contract']/../div/div/label[1]/span[text()='是']"
    奖惩违规记录 = "//label[@for='backinfo.reward_punishment']/../div/div/textarea"
    有无劳动争议或纠纷 = "//label[@for='backinfo.labor_dispute']/../div/div/textarea"
    是否愿意再次雇佣共事 = "//label[@for='backinfo.hire_work']/../div/div/textarea"
    # 保存后提示操作成功
    操作成功 = "//p[@class='el-message__content']"

    """
        背调记录人员列表
    """
    背调记录第一行勾选框 = "//tbody/tr[1]/td[2]/div/span[@class='vxe-cell--radio']/span[2]"
    人员列表确定按钮 = "//div[@class='el-dialog__wrapper']/div/div[2]/div[1]/button[1]/span[text()='确定']"

    """
        紧急联系人Tab页
    """
    紧急联系人 = ("id", "tab-6")
    紧急联系人增行按钮 = "//div[@id='pane-6']/form/p/button/span[text()='增行']"
    与本人关系第一行 = "//tbody/tr[1]/td[3]/div/div/div/div/div/input"
    姓名第一行 = "//tbody/tr[1]/td[4]/div/div/div/div/input"
    身份证号码第一行 = "//tbody/tr[1]/td[5]/div/div/div/div/input"
    电话第一行 = "//tbody/tr[1]/td[6]/div/div/div/div/input"
    与本人关系第二行 = "//tbody/tr[2]/td[3]/div/div/div/div/div/input"
    姓名第二行 = "//tbody/tr[2]/td[4]/div/div/div/div/input"
    身份证号码第二行 = "//tbody/tr[2]/td[5]/div/div/div/div/input"
    电话第二行 = "//tbody/tr[2]/td[6]/div/div/div/div/input"


    # 新增应聘人员-保存基本信息，前置条件：已跳转到新增页
    def addRecruitBasic(self, name, reg_date, national, id_number, relation1, name1, id_number1, phone1, relation2, name2,
                        id_number2, phone2):
        # 点击选择人员
        self.click(self.选择人员按钮, 1)
        self.input(self.姓名, name, 0.5)
        self.click(self.查询按钮, 1)
        self.click(self.选择人员第一行勾选框)
        self.click(self.选择人员确定按钮)
        # 填写基本信息
        self.click(self.手工修改按钮)
        self.input(self.面试日期, reg_date)
        self.click(self.面试时间, 0.5)
        self.click(self.身份证号)  # 关闭时间框
        self.select(self.民族, national)
        self.input(self.身份证号, id_number, wait=1)
        # 增加紧急联系人
        self.click(self.紧急联系人, 0.5)
        self.click(self.紧急联系人增行按钮, 0.5)
        self.select(self.与本人关系第一行, relation1)
        self.input(self.姓名第一行, name1)
        self.input(self.身份证号码第一行, id_number1)
        self.input(self.电话第一行, phone1)
        self.click(self.紧急联系人增行按钮, 0.5)
        self.select(self.与本人关系第二行, relation2)
        self.input(self.姓名第二行, name2)
        self.input(self.身份证号码第二行, id_number2)
        self.input(self.电话第二行, phone2)

        self.click(self.保存按钮, 2)

    # 新增应聘人员-保存面试信息，前置条件：已保存基本信息，且跳转到编辑页面
    def addRecruitInterview(self, indutydate, file_path, first_opinion, first_interviewer, first_interview_time,
                            retest_opinion, retest_interviewer, retest_interview_time, final_opinion, employ_position,
                            wage, final_interviewer, final_interview_time):
        # 取消打印应聘登记表
        self.click(self.打印应聘登记表)
        self.click(self.提示框中确定打印按钮)
        self.wait(2)
        # 通过返回关闭打印界面
        self.driver.back()
        # 先在基本信息中填写‘拟入职日期’和上传文件
        self.input(self.拟入职日期, indutydate)
        self.click(self.备注)     # 点击备注是为了关掉拟入职日期的时间框
        self.click(self.上传文件按钮)
        self.input(self.选择文件按钮, file_path, wait=1)
        self.click(self.上传文件确定按钮)

        # 切换到面试信息页，填写面试信息
        self.click(self.面试信息Tab页)
        self.click(self.形象气质5分)
        self.click(self.性格合适度5分)
        self.click(self.沟通能力5分)
        self.click(self.专业经验5分)
        self.click(self.稳定性5分)
        self.click(self.能力心态5分)
        self.input(self.初试意见输入框, first_opinion)
        self.input(self.初试面试人, first_interviewer)
        self.input(self.初试面试时间, first_interview_time, wait=0.5)
        self.click(self.面试时间确定按钮)
        self.click(self.初试通过单选框)
        self.input(self.复试意见输入框, retest_opinion)
        self.input(self.复试面试人, retest_interviewer)
        self.input(self.复试面试时间, retest_interview_time, wait=0.5)
        self.click(self.面试时间确定按钮)
        self.click(self.复试通过单选框)
        self.input(self.终试意见输入框, final_opinion)
        self.select(self.录用岗位, employ_position)
        self.input(self.试用期工资, wage)
        self.input(self.终试面试人, final_interviewer)
        self.input(self.终试面试时间, final_interview_time, wait=0.5)
        self.click(self.面试时间确定按钮)
        self.click(self.录用选择框)

        self.click(self.保存按钮)
        self.click(self.提示框中确认修改人员按钮, 2)

    # 新增应聘人员-保存背调信息，前置条件：已保存面试信息，且跳转到编辑页面的背调信息Tab页
    def addRecruitBack(self, certifier_name, certifier_job, certifier_phone, candidate_job, company_name, work_startdate,
                       work_enddate, promotion_demotion, job_duty, salary_category, work_manage_ability, along_colleagues,
                       resign_reason, reward_punishment, labor_dispute, hire_work):
        self.input(self.证明人姓名, certifier_name)
        self.input(self.证明人职务, certifier_job)
        self.input(self.证明人联系方式, certifier_phone)
        self.input(self.候选人职务, candidate_job)
        self.input(self.候选人原任职公司名称, company_name)
        self.input(self.候选人工作起始时间, work_startdate)
        self.input(self.候选人工作终止时间, work_enddate)
        self.click(self.晋升或降职情况)  # 关闭掉时间控件
        self.input(self.晋升或降职情况, promotion_demotion)
        self.input(self.实际工作职责, job_duty)
        self.input(self.薪资范畴, salary_category)
        self.click(self.背调记录人, 1)
        self.click(self.背调记录第一行勾选框, 0.5)
        self.click(self.人员列表确定按钮, 0.5)
        self.input(self.对其工作风格管理能力的看法, work_manage_ability)
        self.input(self.与其他同事相处的如何, along_colleagues)
        self.input(self.离职原因, resign_reason)
        self.click(self.与公司签订竞业条款)
        self.click(self.终止解除劳动合同)
        self.input(self.奖惩违规记录, reward_punishment)
        self.input(self.有无劳动争议或纠纷, labor_dispute)
        self.input(self.是否愿意再次雇佣共事, hire_work)
        # 保存
        self.click(self.保存按钮)
        self.click(self.提示框中确认修改人员按钮, 2)
