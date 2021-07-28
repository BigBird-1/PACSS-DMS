import random
from urllib.parse import urlencode

from dataGenerated import randomData
from dms_cs.get_token import get_token
import requests


class SalesDepositOrder(object):
    def __init__(self):
        self.headers = get_token()
        self.order_no = None

    def new_order(self):
        # 预订单新增
        url = "http://10.0.15.134:9999/sales/salesDepositOrder/save"
        # 准备请求数据
        data = urlencode(self.new_data()).encode("utf-8")
        # 发送请求
        res = requests.post(url, headers=self.headers, data=data)
        # 解析响应
        print(res.json())
        # 返回预订单号
        try:
            self.order_no = res.json()["data"]["orderNo"]
        except KeyError:
            print('创建订单失败')

    def edit_order(self):
        # 预订单编辑
        url = "http://10.0.15.134:9999/sales/salesDepositOrder/save"
        # 准备请求数据
        order_data = self.new_data()
        # 修改数据
        order_data["tsdoStr"]["id"]["orderNo"] = self.order_no
        order_data["tsdoStr"]["depositAmount"] = "6000.00"
        data = urlencode(order_data).encode("utf-8")
        # 发送请求
        res = requests.post(url, headers=self.headers, data=data)
        # 解析响应
        print(res.json())

    def search_order(self):
        # 查询
        url = "http://10.0.15.134:9999/sales/salesDepositOrder/searchDepositList"
        # 准备查询条件
        params = urlencode(self.search_params()).encode("utf-8")
        # 发送请求
        res = requests.get(url, headers=self.headers, params=params)
        # 解析响应
        print(res.json())

    def excel_order(self):
        # 导出
        url = "http://10.0.15.134:9999/sales/salesDepositOrder/exportExcel"
        data = urlencode(self.excel_data()).encode()
        # 发送请求
        res = requests.post(url, headers=self.headers, data=data)
        print(res.status_code)

    def commit_audit(self):
        url = "http://10.0.15.134:9999/sales/salesDepositOrder/commitAudit"
        data = {
            "orderNo": self.order_no
        }
        data = urlencode(data).encode()
        requests.post(url, headers=self.headers, data=data)

    def new_data(self):
        vin = randomData.random_vin()
        data = {}
        params = {
            "searchData": {"funCode": "006"}
        }
        params = urlencode(params).encode("utf-8")
        url = "http://10.0.15.134:9999/sales/salesDepositOrder/queryPoCustomer"
        ss = requests.get(url, params=params, headers=self.headers).json()
        if ss["data"]["total"] != 0:
            content = random.choice(ss["data"]["list"])
            print(content)
            try:
                customer_phone = content["customerPhone"]
            except KeyError:
                customer_phone = content["contactorMobile"]
            data = {
                "tsdoStr": {
                    "id": {"entityCode": "HD340400",
                           "orderNo": ""},

                    "customerName": content["customerName"],  # 潜客姓名*
                    "customerNo": content["customerNo"],  # 潜客编号*
                    "orderType": "92071001",
                    "ctCode": content["ctCode"],  # 证件类型*
                    "certificateNo": content["certificateNo"],  # 证件号码*
                    "customerPhone": customer_phone,  # 手机号*
                    "customerAddress": content["address"],  # 地址*

                    "productCode": "FPZ-004199 FWS-001460 FNS-001111",  # 产品代码*
                    "factoryModelId": "96690000002739",  # 厂家车型代码*
                    "factoryModelName": "Q50L 2.0T进取版",  # 厂家车型名称*
                    "brand": "000",  # 品牌代码*
                    "series": "FCX-001069",  # 车系代码*
                    "model": "FXH-004199",  # 车型代码*
                    "config": "FPZ-004199",  # 配置代码*
                    "color": "FWS-001460",  # 颜色代码*
                    "directivePrice": "100000.00",  # 销售指导价*
                    "vin": vin,

                    "quantity": "1",  # 数量*
                    "payMode": "10251001",  # 结算方式*
                    "soldBy": "88880000000157",  # 销售顾问代码*
                    "soldByDesc": "linjinjun",  # 销售顾问姓名*
                    "vehiclePrice": "100000.00",  # 车价*
                    "depositAmount": "3000.00",  # 订金*
                    "otherAmount": "10000.00",  # 预估总毛利（含佣金）*

                    "decorationService": "测试-销售装潢项目",
                    "decorationAmount": "111.11",
                    "insuranceService": "测试-保险项目",
                    "insuranceAmount": "222.22",
                    # "loanService": "2",
                    "loanAmount": "333.33",
                    # "agencyService": "3",
                    "agencyAmount": "444.44",
                    "otherItem": "测试-其他项目",
                    "otherItemAmount": "555.55",
                    "otherService": "测试-其他政策（oa审核）"}
            }
        return data

    @staticmethod
    def excel_data():
        excel_data = {
            "header": ["订单编号", "潜客编号", "单据状态", "上传预订协议", "是否转销售订单", "销售订单编号",
                       "客户名称", "客户来源", "到店次数", "销售顾问", "手机号码", "车系", "车型", "配置", "颜色",
                       "销售指导价", "车价", "订金", "销售装潢金额", "保险金额", "咨询服务费", "劳务服务费",
                       "其它金额", "开单日期", "完成日期", "预订单取消原因"],
            "key": ["orderNo", "customerNo", "soStatusDesc", "hasBarcode", "hasSalesOrder", "soNo", "customerName",
                    "sourceName", "arriveNum", "soldBy", "customerPhone", "series", "model", "config", "color",
                    "directivePrice", "vehiclePrice", "depositAmount", "decorationAmount", "insuranceAmount",
                    "loanAmount", "agencyAmount", "otherItemAmount", "createDate", "finishDate", "cancelReason"],
            "searchData": {},
            "fileName": "预订单"
        }
        return excel_data

    def search_params(self):
        search_data = {
            "soStatus": "",  # 单据状态
            "businessType": "",  # 预订单类型
            "isToSalesOrder": 12781002,  # 是否转销售订单
            "keyWord": self.order_no  # 关键字
        }
        search_params = {
            "limit": "10",
            "offset": "0",
            "useMock": "false",
            "searchData": search_data
        }
        return search_params


if __name__ == '__main__':
    sales_deposit = SalesDepositOrder()
    # sales_deposit.new_order()
    # sales_deposit.search_order()
    sales_deposit.edit_order()
    # sales_deposit.search_order()


























