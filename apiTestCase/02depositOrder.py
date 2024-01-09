import unittest
from common.configHttp import http_r
from common.Log import logger
import paramunittest
import geturlParams
# import pythoncom
import readExcel
from apiTest.orderManagement.depositOrder import deposit_order
from readConfig import read_config


# pythoncom.CoInitialize()


base_url = read_config.get_http("base_url")  # 调用我们的geturlParams获取我们拼接的URL
excel = readExcel.ReadExcel()
login_xls = excel.run_main('tokenCase.xlsx', 'depositOrder')  # 测试用例
log = logger


@paramunittest.parametrized(*login_xls)
class DepositOrder(unittest.TestCase):
    def setParameters(self, num, case_name, path, query, method, result):
        self.num = int(num) + 1
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = deposit_order.new_save("居民身份证", phone="18698741001")  # 代码生成的数据
        self.method = str(method)

    # def description(self):
    #     self.case_name

    def setUp(self):
        self._testMethodDoc = self.case_name  # 用例方法描述自定义为用例名称
        log.info(self.case_name + " 测试开始")

    def http_r(self):
        url = "{}{}".format(base_url, self.path)
        print(url)
        res_dict = http_r.run_main(self.method, url, data=self.query, is_json=1)
        return res_dict

    def test_case(self):
        try:
            if self.case_name == '预订单新增':
                res_dict = self.http_r()
                print(res_dict["code"])
                self.assertEqual(res_dict['code'], 200)
                self.assertIsNotNone(res_dict['data']['orderNo'])
            if self.case_name == "预订单结算方式必填":
                del self.query["salesDeptositOrder"]["payMode"]  # 将预订单结算方式字段从from_data中删除
                res_dict = self.http_r()
                self.assertEqual(res_dict['code'], 400)
            excel.run_main('tokenCase.xlsx', 'depositOrder', data=self.query, result="pass", num=self.num)
        except AssertionError as e:
            excel.run_main('tokenCase.xlsx', 'depositOrder', data=self.query, result=str(e), num=self.num)
            raise

    def tearDown(self):
        log.info("测试结束，输出log完结\n")









