# -*- coding:utf-8 -*
# @FileName:   test_员工招聘入职业务流程.py
# @Author:     刘峰
# @CreateTime: 2022/8/17 15:24

"""
    员工招聘入职业务流程:
        1、人员邀约登记；   2、应聘人员登记；   3、录用申请;   4、录用审批；    5、合同签订；    6、报到入职确认；
"""
import os
import time, allure, pytest

from data_driver.getData import getYaml
from data_driver.randomData import *
from page.ehr人资系统.人员招聘管理.应聘登记管理.应聘人员登记详情页 import RecruitDetailPage
from page.ehr人资系统.人员招聘管理.应聘登记管理.应聘人员登记页 import RecruitListPage
from page.ehr人资系统.人员招聘管理.录用管理.录用申请详情页 import EmployDetailPage
from page.ehr人资系统.人员招聘管理.录用管理.录用申请页 import EmployApplyPage
from page.ehr人资系统.人员招聘管理.录用管理.报到入职确认页 import EmployConfirmPage
from page.ehr人资系统.人员招聘管理.邀约登记管理.人员邀约登记详情页 import InviteDetailPage
from page.ehr人资系统.人员招聘管理.邀约登记管理.人员邀约登记页 import InviteListPage
from page.ehr人资系统.人员档案管理.员工合同管理.合同签订编辑页 import ContractSignEditPage
from page.ehr人资系统.人员档案管理.员工合同管理.合同签订页 import ContractSignPage
from page.ehr人资系统.人员档案管理.员工电子档案管理.员工电子档案编辑页 import PsnArchivesEditPage
from page.wfs行政系统.个人办公.事项管理.业务审批页 import AuditBillPage
from page.wfs行政系统.个人办公.事项管理.待办事项页 import TodoListPage


