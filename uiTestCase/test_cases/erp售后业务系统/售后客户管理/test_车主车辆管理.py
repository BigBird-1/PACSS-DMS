# -*- coding:utf-8 -*
# @FileName:   test_车主车辆管理.py
# @Author:     刘峰
# @CreateTime: 2022/7/23 9:35

"""
    车主车辆管理用例组：
        1、新增车主； 2、新增车辆；
"""
import pytest, allure

from data_driver.randomData import *
from data_driver.getData import *
from page.erp售后业务系统.售后客户管理.车主详情页 import OwnerEditPage
from page.erp售后业务系统.售后客户管理.车主车辆管理页 import VehicleManagePage
from page.erp售后业务系统.售后客户管理.车辆详情页 import VehicleEditPage


@allure.feature("车主车辆管理测试")
class TestVehicleManage:

    @allure.title("车主车辆管理初始化方法")
    def test_begin(self, login):
        TestVehicleManage.oep = OwnerEditPage(login)
        TestVehicleManage.vep = VehicleEditPage(login)
        TestVehicleManage.vmp = VehicleManagePage(login)


    @allure.title("测试用例1：新增车主；")
    @pytest.mark.parametrize("dicts", getExcel(r"./data/erp售后业务系统/新增车主.xlsx"))
    def test_addOwner(self, dicts):

        with allure.step("步骤1：进入新增车主界面，填入必填信息，点击保存；"):
            name = random_name()
            self.oep.addOwner(random_mobile(), name, dicts['性别'], dicts['省份'], dicts['城市'], dicts['区县'])

        with allure.step("步骤2：验证新增车主是否成功."):
            actual = self.oep.getText(self.oep.add_success)
            expect = dicts['期望值']
            assert expect in actual

            # 后置处理，获取车主编号
            TestVehicleManage.owner_number = self.vmp.getOwnerNumber(name)


    @allure.title("测试用例2：新增车辆；")
    @pytest.mark.parametrize("dicts", getYaml(r'./data/erp售后业务系统/新增车辆.yaml'))
    def test_addVehicle(self, dicts):

        with allure.step("步骤1：根据车主编号，跳转到新增车辆界面，"):
            self.vmp.skipToAddVehicle(TestVehicleManage.owner_number)

        with allure.step("步骤2：填写车辆信息，保存；"):
            self.vep.addVehicle(license=random_car(), vin=random_vin(), engineNo=dicts['发动机编号'], brand=dicts['品牌'],
                                series=dicts['车系'], model=dicts['车型'], salesDate=dicts['销售日期'], powerType=dicts['动力类型'])

        with allure.step("步骤3：验证车辆是否新增成功."):
            actual = self.vep.getText(self.vep.addVehicle_success)
            expect = dicts['期望值']
            assert expect in actual
