import time
from interfaceTest.constants import advances_urls
from common.configHttp import http_r
from interfaceTest.initialization import initial
from common import Log


log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class AdvancePayment(object):
    def __init__(self):
        pass

    @staticmethod
    def query(order_no=""):
        params = {"limit": 20, "offset": 0, "searchData": {"receiveType": 12781001, "doNo": order_no}}
        res = http_r.run_main('get', url=advances_urls["预收款登记列表查询"], data=params, name="预收款登记列表查询")
        log.info("预收款登记列表查询: {}".format(res["data"]["total"]))
        receive_no = res['data']['list'][0]['receiveNo']
        deposit_status = res['data']['list'][0]['depositStatusDesc']

        return receive_no, deposit_status

    def gathering(self, order_no):
        """预订单收款"""
        auth_dict = initial.get_audits()
        user_name = auth_dict["用户信息"]['userName']
        user_id = auth_dict["用户信息"]['id']['userId']
        # --------------------------------------------------------------------------------------------------------------
        receive_no, deposit_status = self.query(order_no)
        if deposit_status in ["收款中", "退款中"]:
            data = {
                "receiveNo": receive_no,
                "functionCode": "002"
            }
            res = http_r.run_main('get', url=advances_urls["预收款登记收款界面"], data=data, name="预收款登记收款界面")
            log.info("----{}--点击收款...".format(order_no))
            form_data = res['data']['formData']
            form_data["payTypeCode"] = "0001"
            form_data["payTypeDesc"] = "现金"
            form_data["receiveDate"] = current_date
            form_data["gatheringType"] = 13161001
            form_data["writeoffTag"] = 12781001
            form_data["writeoffBy"] = user_id
            form_data["writeoffDate"] = int(round(time.time() * 1000))
            form_data["remark"] = "测试-购车建议书收款"
            form_data["transactor"] = user_name
            form_data["writeoffByDesc"] = user_name
            for key in list(form_data.keys()):
                if not form_data[key]:
                    del form_data[key]
            data = {"param": form_data}
            res = http_r.run_main('post', url=advances_urls["预收款登记收款保存"], data=data, name="预收款登记收款保存")
            log.info("{}---{}{}成功,-----(购车建议书已完成)-----".format(res, order_no, deposit_status[:2]))
        else:
            log.info("不满足收款条件: {}-{}".format(order_no, deposit_status))
            return


advance_payment = AdvancePayment()

if __name__ == '__main__':
    advance_payment.query()
    # advance_payment.gathering("DO2104120001")






