import time
from common.configHttp import http_r
from interfaceTest.initialization import initial
from interfaceTest.constants import sales_return_urls
from common import Log


log = Log.logger


class SalesReturn(object):
    def __init__(self):
        res = http_r.run_main('get', url=sales_return_urls["新建页面初始化"], name="销售退回新建页面初始化")
        self.sold = res["data"]["soldByList"][0]

    @staticmethod
    def query(return_no=""):
        params = {
            "limit": 20, "offset": 0,
            "searchData": {"cancelType": 13001005, "keyWord": return_no}
        }
        res = http_r.run_main('get', url=sales_return_urls["销售退回列表查询"], data=params, name="销售退回列表查询")
        if res["data"]["total"] == 0:
            log.info("销售退回列表未查到数据")
            return
        y_t = res["data"]["list"][0]

        return y_t

    def new_save(self, old_no=""):
        params = {"limit": 20, "offset": 0, "searchData": {"soStatus": "", "cancelType": 13001001, "keyWord": old_no}}
        res = http_r.run_main('get', url=sales_return_urls["新建销售退回列表查询"], data=params, name="新建销售退回列表查询")
        if res["data"]["total"] == 0:
            log.info("没有可供退回的销售订单")
            return
        old_no = res["data"]["list"][0]["soNo"]
        vin = res["data"]["list"][0]["vin"]
        # --------------------------------------------------------------------------------------------------------------
        data = {
            "oldSoNo": old_no,
            "soldBy": self.sold["id"]["userId"],
            "soldByDesc": self.sold["userName"],
            "remark": "备注 - - 测试",
            "abortingReason": "销售退回原因 - - 测试",
            "penaltyAmount": 0.00}
        res = http_r.run_main('post', url=sales_return_urls["销售退回单保存"], data=data, name="销售退回单保存")
        if res["code"] == 400:
            log.info("{},{}".format(old_no, res["message"]))
            return
        return_no = res["data"]["soNo"]

        return return_no, vin

    @staticmethod
    def submit_audit(so_no):
        data = {"soNo": so_no}
        res = http_r.run_main('post', url=sales_return_urls["提交审核"], data=data, name="销售退回提交审核")
        log.info("{}-----提交审核 成功".format(res))


sales_return = SalesReturn()

if __name__ == '__main__':
    sales_return.new_save()

