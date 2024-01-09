# -*- coding:utf-8 -*
# @FileName:   编辑维修领料页.py
# @Author:     刘峰
# @CreateTime: 2022/7/25 15:35

from base.base_page import BasePage


class EditRepairOutPage(BasePage):

    # 修改领料人按钮
    edit_pick_people = ("xpath", "//span[contains(text(), '修改领料人')]")
    # 出库按钮
    out_bank = ("xpath", "//div[@class='search-form-content']/button[10]")

    """
        请选择领料人窗口
    """
    # 领料人下拉框
    pick_people_input = ("xpath", "//label[@for='receiver']/../div/div/div/input")
    # 确定按钮
    confirm_button = ("xpath", "//div[@class='el-dialog__body']/div[3]/div/div/button[1]/span")


    # 出库成功提示
    out_bank_success = ("class name", "el-message__content")

    """
        出库确认窗口
    """
    # 配件是否全部出库字段
    if_out_storage = ("xpath", "//label[@for='choosePartAllOut']")
    # 配件是否全部出库下拉框
    out_storage_input = ("xpath", "//label[@for='choosePartAllOut']/../div/div/div/input")
    # 确定按钮
    confirm_out = ("xpath", "//div[@class='info']/div/div/button[1]")


    # 编辑维修领料，前置条件：已跳转到编辑维修领料页面
    def editMaintainPick(self, people):
        # 点击修改领料人
        self.click(self.edit_pick_people)
        self.select(self.pick_people_input, people)
        self.click(self.confirm_button)
        self.wait(1)
        # 点击出库
        self.click(self.out_bank)
        self.wait(3)


    # 编辑维修领料并出清，前置条件：已跳转到编辑维修领料页面
    def clearance(self, people):
        self.editMaintainPick(people)
        # 如果弹出出清窗口（即出库确认窗口），全部出清
        try:
            text = self.webDriverWait(self.if_out_storage).text
            if "配件是否全部出库" in text:
                self.select(self.out_storage_input, "是")
                self.click(self.confirm_out)
                self.wait(3)
        except:
            pass