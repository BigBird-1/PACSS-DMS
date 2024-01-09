# -*- coding:utf-8 -*
# @FileName:   test_接车制单02.py
# @Author:     刘峰
# @CreateTime: 2022/8/1 17:33

"""
    接车制单测试用例组：
        9、员工车校验；    10、商品车维修申请；     11、取消和新建；   12、批量删除和批量调整收费分区；  13、解锁出清材料；
"""


import pytest, allure

from data_driver.getData import getYaml
from data_driver.randomData import *
from page.erp售后业务系统.售后客户管理.车主详情页 import OwnerEditPage
from page.erp售后业务系统.售后客户管理.车辆详情页 import VehicleEditPage
from page.erp售后业务系统.维修业务.接车制单详情页 import CustomerReceptionEditMainPage
from page.erp售后业务系统.维修业务.接车制单页 import CustomerReceptionPage
from page.erp配件系统.配件管理.配件出库管理.编辑维修领料页 import EditRepairOutPage
from page.erp配件系统.配件管理.配件出库管理.配件维修领料页 import RepairOutPage


@allure.feature("接车制单功能测试")
class TestCustomerReception02:

    @allure.title("接车制单初始化方法02")
    def test_begin(self, login):
        TestCustomerReception02.oep = OwnerEditPage(login)
        TestCustomerReception02.vep = VehicleEditPage(login)
        TestCustomerReception02.crp = CustomerReceptionPage(login)
        TestCustomerReception02.crep = CustomerReceptionEditMainPage(login)
        TestCustomerReception02.rop = RepairOutPage(login)
        TestCustomerReception02.erop = EditRepairOutPage(login)


    @allure.title("测试用例09：员工车校验；")
    def test_checkStaffCar(self):

        with allure.step("步骤1：跳转到新增接车制单页面；"):
            self.crp.skipToAdd()

        with allure.step("步骤2：选择员工车牌号，点击员工车校验；"):
            self.crep.checkStaffCar("鄂A44578")

        with allure.step("步骤3：验证校验是否是员工车；"):
            actual = self.crep.getText(self.crep.staff_car_success)
            expect = "校验为员工车"
            assert expect in actual

            # 后置处理，关闭编辑接车制单页
            self.crep.click(self.crep.goback_button)


    @allure.title("测试用例10：商品车维修申请；")
    @pytest.mark.parametrize("dicts", getYaml(r'./data/erp售后业务系统/新增接车制单.yaml'))
    def test_applyForMaintain(self, dicts):

        with allure.step("步骤1：跳转到接车制单新增页，保存商品车；"):
            self.crp.skipToAdd()
            self.crep.addAustomerReception(license='无牌照', servicepeople=dicts['服务专员'],
                    insurancetype=dicts['险种类型'], insurancecompany=dicts['保险公司'],
                    project=dicts['收费区分'], vin='LBEADADC4LY622185')
            # 取消同步到DMS
            self.crep.cancleSyscDMS()

        with allure.step("步骤2：点击商品车维修申请，填写信息后保存；"):
            self.crep.applyForMaintain("刘峰", "商品车申请的备注")

        with allure.step("步骤3：验证申请是否成功"):
            actual = self.crep.webDriverWait(self.crep.apply_success).text
            expect = "申请成功"
            assert expect in actual

            # 后置处理，关闭编辑接车制单页
            self.crep.click(self.crep.goback_button)


    @allure.title("测试用例11：取消和新建；")
    def test_cancleAndNew(self):

        with allure.step("步骤1：跳转到新增接车制单页；"):
            self.crp.skipToAdd()

        with allure.step("步骤2：点击取消和新建；"):
            self.crep.click(self.crep.cancle_order_button)
            self.crep.click(self.crep.new_button)

        with allure.step("步骤3：验证新建是否成功；"):
            actual = self.crep.locate(self.crep.license_select_button).get_attribute("type")
            expect = "button"
            assert actual == expect

            # 后置处理，关闭编辑接车制单页
            self.crep.click(self.crep.goback_button)


    @allure.title("测试用例12：批量删除和批量调整收费分区；")
    @pytest.mark.parametrize("dicts1", getYaml(r"./data/erp售后业务系统/新增车主.yaml"))
    @pytest.mark.parametrize("dicts2", getYaml(r'./data/erp售后业务系统/新增车辆.yaml'))
    def test_batchAdjustCharge(self, dicts1, dicts2):

        with allure.step("步骤1：新增车主车辆；"):
            self.oep.addOwner(random_mobile(), random_name(), dicts1['性别'], dicts1['省份'], dicts1['城市'], dicts1['区县'])

            self.oep.click(self.oep.add_car_button)

            TestCustomerReception02.license = random_car()
            self.vep.addVehicle(license=TestCustomerReception02.license, vin=random_vin(), engineNo=dicts2['发动机编号'],
                                brand=dicts2['品牌'], series=dicts2['车系'], model=dicts2['车型'], salesDate=dicts2['销售日期'],
                                powerType=dicts2['动力类型'])

        with allure.step("步骤2：新增接车制单，添加多条维修项目和维修材料；"):
            self.crp.skipToAdd()
            self.crep.addManyAustomerReception(license=TestCustomerReception02.license, servicepeople="超级管理员",
                                               partsnumber='.641010R500')

        with allure.step("步骤3：对维修项目进行批量删除和批量调整收费分区操作；"):
            self.crep.batchAdjustCharge("客户付费")

            # 后置处理，关闭编辑接车制单页
            self.crep.click(self.crep.goback_button)


    @allure.title("测试用例13：解锁出清材料；")
    @pytest.mark.parametrize("dicts", getYaml(r"./data/erp售后业务系统/新增接车制单.yaml"))
    def test_unlockClearMaterials(self, dicts):

        with allure.step("步骤1：新增接车制单；"):
            self.crp.skipToAdd()
            self.crep.addAustomerReception(license=TestCustomerReception02.license, servicepeople=dicts['服务专员'], insurancetype=dicts['险种类型'],
                                           insurancecompany=dicts['保险公司'], project=dicts['收费区分'], isMaterial=True,
                                           partsnumber=dicts['配件代码'], maintaintype=dicts['事故维修'], lossmoney=5000)
            # 取消同步到DMS
            self.crep.cancleSyscDMS()
            # 关闭维修制单新增页面
            self.crep.click(self.crep.goback_button)
            # 获取工单号
            TestCustomerReception02.order_number = self.crp.getOrderNumber()

        with allure.step("步骤2：配件维修领料，出库并出清；"):
            self.rop.skipToMaintainPick(TestCustomerReception02.order_number)
            self.erop.clearance("周海波")
            # 关闭编辑维修领料页面
            self.crep.click(self.crep.goback_button)

        with allure.step("步骤3：再回到接车制单编辑页，点击解锁出清材料；"):
            self.crp.skipToEdit(TestCustomerReception02.order_number)
            self.crep.click(self.crep.unlock_clear_materials)

        with allure.step("步骤4：验证解锁是否成功；"):
            actual = self.crep.webDriverWait(self.crep.unlock_clear_success).text
            expect = "解锁成功"
            assert expect in actual


