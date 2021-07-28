from interfaceTest.constants import stock_entry_urls
from common.configHttp import http_r
from interfaceTest.initialization import initial
from common import Log


log = Log.logger


class VehiclesStockEntry(object):
    def __init__(self):
        res = http_r.run_main('get', url=stock_entry_urls["车辆入库下拉初始化"], name="车辆入库下拉初始化")
        self.type_dict = {}
        for item in res["data"]["stockInTypeList"]:
            self.type_dict[item["statusDesc"]] = item["statusCode"]

    def query(self, se_no="", vin="", flag=None):
        """入库单查询"""
        params = {"limit": 20, "offset": 0, "searchData": {"showNoEntryItem": 12781002, "seNo": se_no, "vin": vin}}
        res = http_r.run_main('get', url=stock_entry_urls["入库单查询"], data=params, name="入库单查询", flag=flag)
        if res["data"]["total"] == 0:
            log.error("{},{} 未查到入库单数据".format(se_no, vin))
            return
        se_no_dict = res["data"]["list"][0]
        stock_in_type = se_no_dict["stockInType"]
        se_no = se_no_dict["seNo"]
        is_all_finished = se_no_dict["isAllFinished"]
        params = {"limit": 20, "offset": 0, "searchData": {"statusCode": self.type_dict[stock_in_type], "seNo": se_no}}
        res = http_r.run_main('get', url=stock_entry_urls["入库单车辆信息"], data=params, name="入库单内车辆信息", flag=flag)
        if res["data"]["total"] == 0:
            log.error("入库单: {} 内没有车辆".format(se_no))
            return
        vehicle_info = res["data"]["list"][0]
        y_t = {
            "车辆信息": vehicle_info,
            "入库单号": se_no
        }

        return y_t

    @staticmethod
    def check_car(se_no, vin_str, flag=None):
        """验收"""
        auth_dict = initial.get_audits()
        user_name = auth_dict["用户信息"]['userName']
        user_id = auth_dict["用户信息"]['id']['userId']
        data = {"seNo": se_no,
                "vinList": vin_str,
                "inspector": user_id,
                "inspectorDesc": user_name,
                "marStatus": 13061002,
                "inspectionResult": 13351002}
        res = http_r.run_main("post", url=stock_entry_urls["批量验收保存"], data=data, name="批量验收保存", flag=flag)
        log.info("{}--{} 验收通过".format(res, vin_str))

    @staticmethod
    def submit_audit(se_no, vin_str, flag=None):
        """提交审核"""
        data = {
            "seNo": se_no,
            "vinS": vin_str,
            "orderType": 10
        }
        res = http_r.run_main("post", url=stock_entry_urls["提交审核"], data=data, name="车辆入库提交审核", flag=flag)
        log.info("{},{} 提交审核成功".format(res, vin_str))

    @staticmethod
    def in_store(se_no, vin_str, flag=None):
        """入库"""
        data = {"seNo": se_no, "vins": vin_str}
        res = http_r.run_main('post', url=stock_entry_urls["手动入库"], data=data, name="车辆入库手动入库", flag=flag)
        if res["code"] == 400:
            log.error("手动入库失败: {}".format(res["message"]))
            return
        log.info("{}--{}--手动入库成功".format(res, vin_str))

    @staticmethod
    def rebate_confirm(se_no, flag=None):
        """调拨入库佣金财务确认"""
        res = http_r.run_main('get', url=stock_entry_urls["返利财务确认列表initData"], name="返利财务确认列表initData", flag=flag)
        apply_code = res["data"]["inSerailApplyCode"]
        business_type = res["data"]["inBusinessType"]
        params = {"limit": 20, "offset": 0,
                  "searchData": {
                      "inSerailApplyCode": apply_code,
                      "inBusinessType": business_type,
                      "remark": se_no}}
        res = http_r.run_main('get', url=stock_entry_urls["返利财务确认列表查询"], data=params, name="返利财务确认列表查询", flag=flag)
        if res['data']["total"] == 0:
            log.error("返利财务确认列表查询-未查到返利数据")
            return
        rebate_order = res['data']["list"][0]
        rebate_no = rebate_order["rebate_no"]
        if rebate_order["status_name"] == "未确认":
            params = {"rebateNo": rebate_no}
            res = http_r.run_main('get', url=stock_entry_urls["财务确认编辑页"], data=params, name="财务确认编辑页", flag=flag)
            rebate_data = res["data"]["rebateTable"]
            for key in list(rebate_data.keys()):
                if not rebate_data[key]:
                    del rebate_data[key]
            data = {
                "rebateNo": rebate_no, "pageFlag": 2,
                "paramsStr": rebate_data
            }
            res = http_r.run_main('post', url=stock_entry_urls["财务确认保存"], data=data, name="财务确认保存", flag=flag)
            log.info("{}--调拨入库佣金财务已操作!".format(res))
        elif rebate_order["status_name"] == "已作废":
            log.error("返利单据已作废-不可操作")
            return


stock_entry = VehiclesStockEntry()


if __name__ == '__main__':
    stock_entry.rebate_confirm("VD2011270003")