@allure.feature("员工招聘入职业务流程")
class TestInviteEntry:

    @allure.title("员工招聘入职业务流程-初始化方法")
    def test_begin(self, login):
        TestInviteEntry.ilp = InviteListPage(login)
        TestInviteEntry.idp = InviteDetailPage(login)
        TestInviteEntry.rlp = RecruitListPage(login)
        TestInviteEntry.rdp = RecruitDetailPage(login)
        TestInviteEntry.eap = EmployApplyPage(login)
        TestInviteEntry.edp = EmployDetailPage(login)
        TestInviteEntry.tlp = TodoListPage(login)
        TestInviteEntry.abp = AuditBillPage(login)
        TestInviteEntry.csp = ContractSignPage(login)
        TestInviteEntry.cep = ContractSignEditPage(login)
        TestInviteEntry.ecp = EmployConfirmPage(login)
        TestInviteEntry.pep = PsnArchivesEditPage(login)

    @allure.title("测试用例1：人员邀约登记；")
    @pytest.mark.parametrize("dict", getYaml(r'./data/ehr人资系统/新增人员邀约登记.yaml'))
    def test_inviteRegister(self, dict):
        with allure.step("步骤1：跳转到新增人员邀约登记页；"):
            self.ilp.skipToInviteAdd()

        with allure.step("步骤2：填写相关信息，保存；"):
            TestInviteEntry.name = random_name()
            TestInviteEntry.phone = random_mobile()
            self.idp.addInvite(invite_data=time.strftime("%Y-%m-%d"), name=TestInviteEntry.name,
                               phone=TestInviteEntry.phone, dept=dict['邀约部门'], post=dict['应聘岗位'],
                               if_invite=dict['是否应邀'], interview_date=time.strftime("%Y-%m-%d"),
                               interview_time=dict['拟面试时间'], sex=dict['性别'], channel=dict['渠道'],
                               education_id=dict['最高学历'], school=dict['毕业院校'], major=dict['专业'])

        with allure.step("步骤3：验证新增人员邀约登记保存是否成功；"):
            actual = self.idp.getText(self.idp.操作成功)
            expect = dict['期望值']
            assert expect in actual

    @allure.title("测试用例2：应聘人员登记;")
    @pytest.mark.parametrize("dict", getYaml(r'./data/ehr人资系统/新增应聘人员登记.yaml'))
    def test_recruitRegister(self, dict):

        with allure.step("步骤1：新增应聘人员，填写并保存基本信息；"):
            self.rlp.skipToRecruitAdd()
            self.rdp.addRecruitBasic(name=TestInviteEntry.name, reg_date=time.strftime("%Y-%m-%d"), national=dict['民族'],
                                     id_number=random_card(), relation1=dict['与本人关系第一行'], name1=random_name(),
                                     id_number1=random_card(), phone1=random_mobile(), relation2=dict['与本人关系第二行'],
                                     name2=random_name(), id_number2=random_card(), phone2=random_mobile())

        with allure.step("步骤2：填写并保存面试信息；"):
            self.rlp.skipToRecruitEdit(name=TestInviteEntry.name, phone=TestInviteEntry.phone)
            path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + dict['文件路径']
            self.rdp.addRecruitInterview(indutydate=time.strftime("%Y-%m-%d"), file_path=path, first_opinion=dict['初试意见'],
                            first_interviewer=dict['初试面试人'], first_interview_time=time.strftime("%Y-%m-%d %H:%M:%S"),
                            retest_opinion=dict['复试意见'], retest_interviewer=dict['复试面试人'], retest_interview_time=time.strftime("%Y-%m-%d %H:%M:%S"),
                            final_opinion=dict['终试意见'], employ_position=dict['雇佣岗位'], wage=dict['试用期工资'],
                            final_interviewer=dict['终试面试人'], final_interview_time=time.strftime("%Y-%m-%d %H:%M:%S"))

        with allure.step("步骤3：验证面试信息是否保存成功；"):
            actual = self.rdp.getText(self.rdp.面试评估已通过)
            expect = dict['期望值']
            assert expect in actual

        with allure.step("步骤4：填写并保存背调信息；"):
            self.rdp.addRecruitBack(certifier_name=random_name(), certifier_job=dict['证明人职务'], certifier_phone=random_mobile(),
                        candidate_job=dict['候选人职务'], company_name=dict['候选人原任职公司名称'], work_startdate=dict['候选人工作起始时间'],
                        work_enddate=dict['候选人工作终止时间'], promotion_demotion=dict['晋升或降职情况'], job_duty=dict['实际工作职责'],
                        salary_category=dict['薪资范畴'], work_manage_ability=dict['对其工作风格管理能力的看法'],
                        along_colleagues=dict['与其他同事相处的如何'], resign_reason=dict['离职原因'], reward_punishment=dict['奖惩违规记录'],
                        labor_dispute=dict['有无劳动争议或纠纷'], hire_work=dict['是否愿意再次雇佣共事'])

        with allure.step("步骤5：验证保存背调信息是否成功；"):
            actual = self.rdp.getText(self.rdp.操作成功)
            expect = dict['背调期望值']
            assert expect in actual

    @allure.title("测试用例3：录用申请;")
    @pytest.mark.parametrize("dict", getYaml(r'./data/ehr人资系统/新增录用申请.yaml'))
    def test_employApply(self, dict):

        with allure.step("步骤1：跳转到录用申请-新增页；"):
            self.eap.skipToEmployApplyAdd()

        with allure.step("步骤2：新增录用申请；"):
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            self.edp.addEmployApply(bill_name=dict['单据名称'], wktype=dict['编制类型'], name=TestInviteEntry.name,
                                    dept=dict['录用部门'], post=dict['录用岗位'], sort=dict['人员类别'], salary=dict['工资数额'],
                                    elite_industry=dict['是否精英行业'], trial_salary=dict['试用期工资'],
                                    file_path1=base_path + dict['身份证档案'], file_path2=base_path + dict['原离职证明'],
                                    file_path3=base_path + dict['体检报告'])

        with allure.step("步骤3：验证新增录用申请保存成功；"):
            actual = self.edp.getText(self.edp.保存成功)
            expect = dict['期望值']
            assert expect in actual

    @allure.title("测试用例4：录用审批;")
    def test_employApproval(self):

        with allure.step("步骤1：查询录用申请单，提交；"):
            TestInviteEntry.receipt_number = self.eap.commitEmployApply(name=TestInviteEntry.name)

        with allure.step("步骤2：审核录用申请单；"):
            self.tlp.skipToApproval(receipt_number=TestInviteEntry.receipt_number)
            self.abp.approvalPass()

        with allure.step("步骤3：验证录用申请单是否审核成功；"):
            self.eap.searchEmployApply(name=TestInviteEntry.name, isclear=True)
            actual = self.eap.getText(self.eap.第一行审批状态)
            expect = "已批准"
            assert expect in actual

    @allure.title("测试用例5：合同签订;")
    @pytest.mark.parametrize("dict", getYaml(r'./data/ehr人资系统/新增合同签订.yaml'))
    def test_contractSign(self, dict):

        with allure.step("步骤1：新增合同签订，保存；"):
            self.csp.skipToContractSignAdd()
            self.cep.addContractSign(name=TestInviteEntry.name, begindate=dict['合同开始日期'], reason=dict['签订原因'])

        with allure.step("步骤2：在人员档案中上传劳动合同（集团）,传劳动合同（公司）,保密协议；"):
            self.ecp.skipToPsnArchivesEdit(name=TestInviteEntry.name)
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            self.pep.uploadFiles(file_path1=base_path + dict['劳动合同（集团）'], file_path2=base_path + dict['劳动合同（公司）'],
                                 file_path3=base_path + dict['保密协议'], file_path4=base_path + dict['安全生产经营承诺书（2019）'],
                                 file_path5=base_path + dict['集团文件学习确认书'], file_path6=base_path + dict['新员工入职培训记录'],
                                 file_path7=base_path + dict['办公计算机使用承诺书'])

        with allure.step("步骤3：合同签订页，点击生效；"):
            self.csp.comeIntoforce(name=TestInviteEntry.name)

        with allure.step("步骤4：验证合同生效是否成功；"):
            actual = self.csp.getText(self.csp.操作成功)
            expect = dict['期望值']
            assert expect in actual

    @allure.title("测试用例6：入职确认;")
    def test_employConfirm(self):

        with allure.step("步骤1：在报到入职确认页中，点击入职确认；"):
            self.ecp.clickEmployConfirm(name=TestInviteEntry.name, isclear=True)

        with allure.step("步骤2：验证入职确认是否成功："):
            actual = self.ecp.getText(self.ecp.操作成功)
            expect = "操作成功"
            assert expect in actual

