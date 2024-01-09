import time
import datetime
from dateutil.relativedelta import relativedelta
from common.configHttp import http_r
from apiTest.constants import oa_urls
from readConfig import read_config
from common import Log, randomData

log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
next_year = (datetime.datetime.now()-relativedelta(years=-1)).strftime('%Y-%m-%d')
entity_code = read_config.get_http('entity_code')


class FixedAssets(object):
    def __init__(self):
        pass

    @staticmethod
    def query(bill_code=""):
        """
        固定资产采购综合查询-查询
        :return: 第一条查询结果
        """
        params = {"page": 1, "pageSize": 15, "bill_code": bill_code}
        res = http_r.run_main('get', url=oa_urls["固定资产采购综合查询"], data=params, name="固定资产采购综合查询")
        if res["data"]["total"] == 0:
            log.warning("固定资产采购综合查询-未查到数据")
            return
        y_t = res["data"]["data"][0]

        return y_t

    @staticmethod
    def up_file():
        file_path = r"C:\Users\cpr264\Desktop\测试文件\阿狸.jpg"
        files = [("file", ("阿狸.jpg", open(file_path, 'rb'), "image/jpeg"))]
        res = http_r.run_main('post', url=oa_urls["车辆入库附件上传"], files=files, name="车辆入库附件上传")
        file_id = res["data"][0]["id"]

        return file_id

    @staticmethod
    def save(apply_type, buy_trench, vin=""):
        """
        固定资产车采购申请保存
        :param apply_type: 车辆类别
        :param buy_trench: 采购渠道  "自店采购": "1", "第三方租赁": "2", "厂家直发": "3"
        :param vin: 指定vin
        :return: 单据编号，接口id
        """
        if buy_trench not in ["自店采购", "第三方租赁", "厂家直发", ""]:
            log.error("请指定正确的资产车采购渠道，如：自店采购，第三方租赁，厂家直发，空字符串")
            return
        trench_type = {"自店采购": "1", "第三方租赁": "2", "厂家直发": "3", "": ""}
        if apply_type not in ["工作车", "服务替换车", "试乘试驾车", "售后救援车", "清障车"]:
            log.error("请指定正确的资产车类型，如：工作车，服务替换车，试乘试驾车，售后救援车，清障车")
            return
        if apply_type in ["工作车", "售后救援车", "清障车"]:
            buy_trench = ""
        if apply_type in ["试乘试驾车", "服务替换车"] and buy_trench == "":
            log.warning("未指定采购渠道默认为自店采购")
            buy_trench = "自店采购"
        params = {"function_code": 32021002}
        res = http_r.run_main('get', url=oa_urls["公司OA"], data=params, name="公司OA")
        if res["code"] == 400:
            log.error("".format(res["msg"]))
            return
        oa_company = {}
        for item in res["data"]:
            if item["erp_code"] == entity_code:
                oa_company = item
        print(oa_company)
        company_name = oa_company["codename"]
        erp_code = oa_company["erp_code"]
        entity_name = oa_company["unitname"]
        oa_id = oa_company["id"]
        car_type = {"工作车": "1", "服务替换车": "2", "试乘试驾车": "3", "售后救援车": "8", "清障车": "10"}
        tax = 1 + 0.13
        f_price = 400000  # 官方指导价
        brand = "红旗"
        brand_code = ""
        color = "黑色"
        color_code = ""
        model = "2018款 2.0T 60周年纪念版"
        model_code = ""
        series = "H7"
        series_code = ""
        vin_1 = randomData.random_vin()
        if vin:
            vin_1 = vin
        vin_type = "0"
        power_type = ""
        profit_type = ""
        if apply_type in ["试乘试驾车", "服务替换车", "售后救援车"] and (buy_trench == "自店采购" or vin_type == "1"):
            data = {"data": {"dispatchedStatus": "13051001", "entityCode": erp_code, "count": 15, "vin": vin}}
            res = http_r.run_main('post', url=oa_urls["获取erp库存车"], data=data, name="获取erp库存车")
            y_t = []  # 选出在库车字典
            for item in res["data"]["list"]:
                if item["stockStatus"] == "在库":
                    y_t.append(item)
            product_data = y_t[0]
            tax = 1 + product_data["tax"]
            optional_price = product_data["optionalPrice"]
            if optional_price is None:
                optional_price = 0
            f_price = product_data["directivePrice"] + optional_price  # 官方指导价
            power_type = product_data["powerType"]
            profit_type = product_data["profitType"]
            brand = product_data["brandName"]
            brand_code = product_data["brandCode"]
            color = product_data["colorName"]
            color_code = product_data["colorCode"]
            model = product_data["modelName"]
            model_code = product_data["modelCode"]
            series = product_data["seriesName"]
            series_code = product_data["seriesCode"]
            vin_1 = product_data["vin"]
            vin_type = "1"
        ticket_price = f_price - 50000  # 开票金额
        tax_price = ticket_price*0.1  # 预估购置税
        no_tax = ticket_price/tax  # 开票不含税
        insurance_price = 3000  # 预估保险
        registration_price = 200  # 上牌费
        assets_price = no_tax + tax_price  # 固定资产原值
        total_no_tax = assets_price + insurance_price + registration_price
        total_tax = ticket_price + tax_price + insurance_price + registration_price
        data = {
            "attachment_ids": [], "bill_code": "",
            "brand": brand, "brand_code": brand_code, "color": color, "color_code": color_code,
            "model": model, "model_code": model_code, "serie": series, "serie_code": series_code,
            "power_type": power_type, "profit_type": profit_type,

            "car_type": car_type[apply_type],  # 车辆类别 （1:工作车）
            "company_name": company_name,  # 申请公司
            "company_type": "",
            "engine_no": "{}".format(vin_1[:5]),
            "expire_at": next_year,  # 到期时间
            "frequesttotalpayments": total_tax,  # 含税总额
            "ftotalprice": total_no_tax,  # 不含税总额
            "funds_use": "公司申请固定资产车，用于行政日常买菜",  # 申购事由
            "icompany_id": oa_id,
            "industry_hold": "",
            "ispreparation": "0",
            "unifiedbuy": "0",
            "management_vehicle_key_num": "1",  # 管理部门钥匙数量
            "userdeptment_vehicle_key_num": "1",  # 使用部门钥匙数量
            "request_time": current_date,  # 申请时间
            "requesttype": "1",  # 申请类别（1-车辆资产）
            "procurement_channels": trench_type[buy_trench],  # 采购渠道
            "status": "编写中",
            "supplier": entity_name,
            "table_infos": [{
                "assetsprice": assets_price,  # 固定资产原值
                "discount": "{}".format(ticket_price/f_price),  # 开票折扣率
                "fappnum": 1,  # 已有上牌数
                "fnum": "1",  # 申请数量
                "fprice": f_price,  # 官方指导价
                "insuranceprice": "{}".format(insurance_price),  # 预估保险费
                "noticketprice": "{}".format(no_tax),  # 开篇不含税
                "shangpaiprice": "{}".format(registration_price),  # 预估上牌费
                "taxprice": "{}".format(tax_price),  # 预估购置税
                "ticketprice": "{}".format(ticket_price)  # 开票含税
            }],
            "taxrate": "{}".format(tax),  # 税率
            "totalNoTax": total_no_tax,
            "totalTax": total_tax,
            "u_id": "",
            "vin": vin_1,
            "vin_type": vin_type,
        }
        res = http_r.run_main('post', url=oa_urls["固定资产采购申请"], data=data, is_json=2, name="固定资产采购申请")
        print(res)
        bill_code = res["data"]["bill_code"]
        url_id = res["data"]["id"]
        log.info("固定资产({})采购申请成功，单据编号：{}，VIN：{}".format(apply_type, bill_code, vin_1))

        return bill_code, url_id, vin_1

    @staticmethod
    def submit_audit(url_id, url_name):
        """
        固定资产车采购申请提交审核
        :param url_id: 接口id
        :param url_name: 接口描述
        :return:
        """
        url = oa_urls[url_name].format(url_id)
        res = http_r.run_main('put', url=url, name=url_name)
        log.info(res["msg"])

    @staticmethod
    def query1(vin):
        """
        车辆信息综合查询-查询
        :param vin: 查询条件-车架号
        :return: 查询结果字典-车辆信息
        """
        params = {
            "page": 1, "rows": 15, "vin": vin, "function_code": 32006103
        }
        res = http_r.run_main('get', url=oa_urls["车辆信息综合查询"], data=params, name="车辆信息综合查询")
        if res["data"]["total"] == 0:
            log.error("车辆信息综合查询-未查到数据")
            return

        data = res["data"]["data"][0]

        return data

    def to_store(self, url_id):
        """
        车辆信息综合查询-入库
        :param url_id: 接口编号
        :return: 单据编号
        """
        res = http_r.run_main('get', url=oa_urls["进入入库页"].format(url_id), name="进入入库页")
        data = res["data"]

        purchase_tax = (float(data["marketprice"])-50000)*0.1

        payload = {"company_id": data["company_id"],
                   "applier_name": data["applier_name"],
                   "request_time": data["request_time"],
                   "bill_code": data["bill_code"],
                   "status": data["status"],
                   "fee_billcode": data["fee_billcode"],
                   "marketprice": data["marketprice"],
                   "vin": data["vin"],
                   "vin_type": data["vin_type"],
                   "brand": data["brand"],
                   "stock": data["stock"],
                   "color": data["color"],

                   "assets_number": data["assets_number"],
                   "car_type": data["car_type"],

                   "purchase_time": current_date,  # 上牌日期
                   "year_careful_time": next_year,  # 年审到期 +1年
                   "mileage": "25",

                   "engine_number": data["engine_number"],
                   "manufactor_gps": data["manufactor_gps"],  # 是否安装厂家gps

                   "licensing_additional_taxes": purchase_tax+300,
                   "no_commission_fare_opening": data["no_commission_fare_opening"],
                   "purchase_cost": "{}".format(float(data["tax_invoice_price"])+purchase_tax),

                   "note": data["note"],  # 备注
                   "serie": data["serie"],
                   "expire_at": data["expire_at"],
                   "discount": data["discount"],
                   "tax_invoice_price": data["tax_invoice_price"],

                   "insure_expire_at": "",
                   "insurance_endtime": "",
                   "insurance_car_endtime": "",

                   "car_file_0": [self.up_file()],
                   "car_file_1": [self.up_file()],
                   "car_file_2": [self.up_file()],
                   "car_file_3": [self.up_file()],
                   "car_file_4": [self.up_file()],
                   "car_file_6": [self.up_file()],
                   "plates": randomData.random_car(),

                   "purchase_tax": str(purchase_tax),  # 购置税
                   "license_fee": "300.00",  # 上牌费
                   "insurance_num": "",  # 保险费
                   "tax_rate": data["tax_rate"],
                   "management_vehicle_key_num": data["management_vehicle_key_num"],
                   "userdeptment_vehicle_key_num": data["userdeptment_vehicle_key_num"]}
        res = http_r.run_main('put', url=oa_urls["固定资产车入库"].format(url_id), data=payload, is_json=2, name="固定资产车入库")
        bill_code = res["data"]["bill_code"]
        log.info("固定资产车入库保存成功 单号:{}，车架号:{}".format(bill_code, data["vin"]))

        return bill_code


fixed_assets = FixedAssets()


if __name__ == '__main__':
    b, u, v = fixed_assets.save("试乘试驾车", buy_trench="自店采购", vin="0V24H3RX4K5T9ESDB")
    print(b, u, v)
    fixed_assets.submit_audit(u, "固定资产车采购申请提交审核")
    # u_id = fixed_assets.query1(vin="LEFCJCDC79HP30D0D")
    # fixed_assets.to_store(u_id["id"])
    # fixed_assets.submit_audit(u_id["id"], "固定资产车入库提交审核")

