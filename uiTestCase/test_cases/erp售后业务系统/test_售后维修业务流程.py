# -*- coding:utf-8 -*
# @FileName:   test_售后维修业务流程.py
# @Author:     刘峰
# @CreateTime: 2022/7/22 15:12

"""
    售后维修业务流程：
        1、新增车主和车辆；  2、新增接车制单，创建工单；   3、派工；   4、维修领料；
        5、开工完工，自动维修质检；   6、提交结算；     7、费用结算；     8、收款。
"""
import pytest, allure, os

from data_driver.getData import getYaml
from data_driver.randomData import *
from page.erp售后业务系统.售后客户管理.车主详情页 import OwnerEditPage
from page.erp售后业务系统.售后客户管理.车辆详情页 import VehicleEditPage
from page.erp售后业务系统.维修业务.接车制单详情页 import CustomerReceptionEditMainPage
from page.erp售后业务系统.维修业务.接车制单页 import CustomerReceptionPage
from page.erp售后业务系统.维修业务.结算页 import BalancePage
from page.erp售后业务系统.维修业务.费用结算页 import SettlementPage
from page.erp售后业务系统.车间管理.车间管理.车间维修管理页 import WorkshopMaintenancePage
from page.erp财务系统.收银台.收银台页 import CashierDeskPage
from page.erp配件系统.配件管理.配件出库管理.编辑维修领料页 import EditRepairOutPage
from page.erp配件系统.配件管理.配件出库管理.配件维修领料页 import RepairOutPage


