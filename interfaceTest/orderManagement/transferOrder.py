import time
from common.configHttp import http_r
from interfaceTest.initialization import initial
from interfaceTest.constants import transfer_urls
from readConfig import read_config
from common import Log


log = Log.logger
# 获取当前日期 年月日
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class TransferOrder(object):
    def __init__(self):
        params = {"funCode": "001"}
        res = http_r.run_main('get', url=transfer_urls["调拨订单新增initData"], data=params, name="调拨订单新增initData")

    @staticmethod
    def new_save(vin):
        auth_dict = initial.get_audits()
        user_name = auth_dict["用户信息"]['userName']
        user_id = auth_dict["用户信息"]['id']['userId']
        entity_name = auth_dict["用户信息"]["entityName"]
        customer_code = read_config.get_http("entity_code1")  # 调拨B店
        # --------------------------------------------------------------------------------------------------------------
        params = {"offset": 0, "limit": 15, "searchData": {"customerTypeCode": "9999", "customerCode": customer_code}}
        res = http_r.run_main('get', url=transfer_urls["客户选择页查询"], data=params, name="客户选择页查询")
        customer_info = res["data"]["list"][0]
        # --------------------------------------------------------------------------------------------------------------
        params = {"offset": 0, "limit": 15, "searchData": {"entityName": entity_name, "vin": vin}}
        res = http_r.run_main('get', url=transfer_urls["库存维护列表查询"], data=params, name="库存维护列表查询")
        if res["data"]["total"] == 0:
            log.info("库存查不到这个车: {}".format(vin))
            return
        vin_info = res["data"]["list"][0]
        product_data = initial.vehicle_main(product_code=vin_info["productCode"])
        log.info("{}, {}, {}".format(vin, vin_info["dispatchedStatus"], vin_info["stockStatus"]))
        if vin_info["dispatchedStatus"] in ["已配车", "已配车确认", "已交车", "已交车确认"]:
            log.info("{},不能继续配车!".format(vin_info["dispatchedStatus"]))
            return
        # --------------------------------------------------------------------------------------------------------------
        params = {"vin": vin}
        res = http_r.run_main('get', url=transfer_urls["车辆信息"], data=params, name="车辆信息")
        price_status = res["data"]["priceStatus"]  # 销售指导价:15341002 含税成本价:15341001
        tsk = res["data"]["tsk"]
        vehicle_price = tsk["directivePrice"]  # 调拨价格
        if price_status == 15341001:
            vehicle_price = tsk["purchasePrice"]
        # --------------------------------------------------------------------------------------------------------------
        transfer_order_detail = {
            "sheetCreatedBy": user_id, "sheetCreatedByDesc": user_name, "sheetCreateDate": current_date,  # 开单信息
            "soldBy": user_id, "soldByDesc": user_name,  # 销售顾问
            "soStatus": 13011010,
            "payMode": 10251001,
            "invoiceMode": 13031001,  # 开票方式
            "deliveringDate": current_time,  # 预定交车日期
            "remark": "调拨订单测试-备注",

            "consigneeName": customer_info["customerName"], "consigneeCode": customer_info["customerCode"],
            "oaAuditNo": "DBDD{}".format(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))),
            "contactorName": "联系人", "address": "地址", "deliveryAddress": "运送地址",

            "vehiclePrice": vehicle_price,  # 调拨价格
            "transferDiscountAmount": 12000,  # 调拨折扣
            "isOverVehiclePrice": 12781002,  # 是否高于车本价
            "orderReceivableSum": vehicle_price - 12000,  # 订单应收

            "storageCode": tsk["storageCode"],
            "dispatchedBy": user_id, "dispatchedByDesc": user_name, "dispatchedDate": current_date,  # 配车信息
            "vin": vin,
            "directivePrice": product_data["directivePrice"],
            "productCode": product_data["productCode"],
            "productName": product_data["productName"],
            "brandCode": product_data["brand"],
            "brandName": product_data["brandName"],
            "seriesCode": product_data["series"],
            "seriesName": product_data["seriesName"],
            "modelCode": product_data["model"],
            "modelName": product_data["modelName"],
            "configCode": product_data["config"],
            "configName": product_data["configName"],
            "innerColor": product_data["innerColorCode"],
            "innerColorName": product_data["innerColorName"],
            "colorCode": product_data["color"],
            "outerColorName": product_data["colorName"]
        }
        data = {'paramJson': transfer_order_detail}
        res = http_r.run_main('post', url=transfer_urls["调拨订单保存"], data=data, name="调拨订单保存")
        so_no = res["data"]["soNo"]
        log.info("{}----调拨订单:{} 新增成功!".format(res, so_no))

        return so_no

    @staticmethod
    def submit_audit(so_no):
        data = {"soNo": so_no}
        res = http_r.run_main('post', url=transfer_urls["提交审核"], data=data, name="调拨订单提交审核")
        log.info("{}----提交审核 成功".format(res))

    @staticmethod
    def order_query(so_no=""):
        params = {"limit": 10, "offset": 0, "searchData": {"keyWord": so_no}}
        res = http_r.run_main('get', url=transfer_urls["调拨订单列表查询"], data=params, name="调拨订单列表查询")
        if res["data"]["total"] == 0:
            log.info("调拨订单列表查询没有数据")
            return
        order_info = res["data"]["list"][0]

        return order_info

    @staticmethod
    def order_cancel(vin=""):
        """调拨退回查询"""
        params = {
            "searchData": {"cancelType": 13001006, "keyWord": vin},
            "offset": 0, "limit": 20
        }
        res = http_r.run_main('get', url=transfer_urls["调拨退回列表查询"], data=params, name="调拨退回列表查询")
        log.info("调拨退回列表查询: {}".format(res["data"]["total"]))
        if res["data"]["total"] == 0:
            log.info("调拨退回列表查询-未查到数据")
        y_t = res["data"]["list"][0]

        return y_t


transfer_order = TransferOrder()

if __name__ == '__main__':
    transfer_order.order_query()
    # transfer_order.new_save()








