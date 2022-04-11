import time
import json
import random
from common.configHttp import http_r
from dataGenerated import randomData
from interfaceTest.initialization import initial
from interfaceTest.constants import deposit_urls
from readConfig import read_config
from common import Log


log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class DepositOrder(object):
    def __init__(self):
        self.type_dict = {}
        self.part_table_data = []  # 汽车用品配件
        res = http_r.run_main('get', url=deposit_urls["新增页面下拉框初始化"], name="购车建议书下拉框初始化")
        self.ctCodeList = res["data"]["ctCodeList"]
        for item in res["data"]["ctCodeList"]:
            self.type_dict[item["statusDesc"]] = item["statusCode"]
        for item in res["data"]["payModeList"]:
            self.type_dict[item["statusDesc"]] = item["statusCode"]
        for item in res["data"]["soldByList"]:
            self.type_dict[item["userName"]] = item["id"]["userId"]
        res = http_r.run_main('get', url=deposit_urls["精品查询页面初始化"], name="精品查询页面初始化")
        for item in res["data"]["typeList"]:
            self.type_dict[item["statusDesc"]] = item["statusCode"]

    @staticmethod
    def query(order_no=""):
        params = {"limit": 10, "offset": 0, "searchData": {"keyWord": order_no}}
        res = http_r.run_main('get', url=deposit_urls["预订单查询列表查询"], data=params, name="购车建议书查询列表查询")
        log.info("购车建议书查询列表查询: {}".format(res["data"]["total"]))
        if res["data"]["total"] == 0:
            log.error("购车建议书查询列表查询")
            return
        order_info = res["data"]["list"][0]

        return order_info

    def boutique(self, type_desc, num):
        y_t = num  # 随机选择X个配件
        params = {"limit": 50, "offset": 0, "searchData": {"typeCode": self.type_dict[type_desc],
                                                           "stockQuantity": "12781001"}}
        res = http_r.run_main('get', url=deposit_urls["配件用品查询"], data=params, name="配件用品查询")
        if res["data"]["total"] == 0:
            log.warning("未查到库存大于0的{}".format(type_desc))
            return
        if y_t > len(res["data"]["list"]):
            y_t = len(res["data"]["list"])
        j = 0
        for i in random.sample(res["data"]["list"], y_t):
            item = dict()
            item["serviceCode"] = i["partNo"]
            item["serviceName"] = i["partName"]
            item["directivePrice"] = i["salesPrice"]
            item["quantity"] = j + 1
            item["remark"] = "测试备注精品{}".format(j + 1)
            item["storageCode"] = i["storageCode"]
            item["typeCode"] = i["typeCode"]
            self.part_table_data.append(item)
            j += 1

    def new_save(self, code_desc, phone=""):
        """新增-保存购车建议书"""
        client_info = initial.customer_info(phone)  # 选择客户返回客户详细信息
        tpc = client_info["data"]["tpc"]  # 客户tpc
        ct_no = randomData.random_card()  # 随机生成身份证号码
        product_data = initial.vehicle_main(read_config.get_http("productCode"))  # 车辆主数据信息(可传产品代码)
        auth_dict = initial.get_audits()
        user_name = auth_dict["用户信息"]['userName']  # 登陆用户信息
        user_id = auth_dict["用户信息"]['id']['userId']
        # -----------------------衍生信息-------------------------------------------------------------------------------
        params = {"editMode": 1}
        res = http_r.run_main('get', data=params, url=deposit_urls["明细初始化"], name="预订单内衍生明细初始化")
        city_code = res["data"]["city"]  # 城市默认值
        insurance_code = []  # 车险
        for item in res["data"]["insuranceServiceList"]:
            insurance_code.append(item["id"]["insuranceTypeCode"])
        labour_code = []  # 劳务
        for item in res["data"]["labourServiceList"]:
            labour_code.append(item["id"]["serviceCode"])
        other_vehicle_code = []  # 非车险
        for item in res["data"]["otherVehicleInsuranceServiceList"]:
            other_vehicle_code.append(item["insuranceTypeCode"])
        after_sales_code = []  # 售后保养
        for item in res["data"]["afterSalesServiceList"]:
            after_sales_code.append(item["packageCode"])
        after_extension_code = []  # 售后延保
        for item in res["data"]["afterExtensionInsuranceList"]:
            after_extension_code.append(item["packageCode"])
        if len(res["data"]["extInsuranceList"]) == 0 or len(res["data"]["insuranceList"]) == 0:
            log.error("没有有效的保险公司或衍生险")
            return
        insurance_company1 = res["data"]["insuranceList"][0]["id"]["insurationCode"]  # 车险保险公司
        insurance_company = res["data"]["extInsuranceList"][-1]["insurationCode"]  # 衍生服务保险公司
        payload = {"insurationCode": insurance_company}
        res = http_r.run_main('post', url=deposit_urls["衍生服务险list"], data=payload, is_json=1, name="衍生服务险list")
        extension_code = []  # 衍生服务
        for item in res["data"]:
            extension_code.append(item["packageCode"])
        # ------------------------汽车用品明细--------------------------------------------------------------------------
        self.boutique("配件", 2)  # 配件2个
        self.boutique("用品", 1)  # 用品1个
        # ------------------------上牌城市------------------------------------------------------------------------------
        params = {"city": ""}
        res = http_r.run_main('get', url=deposit_urls["城市查询"], data=params, name="预订单内城市查询")
        # city_code = res["data"]["listedCityList"][0]["statusCode"]
        # ------------------------预定金规则----------------------------------------------------------------------------
        ct_code = self.type_dict[code_desc]
        data = {"vehiclePrice": product_data["directivePrice"]}
        res = http_r.run_main('post', url=deposit_urls["获取预定金最低金额"], data=data, name="获取预定金最低金额")
        deposit_amount = res['data']['depositLimit']  # 车价对应订金最低金额
        ct_num = ct_no[:8]
        if ct_code == self.type_dict["机构代码"]:
            deposit_amount = 0.01
        if ct_code == self.type_dict["居民身份证"]:
            ct_num = ct_no
        # -------------------------是否代交车---------------------------------------------------------------------------
        vin = ""
        is_deputy_delivery = 12781002
        if is_deputy_delivery == 12781001:
            params = {"searchData": {"isDeputyDelivery": 12781001, "isSalesOrder": 12781001}, "offset": 0, "limit": 20}
            res = http_r.run_main('get', url=deposit_urls["查询代交车"], data=params, name="查询代交车")
            if res["data"]["total"] == 0:
                log.warning("没有查到代交车")
            else:
                vin = res["data"]["list"][0]
                product_code = res["data"]["list"][0]["product_code"]
                product_data = initial.vehicle_main(product_code)
        # --------------------------------------------------------------------------------------------------------------
        vehicle_price = int(product_data["directivePrice"]*0.96)  # 车价
        order_data = {
            "id": {"orderNo": ""},

            "customerName": tpc["customerName"],  # 潜客姓名*
            "customerNo": tpc["id"]["customerNo"],  # 潜客编号*
            "orderType": "",  # 个人
            "ctCode": ct_code,  # 证件类型*
            "certificateNo": ct_num,  # 证件号码*
            "customerPhone": tpc["contactorMobile"],  # 手机号*
            "customerAddress": "湖北省武汉市那条街1号",  # 地址*
            "arriveNum": tpc["arriveNum"],  # 到店次数

            "productCode": product_data["productCode"],  # 产品代码*
            "brand": product_data["brand"],  # 品牌*
            "series": product_data["series"],  # 车系代码*
            "seriesCodeDesc": product_data["seriesName"],
            "model": product_data["model"],  # 车型代码*
            "modelCodeDesc": product_data["modelName"],
            "config": product_data["config"],  # 配置代码*
            "configCodeDesc": product_data["configName"],
            "color": product_data["color"],  # 外颜色代码*
            "colorCodeDesc": product_data["colorName"],
            "innerColor": product_data["innerColorCode"],  # 内饰色代码
            "innerColorDesc": product_data["innerColorName"],
            "directivePrice": product_data["directivePrice"],  # 销售指导价*

            "quantity": "",  # 数量
            "payMode": 10251002,  # 购买方式* 按揭贷款
            "soldBy": user_id,  # 销售顾问代码*
            "soldByDesc": user_name,  # 销售顾问姓名*
            "vehiclePrice": vehicle_price,  # 车价*
            "depositAmount": deposit_amount,  # 订金*
            "sheetCreatedBy": user_id,
            "sheetCreatedByDesc": user_name,  # 开单人
            "sheetCreateDate": current_date,  # 开单日期
            "vin": vin,
            "isPayDeposit": 12781001,  # 是否交预订金
            "useCarAddress": " 用车地址不能为空",  # 用车地址
            "listedCity": city_code,  # 上牌城市
            "depositPurchaseTax": int(vehicle_price/1.16*0.075),  # 购置税金额
            "secAssessmentAmount": 0,  # 预估置换车辆价格(含税)
            "shippingAmount": 0,  # 运费
            "remark": "经甲乙双方友好协商，以上购车金额包含代办客户购买保险（包含意外险项目）、精品（包含加装车翅膀项目）、按揭（蚂蚁上树）、代办客户购买购置税、车船税的全部费用;",

            "advisoryServiceAmount": 0,  # 咨询服务费
            "salesDecorationAmount": 0,  # 汽车用品金额
            "afterSaleAmount": 1000,  # 售后保养产品金额
            "tradeDiscount": 2700,  # 商业折扣
            "labourAmount": 200,  # 劳务服务费
            "otherInsurance": insurance_company1,  # 非车险保险公司
            "otherInsuranceServiceAmount": 1000,  # 非车险金额
            "extInsurance": insurance_company,  # 衍生保险公司
            "extInsuranceServiceAmount": 2000,  # 衍生保险金额
            "vehicleInsurance": insurance_company1,  # 车险保险公司
            "vehicleInsuranceServiceAmount": 1000,  # 车险保险金额
            "syInsuranceAmount": 0,  # 商业险
            "jqInsuranceAmount": 1000,  # 交强险
            "afterSaleExtAmount": 1000,  # 售后延保产品金额
        }
        table_data = []  # 咨询服务方案列表
        if order_data["payMode"] == 10251002:
            order_data["advisoryServiceAmount"] = 500
            m_1 = 36
            m_tax = 0.003
            t_m = int(vehicle_price*0.7)  # 贷款总金额
            rule_1 = m_tax * ((1 + m_tax) ** m_1) / ((1 + m_tax) ** m_1 - 1)
            m_2 = 12
            m_tax = 0.006
            rule_2 = m_tax * ((1 + m_tax) ** m_2) / ((1 + m_tax) ** m_2 - 1)
            table_data.append({"downPaymentAmount": vehicle_price-t_m,  # 首付款金额(元)
                               "loanAmount": t_m,  # 贷款总金额(元)
                               "vehicleLoanAmount": int(t_m*0.85),  # 整车贷款金额（元）
                               "loanTimeLimit": m_1,  # 整车贷款期数(月)
                               "monthlyPaymentAmount": (t_m*0.85)*rule_1,  # 月供
                               "addLoanAmount": int(t_m*0.15),  # 附加贷款金额（元）
                               "addLoanTimeLimit": m_2,  # 附加贷款期数（月）
                               "addMonthlyPaymentAmount": (t_m*0.15)*rule_2,  # 月供
                               "loanInterest": (t_m*0.85)*rule_1*m_1+(t_m*0.15)*rule_2*m_2-t_m,  # 贷款利息(元)
                               "remark": "桃之夭夭 烁烁其华",  # 备注

                               "loanInterestRate": "",
                               "closeVehicleHedgeAmount": ""})  # 咨询服务方案
        service_item = {
            "addDecorationPartListStr": [],  # 汽车用品(废弃)
            "addLabourServiceListStr": labour_code[:1],  # 劳务
            "addExtensionInsuranceListStr": extension_code[:1],  # 衍生包
            "addInsuranceServiceListStr": insurance_code[:2],  # 车险
            "addOtherVehicleInsuranceServiceListStr": other_vehicle_code[:1],  # 非车险
            "addAfterSalesServiceListStr": after_sales_code[:1],  # 售后保养产品
            "addAfterExtensionInsuranceListStr": after_extension_code[:1],  # 售后延保产品
            "addTradeDiscountListStr": [{"serviceCode": "20050001", "realPrice": 2000},
                                        {"serviceCode": "20050003", "realPrice": 700}],  # 商业折扣
            "delDecorationPartListStr": [], "delLabourServiceListStr": [], "delExtensionInsuranceListStr": [],
            "delInsuranceServiceListStr": [], "delOtherVehicleInsuranceServiceListStr": [],
            "delAfterSalesServiceListStr": [], "delAfterExtensionInsuranceListStr": [], "delTradeDiscountListStr": []
        }
        if self.part_table_data:
            order_data["salesDecorationAmount"] = 2100  # 汽车用品金额
        payload = {
            "tableData": table_data,
            "serviceItem": service_item,
            "salesDeptositOrder": order_data,
            "partTableData": self.part_table_data
        }
        res = http_r.run_main('post', url=deposit_urls["预订单保存"], data=payload, is_json=1, name="预订单保存")
        order_no = res['data']['orderNo']
        log.info("{}----客户:{}购车建议书:{}新增成功!".format(res, tpc["contactorMobile"], order_no))

        return order_no, tpc["contactorMobile"]

    @staticmethod
    def submit_audit(order_no):
        """购车建议书提交审核"""
        data = {'orderNo': order_no}
        res = http_r.run_main('post', url=deposit_urls["预订单提交审核"], data=data, name="预订单提交审核")
        log.info("{}----购车建议书: {}提交审核!!".format(res, order_no))

    @staticmethod
    def copy_order(order_no):
        data = {"orderNo": order_no}
        res = http_r.run_main('post', url=deposit_urls["预订单复制"], data=data, name="预订单复制")
        log.info("{}--正在复制购车建议书: {}".format(res, order_no))

    @staticmethod
    def invalid_order(order_no):
        data = {"orderNo": order_no}
        res = http_r.run_main('post', url=deposit_urls["预订单作废"], data=data, name="预订单作废")
        if "message" in res["data"]:
            log.info("{}---购车建议书:{}已作废".format(res, order_no))
        else:
            log.info("购车建议书状态不支持作废:{}".format(order_no))

    @staticmethod
    def order_return(order_no):
        data = {"orderNo": order_no, "isReview": False}
        res = http_r.run_main('post', url=deposit_urls["老单据"], data=data, name="老单据")
        if res["data"]["oldOrderNo"]:
            return_no = res["data"]["oldOrderNo"]  # 已存在的退回单
        else:
            res = http_r.run_main('get', url=deposit_urls["新建预订退回"], data=data, name="新建预订退回")
            log.info("{} 点击建议书退回-操作".format(res["code"]))
            data = {"orderNo": order_no, "cancelReason": "测试取消原因 - 购车建议书退回"}
            res = http_r.run_main("post", url=deposit_urls["预订退回单保存"], data=data, name="预订退回单保存")
            if not res["data"]["success"]:
                log.info(res["data"]["msg"])
                return
            return_no = res["data"]["tsdoi"]["id"]["orderNo"]  # 新增的退回单

        return return_no

    @staticmethod
    def submit_return_audit(return_no):
        data = {'orderNo': return_no}
        res = http_r.run_main('post', url=deposit_urls["预订退回单提交审核"], data=data, name="预订退回单提交审核")
        log.info("{}----购车建议书退回单{}提交审核!!".format(res, return_no))


deposit_order = DepositOrder()


if __name__ == '__main__':
    oo = deposit_order.new_save("居民身份证", phone="")
    # deposit_order.submit_audit(oo)
    # deposit_order.order_return("DO2106030001")
    # deposit_order.query("DO2106190002")
    # deposit_order.invalid_order("DO2107160006")












