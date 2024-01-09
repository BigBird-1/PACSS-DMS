# -*- coding:utf-8 -*
# @FileName:   车间维修管理页.py
# @Author:     刘峰
# @CreateTime: 2022/7/25 16:40

from base.base_page import BasePage


class WorkshopMaintenancePage(BasePage):

    # URL
    url = BasePage.SERVER + "#/erp/repair/workshopMaintenanceDispatchList"

    # 开工按钮
    start_work_button = ("xpath", "//span[text()='开工']")
    # 完工按钮
    complete_button = ("xpath", "//span[text()='完工']")

    """
        开工窗口
    """
    # 全部开工按钮
    all_starts_button = ("xpath", "//span[text()='全部开工']")
    # 返回按钮
    back_button = ("xpath", "//span[text()='返回']")

    """
        完工窗口
    """
    # 全部完工按钮
    all_complete_button = ("xpath", "//span[text()='全部完工']")
    # 返回按钮
    back_button2 = ("xpath", "//span[text()='返回']")

    # 全部完工后操作成功提示
    operator_success = ("xpath", "//p[@class='el-message__content']")


    # 开工
    def startWork(self, ordernumber):
        self.open(self.url, 3)
        # 选择工单
        self.clickByText(ordernumber)
        # 点击开工
        self.click(self.start_work_button, 2)

        self.click(self.all_starts_button, 2)
        self.click(self.back_button)

    # 完工，前置条件是已开工，且进入到车间维修管理页
    def completeWork(self):
        self.click(self.complete_button)
        self.wait(2)
        self.click(self.all_complete_button)
        self.wait(3)
