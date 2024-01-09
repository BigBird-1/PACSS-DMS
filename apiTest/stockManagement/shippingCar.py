import time
import datetime
import random
from common.configHttp import http_r
from apiTest.initialization import initial
from apiTest.constants import shipping_urls, shipping_cars, is_deputy_delivery
from readConfig import read_config
from common import Log, randomData

log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
product_code = read_config.get_http("productCode")
product_data = initial.vehicle_main(product_code)  # 产品数据


class ShippingCar(object):
    def __init__(self):
        res1 = http_r.run_main('get', url=shipping_urls["新增页面初始化"], name="在途新增页面初始化")
        self.shipment_code = res1['data']['shipmentList'][0]['statusCode']  # 发运地代码
        self.tax = res1['data']['tax']

    def faker_flag(self, vin):
        """
        校验是否虚销
        :param vin: 字符串 "AAA" 或者 "AAA,BBB"
        :return:
        """
        directive_price = product_data["directivePrice"]
        params = {"searchData": {"productCode": product_code}}
        res = http_r.run_main('get', url=shipping_urls["获取选装包"], data=params, name="获取选装包")
        if len(res["data"]["optionalCodeList"]) == 0:
            optional_code = ""
            optional_name = ""
            optional_price = 0
        else:
            optional = res["data"]["optionalCodeList"][0]
            optional_code = optional["optionalCode"]
            optional_name = optional["optionalName"]
            optional_price = optional["optionalPrice"]
        # --------------------------------------------------------------------------------------------------------------
        params = {"productCode": product_code}
        res = http_r.run_main('get', url=shipping_urls["获取产品内/外饰色"], data=params, name="获取产品内/外饰色")
        inner_color = res["data"]["innerColorCodeList"]
        outer_color = res["data"]["outerColorCodeList"]
        if len(inner_color) == 0 or len(outer_color) == 0:
            log.error("未下发产品内/外饰色，不能新增在途车")
            return
        # -----------采购价格，税率，不含税采购价，税额-----------------------------------------------------------------
        purchase_price = int(directive_price * 0.92)
        no_tax_vehicle_cost = purchase_price / (1 + self.tax)
        tax_amount = purchase_price - no_tax_vehicle_cost
        # --------------------------------------------------------------------------------------------------------------
        vin_list = []
        table_json = []
        if vin:
            vin_list = vin.split(",")
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
            table_dict["optionalCode"] = optional_code
            table_dict["optionalName"] = optional_name
            table_dict["optionalPrice"] = optional_price
            table_dict["factoryVehiclePrice"] = optional_price + directive_price
            table_dict["outerColorCode"] = outer_color[0]["outerColorCode"]
            table_dict["innerColorCode"] = inner_color[0]["innerColorCode"]
            table_dict["purchasePrice"] = purchase_price
            table_dict["tax"] = self.tax
            table_dict["notaxVehicleCost"] = no_tax_vehicle_cost
            table_dict["taxAmount"] = tax_amount
            table_dict["standardCommission"] = directive_price*0.03  # 标准提车佣金
            if res['data']['code'] == 1:
                table_dict["fakeFlag"] = 12781001
                table_dict["fakeDate"] = res['data']['fakeDate']
            table_json.append(table_dict)
        data = {"tableJson": table_json}
        res = http_r.run_main('post', url=shipping_urls["是否存在库存"], data=data, name="是否存在库存")
        log.info(res)
        return vin_list, table_json

    def new_save(self, vin):
        vin_list, table_json = self.faker_flag(vin)
        # -----------------获取平均在途,周转天数------------------------------------------------------------------------
        params = {
            "productCode": product_data["productCode"]}
        res2 = http_r.run_main('get', url=shipping_urls["标准在途天数"], data=params, name="标准在途天数")
        avg_transit = res2["data"]["avgTransitDays"]
        res3 = http_r.run_main('get', url=shipping_urls["标准周转天数"], data=params, name="标准周转天数")
        avg_turnover = res3["data"]["avgTurnoverDays"]
        # ------------------获取动力类型--------------------------------------------------------------------------------
        params = {
            "searchData": {"productCode": product_data["productCode"]}
        }
        res = http_r.run_main('get', url=shipping_urls["获取动力类型"], data=params, name="获取动力类型")
        p_data = res["data"]["list"][0]["children"][0]
        power_type = p_data["powerType"]
        profit_type = p_data["profitType"]
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

                          "standardCommission": product_data["directivePrice"]*0.03,  # 提车佣金
                          "deliveryCommission": 0,

                          "realOemPickUpDate": current_date + "T16:00:00.000Z",

                          "isDeputyDelivery": is_deputy_delivery,  # 是否代交车
                          "powerType": power_type,  # 动力类型(99951001纯电动, 99951002燃油, 99951003混动)
                          "profitType": profit_type,  # 盈利类型

                          "id": {"entityCode": "", "vin": ""},
                          "sourceCode": "1002",  # 资金来源*
                          "sourceCodeDesc": "银行融资",
                          "dischargeStandard": 30101009,  # 排放标准*
                          "vehicleType": 80151001,  # 车辆类型*
                          "shippingDate": current_date,  # 发车日期
                          "arrivingDate": current_date,  # 预计到货日
                          "certificateLocated": "台湾省",  # 合格证所在地
                          "poNo": ""},  # 采购计划单号
            "tableJson": table_json,
            "deliveryCommission": 0,  # 标准交车佣金
            "isAdd": "true"
        }
        if is_deputy_delivery == 12781001:
            data["paramJson"]["sourceCode"] = ""
            data["paramJson"]["sourceCodeDesc"] = ""
            data["paramJson"]["purchasePrice"] = 0
            data["paramJson"]["notaxVehicleCost"] = 0
            data["paramJson"]["taxAmount"] = 0
        if data["paramJson"]["powerType"] == 99951001:
            data["paramJson"]["dischargeStandard"] = ""
        for key in list(data["paramJson"].keys()):
            if not data["paramJson"][key]:
                del data["paramJson"][key]
        res = http_r.run_main("post", url=shipping_urls["在途车保存"], data=data, name="在途车保存")
        log.info("在途车新增保存:{}---{}---".format(res, vin_list))

        return vin_list

    @staticmethod
    def delete_car(vin):
        """删除在途车"""
        data = {"vin": vin}
        res = http_r.run_main("post", url=shipping_urls["在途车删除"], data=data, name="在途车删除")
        msg = res["data"]["msg"]
        log.info("{}-{}".format(vin, msg))

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
        list1 = []  # 现金规则
        list2 = []  # 非现金规则
        status_code = ""
        financial_products_list = res["data"]["financialProductsList"]
        for item in financial_products_list:
            if item["statusDesc"] == "现金":
                status_code = item["statusCode"]
        rule_list = res["data"]["vehCostRuleList"]
        if len(rule_list) == 0:
            log.error("未下发单车资金成本规则！！！")
            return
        for item in res["data"]["vehCostRuleList"]:
            if item["financial_products"] == status_code:
                list1.append(item)
            else:
                list2.append(item)
        rule = list2[0]
        if source_code == "0001":
            if len(list1) == 0:
                log.error("未下发现金资金成本规则！！！")
                return
            rule = list1[0]
        surety_bond_ratio = random.choice(res["data"]["suretyBondRatioList"])["statusCode"]  # 保证金比例
        d1 = datetime.datetime.now()
        d2 = d1 + datetime.timedelta(days=10)
        d3 = d2.strftime("%Y-%m-%d")
        data = {
            "shippingNotify": {
                "factoryDiscount": "", "costRuleId": rule["item_id"], "suretyBondRatio": surety_bond_ratio,
                "tkDate": current_date, "interestholiDay": 10, "acceptBillDay": 10, "commissionCharge": 0,
                "freeInterestDueDate": d3, "sourceCode": "",
                "financialInstitution": rule["financial_institution"],
                "financialProducts": rule["financial_products"],
                "financialInstitutionDesc": rule["financial_institution_desc"],
                "acceptanceBillDueDate": d3,
                "discountDueDate": d3
            },
            "vin": vin,
            "isFactoryDiscount": "false"
        }
        res = http_r.run_main('post', url=shipping_urls["资金成本设置保存"], data=data, name="资金成本设置保存")
        log.info("{}--资金成本设置-资金规则:{}".format(res, rule["rule_name"]))


shipping_car = ShippingCar()


if __name__ == '__main__':
    shipping_car.new_save(vin="")
    # shipping_car.capital_cost("TCRHY8MK4FJ34GPS6")























