from common.baseMethod import BaseMethod
from common import Log


log = Log.logger


class LoginPage(BaseMethod):
    # 登录页URL
    url = BaseMethod.BASE_URL + "/#/sso/login"

    # 元素：切换登录
    switch_button = ("xpath", "//span[text()='切换登录']")
    # 元素：公司代码输入框
    entity_code_input = ("xpath", "//input[@placeholder='请输入公司代码']")
    # 元素：用户名输入框
    user_input = ("xpath", "//input[@placeholder='请输入用户名/手机号']")
    # 元素：密码输入框
    password_input = ("xpath", "//input[@placeholder='请输入密码']")
    # 元素：登录按钮
    login_button = ("xpath", "//span[contains(text(), '线版本】 登')]")

    def login_c(self, entity_code, username, password):
        """登录操作"""
        self.open(self.url)
        self.click(self.switch_button)
        self.input(self.entity_code_input, entity_code)
        self.input(self.user_input, username)
        self.input(self.password_input, password)
        self.click(self.login_button)

    # def read_account(self):
    #     """读取多账号存入字典并添加到列表"""
    #     e_u_ps = []
    #     # 打开excel工作簿
    #     tem_excel = xlrd.open_workbook(self.login_path)
    #     # 打开工作表
    #     tem_sheet = tem_excel.sheet_by_name(self.sheet_name)
    #     # 获取sheet1工作表里的行数，列数
    #     row_nums = tem_sheet.nrows
    #     col_nums = tem_sheet.ncols
    #     # 获取第一行所有内容,如果括号中1就是第二行
    #     keys = tem_sheet.row_values(0)
    #     # 读取单店编号/账号/密码 并保存
    #     for i in range(1, row_nums):
    #         eup_dict = {}
    #         for j in range(col_nums):
    #             # 获取单元格数据类型
    #             c_type = tem_sheet.cell(i, j).ctype
    #             # 获取单元格数据
    #             c_cell = tem_sheet.cell_value(i, j)
    #             # 如果单元格数据为整行则切掉点零
    #             if c_type == 2 and c_cell % 1 == 0:
    #                 c_cell = int(c_cell)
    #             # 将一行数据添加到字典中
    #             eup_dict[keys[j]] = c_cell
    #         # 将字典添加到列表中
    #         e_u_ps.append(eup_dict)
    #     return e_u_ps




