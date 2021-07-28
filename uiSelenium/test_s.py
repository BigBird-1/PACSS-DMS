import unittest

from common.configHttp import RunMain
from common.Log import logger
from nose_parameterized import parameterized
import geturlParams
# import pythoncom
import readExcel
from interfaceTest.orderManagement import depositOrder

# pythoncom.CoInitialize()


base_url = geturlParams.GeturlParams().get_url()  # 调用我们的geturlParams获取我们拼接的URL
excel = readExcel.ReadExcel()
login_xls = excel.run_main('tokenCase.xlsx', 'depositOrder')  # 测试用例
login_xls2 = excel.run_main('tokenCase.xlsx', 'Sheet3')
log = logger
hh = RunMain()


class DepositOrder(unittest.TestCase):
    # def setParameters(self, num, case_name, path, query, method, result):
    #     self.num = int(num) + 1
    #     self.case_name = str(case_name)
    #     self.path = str(path)
    #     self.query = depositOrder.data  # 代码生成的数据
    #     self.method = str(method)

    # def description(self):
    #     self.case_name

    # def setUp(self):
    #     log.info(self.case_name + " 测试开始")

    # def http_r(self, path, method):
    #     url = "{}{}".format(base_url, self.path)
    #     res_dict = RunMain().run_main(self.method, url, self.query)
    #     return res_dict

    @parameterized.expand(login_xls)
    def test_case(self, num, case_name, path, query, method, result):
        num = int(num) + 1
        case_name = str(case_name)
        path = str(path)
        query = depositOrder.data  # 代码生成的数据
        method = str(method)
        try:
            if case_name == '预订单新增':
                url = "{}{}".format(base_url, path)
                res_dict = hh.run_main(method, url, query)
                self.assertEqual(res_dict['code'], 200)
                self.assertIsNotNone(res_dict['data']['orderNo'])
            if case_name == '预订单数量必填':
                del query["tsdoStr"]["quantity"]  # 将预订单数量字段从from_data中删除
                url = "{}{}".format(base_url, path)
                res_dict = hh.run_main(method, url, query)
                self.assertEqual(res_dict['code'], 400)
            if case_name == "预订单结算方式必填":
                query["tsdoStr"]["quantity"] = "1"
                del query["tsdoStr"]["payMode"]  # 将预订单结算方式字段从from_data中删除
                url = "{}{}".format(base_url, path)
                res_dict = hh.run_main(method, url, query)
                self.assertEqual(res_dict['code'], 400)
            if case_name == "预订单查询":
                query = depositOrder.params1
                url = "{}{}".format(base_url, path)
                res_dict = hh.run_main(method, url, query)
                self.assertEqual(res_dict['code'], 200)
            excel.run_main('tokenCase.xlsx', 'depositOrder', data=query, result="pass", num=num)
        except AssertionError as e:
            excel.run_main('tokenCase.xlsx', 'depositOrder', data=query, result=str(e), num=num)
            raise

    @parameterized.expand(login_xls2)
    def test_case2(self, num, case_name, path, query, method, result):
        num = int(num) + 1
        case_name = str(case_name)
        path = str(path)
        query = depositOrder.data  # 代码生成的数据
        method = str(method)
        try:
            if case_name == "预订单查询":
                query = depositOrder.params1
                url = "{}{}".format(base_url, path)
                res_dict = hh.run_main(method, url, query)
                self.assertEqual(res_dict['code'], 200)
            excel.run_main('tokenCase.xlsx', 'depositOrder', data=query, result="pass", num=num)
        except AssertionError as e:
            excel.run_main('tokenCase.xlsx', 'depositOrder', data=query, result=str(e), num=num)
            raise

    def tearDown(self):
        log.info("测试结束，输出log完结\n")


if __name__ == '__main__':
    unittest.main()






