# -*- coding:utf-8 -*
# @FileName:   test_接车制单.py
# @Author:     刘峰
# @CreateTime: 2022/7/28 8:36

"""
    接车制单测试用例组：
        1、新增接车制单；   2、查询工单；   3、编辑接车制单；   4、打印工单；     5、派工；   6、提交结算；
        7、取消提交结算；   8、结算；
"""

import pytest, allure

from data_driver.getData import getYaml
from data_driver.randomData import *
from page.erp售后业务系统.售后客户管理.车主详情页 import OwnerEditPage
from page.erp售后业务系统.售后客户管理.车辆详情页 import VehicleEditPage
from page.erp售后业务系统.维修业务.接车制单详情页 import CustomerReceptionEditMainPage
from page.erp售后业务系统.维修业务.接车制单页 import CustomerReceptionPage
from page.erp售后业务系统.维修业务.结算页 import BalancePage


@allure.feature("接车制单功能测试")
class TestCustomerReception:

    @allure.title("接车制单初始化方法")
    def test_begin(self, login):
        TestCustomerReception.oep = OwnerEditPage(login)
        TestCustomerReception.vep = VehicleEditPage(login)
        TestCustomerReception.crp = CustomerReceptionPage(login)
        TestCustomerReception.crep = CustomerReceptionEditMainPage(login)
        TestCustomerReception.bp = BalancePage(login)


    @allure.title("测试用例01：新增接车制单；")
    @pytest.mark.parametrize("dicts1", getYaml(r"./data/erp售后业务系统/新增车主.yaml"))
    @pytest.mark.parametrize("dicts2", getYaml(r'./data/erp售后业务系统/新增车辆.yaml'))
    @pytest.mark.parametrize("dicts", getYaml(r'./data/erp售后业务系统/新增接车制单.yaml'))
    def test_addCustomerReception(self, dicts1, dicts2, dicts):


        with allure.step("前置操作：新增车主和车辆；"):
            self.oep.addOwner(random_mobile(), random_name(), dicts['性别'], dicts['省份'], dicts['城市'], dicts['区县'])

            self.oep.click(self.oep.add_car_button)

            TestCustomerReception.license = random_car()
            self.vep.addVehicle(license=TestCustomerReception.license, vin=random_vin(), engineNo=dicts2['发动机编号'], brand=dicts2['品牌'],
                                series=dicts2['车系'], model=dicts2['车型'], salesDate=dicts2['销售日期'], powerType=dicts2['动力类型'])

        with allure.step("步骤1：跳转到新增接车制单页；"):
            self.crp.skipToAdd()

        with allure.step("步骤2：新增接车制单；"):
            self.crep.addAustomerReception(license=TestCustomerReception.license, servicepeople=dicts['服务专员'], insurancetype=dicts['险种类型'],
                                           insurancecompany=dicts['保险公司'], project=dicts['收费区分'])

        with allure.step("步骤3：验证新增接车制单是否保存成功."):
            actual = self.crep.webDriverWait(self.crep.save_success).text
            print("新增接车制单保存后弹出的提示文字是：{}".format(actual))
            expect = '保存成功'
            assert expect in actual

            # 后置处理，取消同步到DMS，关闭维修制单新增页面，获取工单
            self.crep.cancleSyscDMS()

            self.crep.click(self.crep.goback_button)
            TestCustomerReception.order_number = self.crp.getOrderNumber()


    @allure.title("测试用例02：查询工单；")
    def test_searchCustomerReception(self):

        with allure.step("步骤1：进入接车制单页，查询工单；"):
            self.crp.searchByCondition(TestCustomerReception.order_number)

        with allure.step("步骤2：验证查询结果是否正确；"):
            actual = self.crp.getText(self.crp.order_number_text)
            expect = TestCustomerReception.order_number
            assert actual == expect


    @allure.title("测试用例03：编辑接车制单；")
    def test_editCustomerReception(self):

        with allure.step("步骤1：进入编辑接车制单界面；"):
            self.crp.skipToEdit(TestCustomerReception.order_number)

        with allure.step("步骤2：编辑厂家委托书号、行驶里程，保存；"):
            self.crep.editAustomerReception(2022080144316, 200)

        with allure.step("步骤3：验证编辑是否成功；"):
            actual = self.crep.webDriverWait(self.crep.save_success).text
            expect = "保存成功"
            assert expect in actual

            # 后置处理，取消同步到DMS
            self.crep.cancleSyscDMS()


    @allure.title("测试用例04：打印工单；")
    def test_printOrder(self):

        with allure.step("步骤1：点击打印工单；"):
            self.crep.printOrder()

        with allure.step("步骤2：验证是否进入到打印工单页；"):
            self.crep.switchWindow()
            actual = self.crep.getText(self.crep.service_attorney_book)
            expect = "服务委托书"
            assert expect in actual

            # 后置处理，关闭打印界面
            self.crep.switchWindow(window=0, close=True)


    @allure.title("测试用例05：派工：")
    def test_dispatching(self):

        with allure.step("步骤1：派工"):
            self.crep.dispatching("刘峰", 0.2)

        with allure.step("步骤2：验证派工是否保存成功."):
            actual = self.crep.webDriverWait(self.crep.save_success).text
            print("派工保存后弹出的提示文字是：{}".format(actual))
            expect = "保存成功"
            assert expect in actual


    @allure.title("测试用例06：提交结算；")
    def test_commitAccount(self):

        with allure.step("步骤1：派工完成后直接提交结算；"):
            self.crep.commitPay()

        with allure.step("步骤2：验证提交结算是否成功；"):
            actual = self.crep.webDriverWait(self.crep.commit_order_success).text
            expect = "提交结算成功"
            assert expect in actual

            # 后置处理，关闭维修单编辑页面
            self.crep.click(self.crep.goback_button)


    @allure.title("测试用例07：取消提交结算；")
    def test_cancleAccount(self):

        with allure.step("步骤1：进入接车制单页，查询工单，取消结算；"):
            self.crp.cancleCommitAccount(TestCustomerReception.order_number, orderstate='已提交结算')

        with allure.step("步骤2：验证取消提交结算是否成功；"):
            actual = self.crp.webDriverWait(self.crp.cancle_commit_success).text
            expect = "修改成功"
            assert expect in actual


    @allure.title("测试用例08：结算；")
    def test_payBalance(self):

        with allure.step("步骤1：进入编辑界面"):
            self.crp.skipToEdit(TestCustomerReception.order_number)

        with allure.step("步骤2：保存，提交结算；"):
            self.crep.saveAndCommit()

        with allure.step("步骤3：点击结算，跳转到结算界面；"):
            self.crep.click(self.crep.settle_account_button)

        with allure.step("步骤4：进行结算；"):
            self.bp.payBalance("维修建议输入")

        with allure.step("步骤：验证结算是否成功."):
            actual = self.bp.webDriverWait(self.bp.pay_success).text
            expect = "结算成功"
            assert expect in actual

            self.crep.cancleSyscDMS()
            self.crep.click(self.crep.goback_button)
            self.crep.click(self.crep.goback_button)

