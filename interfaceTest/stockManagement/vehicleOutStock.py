from common.configHttp import http_r
from interfaceTest.constants import out_stock_urls
from common import Log


log = Log.logger


class OutStock(object):
    def __init__(self):
        res = http_r.run_main('get', url=out_stock_urls["车辆出库initData"], name="车辆出库initData")
        self.out_type_dict = {}
        for item in res["data"]["stockOutTypeList"]:
            self.out_type_dict[item["statusDesc"]] = item['statusCode']
        self.return_reason = ""

    @staticmethod
    def query_order(sd_no="", vin="", flag=None):
        params = {"userMock": False, "offset": 0, "limit": 20,
                  "searchData": {
                      "sdNo": sd_no, "stockOutType": "", "isAllFinished": "", "vin": vin
                  }}
        res = http_r.run_main('get', url=out_stock_urls["出库单选择查询"], data=params, name="出库单选择查询", flag=flag)
        log.info("出库单选择查询: {}".format(res["data"]["total"]))
        if res["data"]["total"] == 0:
            log.error("出库单选择查询-未查到出库单数据")
            return
        sd_no_dict = res["data"]["list"][0]
        stock_out_type = sd_no_dict["stockOutType"]
        sd_no = sd_no_dict["sdNo"]
        is_all_finished = sd_no_dict["isAllFinished"]
        params = {"userMock": False, "offset": 0, "limit": 20, "searchData": {"sdNo": sd_no}}
        res = http_r.run_main('get', url=out_stock_urls["出库单车辆信息"], data=params, name="出库单车辆信息", flag=flag)
        if res["data"]["total"] == 0:
            log.error("出库单:{}内没有车辆".format(sd_no))
            return
        vehicle_info = res["data"]["list"][0]
        is_finished = vehicle_info["isFinished"]  # 是否入账
        stock_status = vehicle_info["stockStatus"]  # 库存状态

        return vehicle_info

    def create_order(self, out_type, vin, flag=None):
        params = {
            "userMock": False, "offset": 0, "limit": 20,
            "searchData": {"vin": vin},
            "stockOutType": self.out_type_dict[out_type]
        }
        res = http_r.run_main('get', url=out_stock_urls["新增出库类型查询"], data=params, name="新增出库类型查询", flag=flag)
        if res["data"]["total"] == 0:
            log.error("{}在新增{}里未查到".format(vin, out_type))
            return
        out_info = res["data"]["list"][0]
        data = {
            "userMock": False,
            "soNo": out_info["soNo"],
            "vin": vin,
            "stockOutType": self.out_type_dict[out_type]}
        if out_info["soNo"] is None:
            data["soNo"] = ""
        res = http_r.run_main('post', url=out_stock_urls["新增出库单"], data=data, name="新增出库单", flag=flag)

        sd_no = res["data"]["tvsd"]["id"]["sdNo"]

        return sd_no

    def submit_audit(self, vin_1, sd_no, out_type, flag=None):
        self.return_reason = "测试 - {}".format(out_type)
        data = {
            "vin": vin_1,
            "sdNo": sd_no,
            "stockOutType": self.out_type_dict[out_type],
            "returnReason": self.return_reason,
            "orderType": 10
        }
        res = http_r.run_main('post', url=out_stock_urls["出库车辆提交审核"], data=data, name="出库车辆提交审核", flag=flag)
        log.info(res)

    def out_store(self, sd_no, flag=None):
        data = {"userMock": False, "sdNo": sd_no, "returnReason": self.return_reason}
        res = http_r.run_main('post', url=out_stock_urls["手动出库"], data=data, name="手动出库", flag=flag)
        if res["code"] == 400:
            log.error("出库失败: {}".format(res["message"]))
            return
        log.info("{}---手动出库成功,-----(出库完成)-----".format(res))


out_stock = OutStock()

if __name__ == '__main__':
    out_stock.out_store("VD2202210001")








