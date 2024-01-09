from common.baseMethod import BaseMethod


class CostAddPage(BaseMethod):
    # 费用申请页地址
    add_cost_url = BaseMethod.BASE_URL + "/#/oa/finance/expense/expenseDetail/add/add"
    # 保存按钮
    save_button = ("xpath", "//span[text()='保存']")
    # 费用项目下拉框
    fee_project_input = ("xpath", "//label[@for='fee_project']/div/div/div/input")
    # 本次申请开支额
    fee_askmoney_input = ("xpath", "//label[@for='fee_askmoney']/div/div/input")
    # 申请事由
    fee_askreason_input = ("xpath", "//label[@for='fee_askreason']/div/div/input")
    # 附件
    attachment_ids_button = ("xpath", "//span[text()='附件']")
    up_file_button = ("xpath", "//span[text()='上传文件']")
    file_input = ("name", "file")
    # 保存成功
    is_submit = ("xpath", "//p[contain(text(), '是否提交审核?')]")

    def add_cost(self):
        self.select(self.fee_project_input, "劳动保护费")
        self.input(self.fee_askmoney_input, 0)
        self.input(self.fee_askreason_input, "举杯邀明月，对影成三人，月既不解饮，影徒随我身")

        self.click(self.save_button, wait=0.5)







