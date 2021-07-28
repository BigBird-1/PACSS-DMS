import time
import datetime
import random
from dataGenerated import randomData
from common.configHttp import http_r
from interfaceTest.initialization import initial
from interfaceTest.constants import shipping_urls, shipping_cars
from readConfig import read_config
from common import Log


log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class ShippingCar(object):
    def __init__(self):
        res1 = http_r.run_main('get', url=shipping_urls["新增页面初始化"], name="在途新增页面初始化")
        self.shipment_code = res1['data']['shipmentList'][0]['statusCode']  # 发运地代码
        self.tax = res1['data']['tax']

    @staticmethod
    def faker_flag(vin=None):
        vin_list = []
        table_json = []
        if vin:
            vin_list.append(vin)
        else:
            for i in range(shipping_cars):
                vin = randomData.random_vin()
                vin_list.append(vin)
        for vin in vin_list:
            table_dict = {}
            params = {"vin": vin}
            res = http_r.run_main('get', url=shipping_urls["检查是否虚销"], data=params, name="检查是否虚销")
            log.info(res)
            table_dict["vin"] = vin
            table_dict["engineNo"] = "EQ8100Q1{}".format(vin[:5])
            table_dict["certificateNumber"] = "SQ67IJ692"
            table_dict["fakeFlag"] = 12781002
            table_dict["fakeDate"] = ""
            if res['data']['code'] == 1:
                table_dict["fakeFlag"] = 12781001
                table_dict["fakeDate"] = res['data']['fakeDate']
            table_json.append(table_dict)
        data = {"tableJson": table_json}
        res = http_r.run_main('post', url=shipping_urls["是否存在库存"], data=data, name="是否存在库存")
        log.info(res)
        return vin_list, table_json

    def new_save(self, table_json):
        product_data = initial.vehicle_main(read_config.get_http("productCode"))  # 产品代码
        # product_data = initial.vehicle_main("FPZ-008339 FWS-001402 FNS-000046")  # 产品代码
        # -----------采购价格，税率，不含税采购价，税额-----------------------------------------------------------------
        purchase_price = int(product_data["directivePrice"]*0.92)
        no_tax_vehicle_cost = purchase_price / (1 + self.tax)
        tax_amount = purchase_price - no_tax_vehicle_cost
        # -----------------平均在途,周转天数----------------------------------------------------------------------------
        params = {
            "productCode": product_data["productCode"]}
        res2 = http_r.run_main('get', url=shipping_urls["标准在途天数"], data=params, name="标准在途天数")
        avg_transit = res2["data"]["avgTransitDays"]
        res3 = http_r.run_main('get', url=shipping_urls["标准周转天数"], data=params, name="标准周转天数")
        avg_turnover = res3["data"]["avgTurnoverDays"]
        # --------------构造请求数据------------------------------------------------------------------------------------
        data = {
            "paramJson": {"businessType": 13071002,  # 业务类型*
                          "vendorCode": "888888888888",  # 供应商代码*
                          "vendorName": "OEM",  # 供应商名称*
                          "isLargeConsumer": 12781002,  # 是否大客户*

                          "productCode": product_data["productCode"],  # 产品代码*
                          "factoryModelName": product_data["factoryModelName"],  # 厂家车型*
                          "factoryModelId": product_data["factoryModelId"],
                          "directivePrice": product_data["directivePrice"],  # 销售指导价 （带出）
                          "factoryDirectivePrice": product_data["oemDirectivePrice"],  # 厂家指导价  （带出）
                          "factoryModelCode": "Chang-jia-车型code",  # 厂家车型代码

                          "shipmentCode": self.shipment_code,  # 发运地代码
                          "shipmentMode": 14581001,  # 运输方式代码

                          "avgTransitDays": avg_transit,  # 标准在途天数
                          "avgTurnoverDays": avg_turnover,  # 标准周转天数

                          "standardCommission": 25846,  # 提车佣金
                          "deliveryCommission": 0,

                          "realOemPickUpDate": current_date + "T16:00:00.000Z",

                          "id": {"entityCode": "", "vin": ""},
                          "sourceCode": "1002",  # 资金来源*
                          "sourceCodeDesc": "银行融资",
                          "dischargeStandard": 30101009,  # 排放标准*
                          "vehicleType": 80151001,  # 车辆类型*
                          "purchasePrice": str(purchase_price),  # 采购价格*
                          "tax": self.tax,  # 税率*
                          "notaxVehicleCost": str(no_tax_vehicle_cost),  # 不含税采购价* （自动算）
                          "taxAmount": str(tax_amount),  # 税额（自动算）
                          "shippingDate": current_date,  # 发车日期
                          "arrivingDate": current_date,  # 预计到货日
                          "certificateLocated": "台湾省",  # 合格证所在地
                          "poNo": ""},  # 采购计划单号
            "tableJson": table_json,
            "standardCommission": 25846,  # 标准提车佣金
            "deliveryCommission": 0,  # 标准交车佣金
            "isAdd": "true"
        }
        for key in list(data["paramJson"].keys()):
            if not data["paramJson"][key]:
                del data["paramJson"][key]
        res = http_r.run_main("post", url=shipping_urls["在途车保存"], data=data, name="在途车保存")
        log.info("在途车新增保存:{}---{}---采购价:{}".format(res, table_json, purchase_price))

    @staticmethod
    def to_store(vin_str):
        """转入库单"""
        data = {
            "storageCode": "ZCCK",
            "storageName": "整车仓库",
            "vinStr": vin_str,
            "stockInType": 13071002
        }
        res = http_r.run_main("post", url=shipping_urls["在途车转入库"], data=data, name="在途车转入库")
        se_no = res["data"]["seNo"]  # 入库单号
        log.info("{}--{}转入库单,入库单号:{}".format(res, vin_str, se_no))

        return se_no

    @staticmethod
    def query(vin=""):
        params = {
            "limit": 100, "offset": 0,
            "searchData": {"vin": vin}
        }
        res = http_r.run_main('get', url=shipping_urls["在途车辆管理列表查询"], data=params, name="在途车辆管理列表查询")
        log.info("在途列表查询: {}".format(res["data"]["total"]))
        if res["data"]["total"] == 0:
            log.info("在途列表未查询到数据")
            return

        return res["data"]["list"][0]

    def capital_cost(self, vin):
        """资金成本设置"""
        car01 = self.query(vin)
        source_code = car01["source_code"]
        params = {"vin": vin}
        res = http_r.run_main("get", url=shipping_urls["获取资金成本规则"], data=params, name="获取资金成本规则")
        if len(res["data"]["vehCostRuleList"]) == 0:
            log.info("没有下发资金规则")
            return
        rule = random.choice(res["data"]["vehCostRuleList"])
        surety_bond_ratio = random.choice(res["data"]["suretyBondRatioList"])["statusCode"]
        item_id = rule["item_id"]
        if source_code == "0001":
            for item in res["data"]["vehCostRuleList"]:
                if item["rule_name"] in ["现金提车", "现金公式规则"]:
                    item_id = item["item_id"]
                else:
                    log.info("没有现金车资金规则")
                    return
        params = {"costRuleId": item_id}
        res = http_r.run_main('get', url=shipping_urls["获取指定资金成本"], data=params, name="获取指定资金成本")
        rule = res["data"]["vehCostRule"]
        d1 = datetime.datetime.now()
        d2 = d1 + datetime.timedelta(days=10)
        d3 = d2.strftime("%Y-%m-%d")
        data = {
            "shippingNotify": {"costRuleId": rule["itemId"], "suretyBondRatio": surety_bond_ratio,
                               "tkDate": current_date, "freeInterestDueDate": d3,
                               "acceptanceBillDueDate": d3, "interestholiDay": 10, "acceptBillDay": 10,
                               "commissionCharge": 0, "financialInstitution": rule["financialInstitution"],
                                "financialProducts": rule["financialProducts"],
                               "financialInstitutionDesc": rule["financialInstitutionDesc"],
                                "discountDueDate": d3},
            "vin": vin
        }
        res = http_r.run_main('post', url=shipping_urls["资金成本设置保存"], data=data, name="资金成本设置保存")
        log.info("{}--资金成本设置-资金规则:{}".format(res, rule["ruleName"]))


shipping_car = ShippingCar()


if __name__ == '__main__':
    vin_list1, table_json1 = shipping_car.faker_flag()
    # vin_str1 = ','.join(vin_list1)
    # shipping_car.new_save(table_json1)
    # shipping_car.to_store(vin_str1)























