# from urllib.parse import urlencode
# from dms_cs.get_token import get_token
# from dms_cs.data_generate.brand_data import new_brand_data
# import requests


# 带token的headers
# headers = get_token()
#
#
# # 新增品牌-保存
# url = "http://10.0.15.130:31099/gms/gmsBrand/save"
# # 构建请求数据
# brand_data = new_brand_data()
# data = urlencode(brand_data).encode()  # 暂不清楚为啥要这样编码就可以传
# res = requests.post(url, headers=headers, data=data)
# print(res.json())
# res = res.json()
# assert res["code"] == 200
# assert res["message"] == "添加成功!"




# # 列表查询
# url = "http://10.0.15.130:31099/gms/gmsBrand/list"
# # 准备查询条件
# search_data = {
#     "brandKeywords": brand_data["data"]["brandCode"]
# }
# # 准备查询参数
# params = {
#     "limit": 10,
#     "offset": 0,
#     "searchData": search_data,
#     "useMock": "false"
# }
# params = urlencode(params).encode("utf-8")
# res = requests.get(url, headers=headers, params=params)
# print(res.content.decode())

# -*- coding:utf-8 -*-
# import unittest
# import paramunittest
# import time
# import ast
#
# list = [['品牌新增', '/gms/gmsBrand/save', '{\n            "data": {"brandCode": "PPPD432", \n                     "brandName": "时间111",  \n                     "coefficient": "1.13",  \n                     "isSale": 12781001,  \n                     "isAfterSale": 12781001,  \n                     "id": {"brandCode": "PPPD432"},\n                     "vendorCode": "CSBM-CS2020",  \n                     "vendorName": "changjia-2020", \n                     "enableStdLabour": 12781001,  \n                     "facRepairType": "changjia-cs2020"},  \n            "useMock": "false",\n            "isNew": "1"\n    }', 'post'], ['品牌新增', '/gms/gmsBrand/save', '{\n            "data": {"brandCode": "GGGD432", \n                     "brandName": "shijian111",  \n                     "coefficient": "1.13",  \n                     "isSale": 12781001,  \n                     "isAfterSale": 12781001,  \n                     "id": {"brandCode": "GGGD432"},\n                     "vendorCode": "CSBM-CS2020",  \n                     "vendorName": "changjia-2020", \n                     "enableStdLabour": 12781001,  \n                     "facRepairType": "changjia-cs2020"},  \n            "useMock": "false",\n            "isNew": "2"\n    }', 'post']]
#
#
# @paramunittest.parametrized(*list)
# class TestDemo(unittest.TestCase):
#     def setParameters(self, case_name, path, query, method):
#         '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
#         # self.user = user
#         # self.user = psw
#         # self.result = result
#         self.case_name = str(case_name)
#         self.path = str(path)
#         self.query = ast.literal_eval(query)
#         self.method = str(method)
#
#     def testcase(self):
#         print("开始执行用例：--------------")
#         time.sleep(0.5)
#         print("输入用户名：%s" % self.case_name)
#         print("输入密码：%s" % self.path)
#         print("期望结果：%s " % self.query)
#         print(type(self.query))
#         print("实际结果：%s " % self.method)
#         time.sleep(0.5)
#         self.assertTrue(self.method == "post")
#
#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)
# import random
# import string
#
# vin = ''.join(random.sample(string.ascii_uppercase + string.digits, 17))
# print(vin)

























