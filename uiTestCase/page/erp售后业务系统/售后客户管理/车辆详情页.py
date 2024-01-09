# -*- coding:utf-8 -*
# @FileName:   车辆详情页.py
# @Author:     刘峰
# @CreateTime: 2022/7/22 17:20

"""
    车辆详情页
"""
from base.base_page import BasePage


class VehicleEditPage(BasePage):

    # 保存按钮
    save_button = ("xpath", "//span[text()='保存']")
    # 车牌号输入框
    license_input = ("xpath", "//label[@for='license']/../div/div[1]/input")
    # VIN输入框
    vin_input = ("xpath", "//label[@for='id.vin']/../div/div[1]/input")
    # 发动机号输入框
    engineNo_input = ("xpath", "//label[@for='engineNo']/../div/div[1]/input")
    # 品牌输入框
    brand_input = ("xpath", "//label[@for='brand']/../div/div/div/input")
    # 车系输入框
    series_input = ("xpath", "//label[@for='series']/../div/div/div/input")
    # 车型输入框
    model_input = ("xpath", "//label[@for='model']/../div/div/div/input")
    # 销售日期
    salesDate_input = ("xpath", "//label[@for='salesDate']/../div/div/input")
    # 保修到期日期
    after_service_data = ("xpath", "//label[text()='保修到期日']/../div/div/input")
    # 动力类型
    powerType_input = ("xpath", "//label[@for='powerType']/../div/div/div/input")


    # 新增成功提示：新增车辆成功！
    addVehicle_success = ("xpath", "//p[@class='el-message__content']")

    # 新增车辆，前置操作：在车主车辆管理页跳转到新增车辆
    def addVehicle(self, license, vin, engineNo, brand, series, model, salesDate, powerType):
        self.click(self.license_input, 1)
        self.input(self.license_input, license, True, wait=1)

        self.input(self.vin_input, vin)

        self.click(self.engineNo_input, 1)
        self.input(self.engineNo_input, engineNo)

        self.select(self.brand_input, brand)
        self.select(self.series_input, series)
        self.select(self.model_input, model)

        self.click(self.salesDate_input)
        self.input(self.salesDate_input, salesDate)

        self.select(self.powerType_input, powerType)
        # 保存
        self.click(self.save_button, 1)

        try:
            text1 = self.getText(("xpath", "//div[@class='el-message-box__message']/p"))
            if "VIN未匹配到精友车系车型" in text1:
                self.click(("xpath", "//div[@class='el-message-box__btns']/button[2]/span"))
                self.wait(1)
        except:
            pass

        try:
            text2 = self.getText(("xpath", "//div[@class='el-message-box__message']/p"))
            if "是否要自动创建送修人" in text2:
                self.click(("xpath", "//div[@class='el-message-box__btns']/button[2]/span"))
        except:
            pass

        self.wait(3)



