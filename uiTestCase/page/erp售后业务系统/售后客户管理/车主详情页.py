# -*- coding:utf-8 -*
# @FileName:   车主详情页.py
# @Author:     刘峰
# @CreateTime: 2022/7/19 16:30

"""
    车主详情页：可进行新增、编辑等操作
"""
from base.base_page import BasePage

# 从车主车辆管理页跳转到新增车主、编辑车主等界面
class OwnerEditPage(BasePage):

    # 新增车主的URL
    add_owner_url = BasePage.SERVER + "#/erp/customer/ownerEdit?funCode=001&ownerNo&breadName=%E6%96%B0%E5%A2%9E%E8%BD%A6%E4%B8%BB"

    # 保存按钮
    save_button = ("xpath", "//span[text()='保存']")
    # 新增车辆按钮
    add_car_button = ("xpath", "//span[text()='新增车辆']")

    '''
        基本信息中的元素
    '''
    # 手机输入框
    phone_input = ("xpath", "//label[@for='mobile']/../div/div[1]/input")
    # 车主编号
    owner_number = ("xpath", "//label[text()='车主编号']/../div/div/input")
    # 车主姓名输入框
    owner_name_input = ("xpath", "//label[@for='ownerName']/../div/div[1]/input")
    # 性别下拉框
    gender_input = ("xpath", "//label[@for='gender']/../div/div/div/input")
    # 车主性质下拉框
    owner_property_input = ("xpath", "//label[@for='ownerProperty']/../div/div/div/input")
    # 省份下拉框
    province_input = ("xpath", "//label[@for='province']/../div/div/div/input")
    # 城市下拉框
    city_input = ("xpath", "//label[@for='city']/../div/div/div/input")
    # 区县下拉框
    district_input = ("xpath", "//label[@for='district']/../div/div/div/input")

    '''
        联系人信息中的元素
    '''
    # 自动同步车主信息按钮
    autosyns_owner_info = ("xpath", "//span[text()='自动同步车主信息']")

    '''
        保存后的提示元素
    '''
    # 提示添加成功
    add_success = ("xpath", "//p[@class='el-message__content']")

    # 操作：保存新增车主
    def addOwner(self, phone, ownername, sex, pro, city, dis):
        self.open(self.add_owner_url, 5)
        # 输入基本信息
        self.input(self.phone_input, phone, wait=1)
        self.click(self.owner_name_input, 1)
        self.input(self.owner_name_input, ownername)
        self.select(self.gender_input, sex)
        self.select(self.province_input, pro)
        self.select(self.city_input, city)
        self.select(self.district_input, dis)

        # 同步车主信息
        self.click(self.autosyns_owner_info, 1)
        # 保存
        self.click(self.save_button, 3)
