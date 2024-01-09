import time
from common.configHttp import http_r
from apiTest.constants import gathering_urls
from apiTest.initialization import initial
from common import Log


log = Log.logger


class SettlementGathering(object):
    def __init__(self):
        pass

    @staticmethod
    def query(order_no=""):
        params = {"limit": 20, "offset": 0, "funCode": "002", "searchData": {"funCode": "002", "keyWord": order_no}}
        res = http_r.run_main('get', url=gathering_urls["结算收款列表查询"], data=params, name="结算收款列表查询")
        if res["data"]["total"] == 0:
            log.info("结算收款列表查询-没有单据")
            return
        business_type = res["data"]["list"][0]["businessType"]
        so_status = res["data"]["list"][0]["soStatus"]
        customer_name = res["data"]["list"][0]["customerName"]
        pay_off = "未结清"
        if res["data"]["list"][0]["payOff"] == 12781001:
            pay_off = "已结清"
        log.info("结算收款查询: {} {} {} {}".format(order_no, business_type, so_status, pay_off))

        return business_type, so_status, customer_name

    def gathering(self, order_no):
        business_type, so_status, customer_name = self.query(order_no)
        params = {"soNo": order_no}
        res = http_r.run_main('get', url=gathering_urls["新增收款页"], data=params, name="结算收款新增收款页")
        order_arrearage = res["data"]["salesOrder"]["orderArrearageAmount"]
        # --------------------------------------------------------------------------------------------------------------
        auth_dict = initial.get_audits()
        user_name = auth_dict["用户信息"]['userName']
        user_id = auth_dict["用户信息"]['id']['userId']
        # --------------------------------------------------------------------------------------------------------------
        data = {"prePayAmount": 0, "isNew": 1,
                "param": {
                    "id": {}, "prePayAmount": 0, "receiveAmount": order_arrearage, "payer": customer_name,
                    "writeoffTag": 12781001, "writeoffBy": user_id, "writeoffDate": int(round(time.time() * 1000)),
                    "recorder": user_id, "recorderDesc": user_name, "receiveDate": int(round(time.time() * 1000)),
                    "gatheringType": 13161005,  # 收款类型:购车全款
                    "payTypeDesc": "现金", "payTypeCode": "0001",  # 付款方式:现金
                    "remark": "测试 -- 备注", "soNo": order_no}}
        if business_type == "一般销售" and so_status == "交车确认中":
            customer_no = res["data"]["customer"]["id"]["customerNo"]
            usable_amount = res["data"]["customer"]["usableAmount"]  # 预收款余额
            data["prePayAmount"] = usable_amount
            data["param"]["prePayAmount"] = usable_amount
            data["param"]["receiveAmount"] = order_arrearage - usable_amount
            data["param"]["customerNo"] = customer_no
            if usable_amount > order_arrearage:
                data["prePayAmount"] = order_arrearage
                data["params"]["prePayAmount"] = order_arrearage
                data["params"]["receiveAmount"] = 0
        elif business_type == "车辆调拨" and so_status == "交车确认中":
            data["param"]["tax"] = "0.03"
        elif business_type == "销售退回" and so_status == "已完成":
            used_pre_amount = res["data"]["usedPreAmount"]  # 已使用预收款
            customer_no = res["data"]["customer"]["id"]["customerNo"]
            data["param"]["tax"] = "0.16"
            data["prePayAmount"] = -used_pre_amount
            data["param"]["prePayAmount"] = -used_pre_amount
            data["param"]["receiveAmount"] = order_arrearage + used_pre_amount
            data["param"]["customerNo"] = customer_no
        else:
            log.info("不满足收款条件: {}-{}-{}".format(order_no, business_type, so_status))
            return
        res = http_r.run_main('post', url=gathering_urls["收款保存"], data=data, name="结算收款收款保存")
        log.info(res)


settlement_gathering = SettlementGathering()

if __name__ == '__main__':
    settlement_gathering.gathering("SN2104070006")











