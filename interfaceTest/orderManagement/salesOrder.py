import time
import json
from common.configHttp import http_r
from dataGenerated import randomData
from interfaceTest.initialization import initial
from interfaceTest.constants import sales_urls
from common import Log


log = Log.logger
auth_dict = initial.get_audits()
entity_name = auth_dict["用户信息"]["entityName"]
user_name = auth_dict["用户信息"]['userName']
user_id = auth_dict["用户信息"]['id']['userId']
options = auth_dict["选项权限"]
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class SalesOrder(object):
    def __init__(self):
        res = http_r.run_main('get', url=sales_urls["销售订单列表下拉初始化"], name="销售订单列表下拉初始化")
        self.status_dict = {}
        for item in res["data"]["soStatusList"]:
            self.status_dict[item["statusDesc"]] = item["statusCode"]

    @staticmethod
    def is_dispatch_audit(vin):
        params = {"offset": 0, "limit": 15, "searchData": {"entityName": entity_name, "vin": vin}}
        res = http_r.run_main('get', url=sales_urls["库存维护列表查询"], data=params, name="库存维护列表查询")
        if res["data"]["total"] == 0:
            log.info("库存查不到这个车: {}".format(vin))
            return
        vin_info = res["data"]["list"][0]
        product_data = initial.vehicle_main(product_code=vin_info["productCode"])
        stock_time = vin_info["inTransitDays"]
        params = {
            "searchData": {"brandCode": product_data["brand"], "brandName": product_data["brandName"],
                           "seriesCode": product_data["series"], "seriesName": product_data["seriesName"],
                           "modelCode": product_data["model"], "modelName": product_data["modelName"],
                           "isSalesOrder": 12781001},
            "offset": 0, "limit": 20
        }
        res = http_r.run_main('get', url=sales_urls["库存车辆查询"], data=params, name="销售订单库存车辆查询")
        big_stock_time = int(res["data"]["list"][0]["stockTime"])
        big_vin = res["data"]["list"][0]["vin"]
        is_dispatched_audit = 12781002
        if options["不按先进先出进行配车（两个允许配车勾上了就可以任意配车）"] == 12781002:
            if big_stock_time >= 365 and vin != big_vin:
                is_dispatched_audit = 12781001
                log.info("最大库龄:{},车辆库龄:{} 不满足先进先出规则,需要配车审核!".format(big_stock_time, stock_time))
            elif big_stock_time >= 60 and big_stock_time - stock_time > 30:
                is_dispatched_audit = 12781001
                log.info("最大库龄:{},车辆库龄:{} 不满足先进先出规则,需要配车审核!".format(big_stock_time, stock_time))
            elif big_stock_time < 60:
                log.info("最大库龄:{},车辆库龄:{} 无需配车审核".format(big_stock_time, stock_time))
            else:
                log.info("最大库龄:{},车辆库龄:{} 无需配车审核".format(big_stock_time, stock_time))

        return is_dispatched_audit

    @staticmethod
    def new_save(vin, phone=""):
        if options["允许进行配车"] == 12781002:
            log.error("没有配车权限")
            return
        # --------------------------------------------------------------------------------------------------------------
        ct_no = randomData.random_card()  # 随机生成身份证号码
        client_info = initial.customer_info(phone)  # 客户详细信息
        tpc = client_info["data"]["tpc"]  # 客户tpc
        # --------------------------------------------------------------------------------------------------------------
        params = {"offset": 0, "limit": 15, "searchData": {"entityName": entity_name, "vin": vin}}
        res = http_r.run_main('get', url=sales_urls["库存维护列表查询"], data=params, name="库存维护列表查询")
        if res["data"]["total"] == 0:
            log.error("库存查不到这个车: {}".format(vin))
            return
        vin_info = res["data"]["list"][0]
        product_data = initial.vehicle_main(product_code=vin_info["productCode"])
        stock_status = vin_info["stockSta"]
        log.info("{}, {}, {}".format(vin, vin_info["dispatchedStatus"], vin_info["stockStatus"]))
        if vin_info["dispatchedStatus"] in ["已配车确认", "已交车", "已交车确认"]:
            log.error("{},不能继续配车!".format(vin_info["dispatchedStatus"]))
            return
        actual_price = int(product_data["directivePrice"]*0.96)  # 销售订单实际售价
        # --------------------------------------------------------------------------------------------------------------
        data = {
            "productCode": product_data["productCode"],
            "vin": vin, "soNo": "", "stockStatus": int(stock_status)
        }
        res = http_r.run_main('post', url=sales_urls["选中vin返回信息"], data=data, name="选中vin返回信息")
        if tpc["customerType"] == 10181003:
            if vin_info["fixedAssetsTypeName"]:
                actual_price = res["data"]["tvs"]["invoicePriceIncludingTax"]  # 如果是固定资产车,售价取OA传过来的值
            else:
                log.error("本经销商客户,车辆必须为固定资产车,{}不是固定资产车".format(vin))
                return
        else:
            if vin_info["fixedAssetsTypeName"]:
                log.error("车辆{}为固定资产车,客户类型非本经销商".format(vin))
                return
        # --------------------------------------------------------------------------------------------------------------
        ct_code = tpc["ctCode"]
        ct_nu = tpc["certificateNo"]
        if ct_code is None:
            ct_code = 12391006
            ct_nu = ct_no[:10]
        else:
            if ct_nu == "":
                if ct_code == 12391001:
                    ct_nu = ct_no
                else:
                    ct_nu = ct_no[:8]
        # --------------------------------------------------------------------------------------------------------------
        sales_order_detail = {
            "soStatus": 13011010,
            "payMode": 10251001,  # 一次付清 按揭贷款:10251002
            "sheetCreateDate": current_date,
            "sheetCreatedBy": user_id,
            "sheetCreatedByDesc": user_name,
            "customerNo": tpc["id"]["customerNo"],
            "customerName": tpc["customerName"],
            "phone": tpc["contactorMobile"],
            "remarkHtml": "经甲乙双方友好协商，乙方自愿支付车辆运输费用2555元;",
            "oaAuditRemark": "OA审核备注-测试",
            "contractDate": current_date,
            "deliveryMode": 13021001,  # 交车方式
            "deliveringDate": current_date,
            "invoiceMode": 13031001,  # 开票方式
            "address": "武汉那条街",
            "customerType": tpc["customerType"],
            "ctCode": ct_code,
            "certificateNo": ct_nu,
            "soldBy": user_id,
            "soldByDesc": user_name,
            "contactorName": tpc["customerName"],
            "productCode": product_data["productCode"],
            "productName": product_data["productName"],
            "vin": vin,
            "storageCode": vin_info["storage_code"],
            # "dispatchedDate": "2021-03-22",
            # "dispatchedBy": 88880000002689,

            "directivePrice": product_data["directivePrice"],  # 车辆指导价
            "actualPrice": actual_price,  # 实际销售价
            "cashSaleDiscount": product_data["directivePrice"]-actual_price,  # 折让合计
            "newCarDiscount": product_data["directivePrice"]-actual_price,  # 新车折让
            "secondHandCarDiscount": 0,  # 二手车政策折让
            "bigCustomerDiscount": 0,  # 大客户政策折让
            "otherDiscount": 0,  # 其他政策折让

            "estimateInsCommission": 0,  # 预估保险返利
            "financeRebate": 0,  # 金融返利
            "estimateCommission": 1000,  # 预估佣金
            "bigCustomersCommission": 0,  # 大客户佣金
            "secondHandCommission": 0,  # 二手车佣金
            "purchasePrice": vin_info["purchasePrice"],  # 采购价格

            "derivedRemark": "衍生条款备注",
            "orderType": 92071001,
            "rebate": "{}".format(vin_info["rebate"]),  # 佣金
            "brandCode": product_data["brand"],
            "seriesCode": product_data["series"],
            "seriesCodeDesc": product_data["seriesName"],
            "modelCode": product_data["model"],
            "modelCodeDesc": product_data["modelName"],
            "configCode": product_data["config"],
            "configCodeDesc": product_data["configName"],
            "innerColor": product_data["innerColorCode"],
            "innerColorDesc": product_data["innerColorName"],
            "colorCode": product_data["color"],
            "colorCodeDesc": product_data["colorName"],
            "isLoan": 12781002,  # 是否贷款
            "realChangeVin": "LBESUBFC4LW027078",  # 二手车VIN
            "otherAmountObject": [11981003, 11981004],  # 其他服务
            "otherAmount": 2000,  # 其他服务金额
            "lossReplacementProfit": 0,  # 全损换新预估毛利
            "discountRefundAmount": 0,  # 后期折让或退款金额
            "decorationDerateAmount": 0,  # 精品减免金额
            "isHasDiscount": 12781001,  # 是否有折扣折让
            "discountItem": [14111001, 14111003],  # 折扣折让项目
            "otherServiceSum": 0,  # 衍生收入(展车装潢+销售装潢+劳务+咨询)
            "orderSum": product_data["directivePrice"],  # 订单总额  取的指导价
            "orderReceivableSum": actual_price,  # 整车应收金额
            "marginalStandard": 0,  # 边界值标准
            "storeNum": tpc["arriveNum"],  # 到店次数
            "engineNo": vin_info["engineNo"],
            "certificateNumber": vin_info["certificateNumber"],
            "relatedDecorationOrderList": [],
            "cancelRelatedDecorationOrderList": [],
            "relatedServiceOrderList": [],
            "cancelRelatedServiceOrderList": [],
            "relatedLoanOrderList": [],
            "cancelRelatedLoanOrderList": [],
            "order_receivable_sum": actual_price,  # 订单收入合计(整车应收+衍生收入)
            "printAmountSum": 2000,  # 其他服务金额
            "order_sum": product_data["directivePrice"],  # 指导价+衍生收入
            "dispatchedByDesc": "销售一"}
        if "depositOrder" in client_info['data']:
            sales_order_detail["relatedOrderNo"] = client_info["data"]["depositOrder"]["id"]["orderNo"]
            sales_order_detail["depositAmount"] = client_info["data"]["depositOrder"]["depositAmount"]
        payload = {'salesOrderDetailVoStr': sales_order_detail}
        res = http_r.run_main('post', url=sales_urls["销售订单保存"], data=payload, is_json=1, name="销售订单保存")
        log.info(res)
        so_no = res["data"]["soNo"]

        return so_no, tpc["customerType"]

    @staticmethod
    def submit_audit(so_no):
        data = {"soNo": so_no}
        res = http_r.run_main('post', url=sales_urls["提交审核"], data=data, name="销售订单提交审核")
        log.info("{}----提交审核 成功".format(res))

    @staticmethod
    def dispatch_audit(so_no):
        data = {"soNo": so_no}
        res = http_r.run_main('post', url=sales_urls["配车审核"], data=data, name="销售订单提交配车审核")
        log.info("{}----提交配车审核 成功".format(res))

    @staticmethod
    def order_query(so_no=""):
        params = {"limit": 10, "offset": 0, "searchData": {"keyWord": so_no}}
        res = http_r.run_main('get', url=sales_urls["销售订单列表查询"], data=params, name="销售订单列表查询")
        if res["data"]["total"] == 0:
            log.info("销售订单列表未查到数据")
            return
        order_info = res["data"]["list"][0]

        return order_info

    def financial_reject(self, so_no):
        """财务驳回"""
        params = {"soNo": so_no}
        res = http_r.run_main('get', url=sales_urls["财务驳回订单状态"], data=params, name="财务驳回订单状态")
        if res["data"]["soStatus"] != self.status_dict["交车确认中"]:
            log.error("订单不是交车确认中的状态,不能财务驳回!!!")
            return
        res = http_r.run_main('get', url=sales_urls["财务驳回订单是否收过款"], data=params, name="财务驳回订单是否收过款")
        if res["data"]["success"]:
            log.error("订单:{}已收款，请先进行退款操作之后再进行财务驳回!!!".format(so_no))
            return
        data = {"soNo": so_no, "remark": "销售订单财务驳回 -- 测试"}
        res = http_r.run_main('post', url=sales_urls["财务驳回确定"], data=data, name="财务驳回确定")
        log.info("{}-----订单:{}财务驳回成功!".format(res, so_no))


sales_order = SalesOrder()


if __name__ == '__main__':
    # sales_order.financial_reject("SN2104220001")
    sales_order.new_save("VWC3YP9R2H1TXAFK5")