@allure.feature("售后维修业务流程测试")
class TestCustomerRepair:

    @allure.title("售后维修业务流程初始化方法")
    def test_begin(self, login):
        TestCustomerRepair.oep = OwnerEditPage(login)
        TestCustomerRepair.vep = VehicleEditPage(login)
        TestCustomerRepair.crp = CustomerReceptionPage(login)
        TestCustomerRepair.crep = CustomerReceptionEditMainPage(login)
        TestCustomerRepair.rop = RepairOutPage(login)
        TestCustomerRepair.erop = EditRepairOutPage(login)
        TestCustomerRepair.wmp = WorkshopMaintenancePage(login)
        TestCustomerRepair.sp = SettlementPage(login)
        TestCustomerRepair.bp = BalancePage(login)
        TestCustomerRepair.cdp = CashierDeskPage(login)


    @allure.title("测试用例1：新增车主和车辆；")
    @pytest.mark.parametrize("dicts1", getYaml(r"./data/erp售后业务系统/新增车主.yaml"))
    @pytest.mark.parametrize("dicts2", getYaml(r'./data/erp售后业务系统/新增车辆.yaml'))
    def test_addOwnerAndVehicle(self, dicts1, dicts2):

        with allure.step("步骤1：新增车主和车辆；"):
            self.oep.addOwner(random_mobile(), random_name(), dicts1['性别'], dicts1['省份'], dicts1['城市'], dicts1['区县'])

            self.oep.click(self.oep.add_car_button)

            TestCustomerRepair.license = random_car()
            self.vep.addVehicle(license=TestCustomerRepair.license, vin=random_vin(), engineNo=dicts2['发动机编号'], brand=dicts2['品牌'],
                                series=dicts2['车系'], model=dicts2['车型'], salesDate=dicts2['销售日期'], powerType=dicts2['动力类型'])

        with allure.step("步骤2：验证车辆是否新增成功."):
            actual = self.vep.getText(self.vep.addVehicle_success)
            expect = dicts2['期望值']
            assert expect in actual


    @allure.title("测试用例2：新增接车制单，创建工单；（客户付费）")
    @pytest.mark.parametrize("dicts", getYaml(r"./data/erp售后业务系统/新增接车制单.yaml"))
    def test_addAustomerReception(self, dicts):

        with allure.step("步骤1：跳转到新增接车制单页；"):
            self.crp.skipToAdd()

        with allure.step("步骤2：新增接车制单；"):
            self.crep.addAustomerReception(license=TestCustomerRepair.license, servicepeople=dicts['服务专员'],
                    insurancetype=dicts['险种类型'], insurancecompany=dicts['保险公司'],
                    project=dicts['收费区分'], isMaterial=True, partsnumber=dicts['配件代码'])

        with allure.step("步骤3：验证新增工单是否保存成功."):
            actual = self.crep.getText(self.crep.save_success)
            print("新增工单保存后弹出的提示文字是：{}".format(actual))
            expect = '保存成功'
            assert expect in actual

            # 后置处理，取消同步到DMS
            self.crep.cancleSyscDMS()


    @allure.title("测试用例3：派工；")
    def test_dispatching(self):

        with allure.step("步骤1：派工"):
            self.crep.dispatching("刘峰", 0.1)

        with allure.step("步骤2：验证派工是否保存成功."):
            actual = self.crep.getText(self.crep.save_success)
            expect = "保存成功"
            assert expect in actual

            # 后置处理，关闭维修制单新增页面，获取工单号
            self.crep.click(self.crep.goback_button)
            TestCustomerRepair.order_number = self.crp.getOrderNumber()


    @allure.title("测试用例4：维修领料；")
    def test_maintainPick(self):

        with allure.step("步骤1：跳转到编辑维修领料页；"):
            self.rop.skipToMaintainPick(TestCustomerRepair.order_number)

        with allure.step("步骤2：编辑维修领料，修改领料人，出库；"):
            self.erop.editMaintainPick("周海波")

        with allure.step("步骤3：验证出库是否成功."):
            actual = self.erop.getText(self.erop.out_bank_success)
            print("出库后弹出的提示文字是：{}".format(actual))
            expect = "出库成功"
            assert expect in actual

            # 后置处理，关闭编辑维修领料界面
            self.erop.click(self.crep.goback_button, 0.5)


    @allure.title("测试用例5：开工完工，自动维修质检；")
    def test_workshopMaintenance(self):

        with allure.step("步骤1：全部开工；"):
            self.wmp.startWork(TestCustomerRepair.order_number)

        with allure.step("步骤2：全部完工；"):
            self.wmp.completeWork()

        with allure.step("步骤3：验证完工操作是否成功."):
            actual = self.wmp.getText(self.wmp.operator_success)
            expect = "操作成功"
            assert expect in actual

            # 后置处理，关闭完工窗口
            self.wmp.click(self.wmp.back_button2)


    @allure.title("测试用例6：提交结算；")
    def test_commitAccount(self):

        with allure.step("步骤1：进入接车制单页，查询工单，提交结算；"):
            self.crp.commitAccount(TestCustomerRepair.order_number)

        with allure.step("步骤2：验证提交结算是否成功；"):
            actual = self.crp.getText(self.crp.order_commit_success)
            expect = "提交结算成功"
            assert expect in actual


    @allure.title("测试用例7：费用结算；")
    def test_payBalance(self):

        with allure.step("步骤1：从费用结算页跳转到结算页面；"):
            self.sp.skipToSettlement(TestCustomerRepair.order_number)

        with allure.step("步骤2：进行结算；"):
            self.bp.payBalance("维修建议输入")

        with allure.step("步骤3：验证结算是否成功."):
            actual = self.bp.getText(self.bp.pay_success)
            expect = "结算成功"
            assert expect in actual


    @allure.title("测试用例8：收款；")
    def test_receipt(self):

        with allure.step("步骤1：进入收银台收款；"):
            self.cdp.gathering(TestCustomerRepair.order_number, "现金")

        with allure.step("步骤2：验证所有订单是否收款成功."):
            actual = self.cdp.getText(self.cdp.all_order_success)
            expect = "所有订单都收款成功"
            assert expect in actual


if __name__ == '__main__':
    pytest.main(['-s', 'test_售后维修业务流程.py', '--alluredir', './result', '--clean-alluredir'])
    os.system("allure serve ./result")


