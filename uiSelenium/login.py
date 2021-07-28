import logging
import xlrd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from hx_erp.hx_config.config import Config
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger()
# 调用配置的日志
# Config().set_up()


class LoginCs(object):
    def __init__(self):
        self.login_path = 'C:\\Users\cpr264\Desktop\自动化模板\测试线批量登录模板.xls'
        self.sheet_name = '多账号'
        self.driver = None

    def slide(self):
        """滑动解锁"""
        div = self.driver.find_element_by_xpath("//form[@class='el-form']/div[4]/div/div[3]")
        action = ActionChains(self.driver)
        action.click_and_hold(div).perform()
        action.move_to_element_with_offset(to_element=div, xoffset=475, yoffset=0).release().perform()

    def logout(self):
        """从主页面退出系统到登录界面"""
        self.driver.find_element_by_xpath(".//div[@id='exit']/div").click()
        self.driver.find_element_by_xpath(".//a[@title='退出恒信管理系统']/img[@alt='退出系统']").click()
        sleep(0.5)
        self.driver.switch_to_alert().accept()
        sleep(1)

    def xpath_expression(self, num, code):
        """input框公用表达式"""
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[{}]/div/div/input".format(num)).clear()
        self.driver.find_element_by_xpath("//form[@class='el-form']/div[{}]/div/div/input".format(num)).send_keys(code)

    def login1(self):
        """一次登录"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)  # 隐性等待3秒
        account = ['HD340400', 'A08D', 'hxqc2020!']
        try:
            self.driver.get("https://dms.t.hxqcgf.com/#/sso/login")
            self.driver.find_element_by_xpath("//form[@class='el-form']/div[1]/div/div/div/input").clear()
            self.driver.find_element_by_xpath("//form[@class='el-form']/div[1]/div/div/div/input").send_keys(account[0])
            self.driver.find_element_by_xpath("//form[@class='el-form']/div[1]/div/div/div/input").send_keys(Keys.TAB)
        except Exception as e:
            logger.info('%s DMS地址请求失败或地址不正确' % e)
            self.driver.close()
            return
        self.xpath_expression(2, account[1])
        self.xpath_expression(3, account[2])
        try:
            self.slide()
            self.driver.find_element_by_xpath("//form[@class='el-form']/div[5]/button").click()
            # logger.info('HD340400-Admin-hxqc2018！登录成功')
            return self.driver
        except:
            self.driver.close()
            logger.info('滑动失败 未找到元素verify-move-block')
            self.login1()

    def login2(self):
        """多次登录"""
        self.login1()
        self.logout()
        for item in self.read_account():
            sleep(0.5)
            self.xpath_expression('code', item['单店编码'])
            self.xpath_expression('uid', item['账号'])
            self.xpath_expression('pswd', item['密码'])
            self.slide()
            self.driver.find_element_by_xpath(".//button[@id='button']").click()
            sleep(0.5)
            try:
                if self.driver.find_element_by_id('error_info'):
                    logger.info('%s-%s-%s 登录失败！！！' % (item['单店编码'],item['账号'],item['密码']))
                    continue
            except:
                self.driver.find_element_by_xpath(".//img[@alt='ERP']").click()
                logger.info('%s-%s-%s 登录成功' % (item['单店编码'], item['账号'], item['密码']))
                self.logout()
        # 关闭当前窗口
        self.driver.close()

    def read_account(self):
        """读取多账号存入字典并添加到列表"""
        e_u_ps = []
        # 打开excel工作簿
        tem_excel = xlrd.open_workbook(self.login_path)
        # 打开工作表
        tem_sheet = tem_excel.sheet_by_name(self.sheet_name)
        # 获取sheet1工作表里的行数，列数
        row_nums = tem_sheet.nrows
        col_nums = tem_sheet.ncols
        # 获取第一行所有内容,如果括号中1就是第二行
        keys = tem_sheet.row_values(0)
        # 读取单店编号/账号/密码 并保存
        for i in range(1, row_nums):
            eup_dict = {}
            for j in range(col_nums):
                # 获取单元格数据类型
                c_type = tem_sheet.cell(i, j).ctype
                # 获取单元格数据
                c_cell = tem_sheet.cell_value(i, j)
                # 如果单元格数据为整行则切掉点零
                if c_type == 2 and c_cell % 1 == 0:
                    c_cell = int(c_cell)
                # 将一行数据添加到字典中
                eup_dict[keys[j]] = c_cell
            # 将字典添加到列表中
            e_u_ps.append(eup_dict)
        return e_u_ps


