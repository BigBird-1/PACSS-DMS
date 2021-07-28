import json
import unittest
import requests
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
import ast
# pythoncom.CoInitialize()
from common.HTMLTestRunnerEN import HTMLTestRunner

from getpathInfo import get_path

base_url = geturlParams.GeturlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.ReadExcel().read_xls('tokenCase.xlsx', 'tokenCase')  # 测试用例


@paramunittest.parametrized(*login_xls)
class NewBrand(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = ast.literal_eval(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")

    def test_case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        url = "{}{}".format(base_url, self.path)
        info = RunMain().run_main(self.method, url, self.query)
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == '品牌新增':
            self.assertEqual(ss['message'], "已存在该品牌代码")
        if self.case_name == '品牌重复新增':  # 同上
            self.assertEqual(ss['message'], "已存在该品牌代码")




