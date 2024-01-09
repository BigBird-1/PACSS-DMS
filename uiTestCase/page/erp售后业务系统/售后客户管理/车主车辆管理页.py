# -*- coding:utf-8 -*
# @FileName:   车主车辆管理页.py
# @Author:     刘峰
# @CreateTime: 2022/7/19 16:17

"""
    车主车辆管理页
"""
from base.base_page import BasePage


class VehicleManagePage(BasePage):

    # 车主车辆管理页URL
    url = BasePage.SERVER + "#/erp/customer/vehicleManage"

    # 车主输入框
    owner_name = ("xpath", "//label[text()='车主']/../div/div/input")
    # 查询按钮
    search_button = ("xpath", "//*[@id='app']/div/div[1]/div[2]/button[3]/span")
    # 车主列表中搜索到的车主编号
    owner_number = ("xpath", "//*[@id='app']/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/div")

    """
        车主列表
    """
    # 元素：新增车主按钮
    add_owner = ("xpath", "//span[text()='新增车主']")

    """
        车辆列表
    """
    # 车主编号输入框
    owner_number_input = ("xpath", "//*[@id='searchFormView']/form/div/div[1]/div/div/div/input")
    # 查询按钮
    select_button = ("xpath", "//*[@id='app']/div/div[3]/div[2]/button[2]/span")
    # 新增车辆按钮
    add_vehicle_button = ("xpath", "//span[text()='新增车辆']")

    # 操作：跳转到新增车辆
    def skipToAddVehicle(self, ownernumber):
        self.open(self.url, 3)
        self.input(self.owner_number_input, ownernumber, 1)
        self.click(self.select_button)
        self.click(self.add_vehicle_button, 2)

    # 获取车主编号
    def getOwnerNumber(self, ownername):
        self.open(self.url, 3)
        self.input(self.owner_name, ownername, 1)
        self.click(self.search_button)
        return self.getText(self.owner_number)

