import json
from common.configHttp import http_r
from interfaceTest.constants import gross_urls
from common import Log


log = Log.logger


class GrossStandard(object):
    def __init__(self):
        pass

    @staticmethod
    def query(vin_str=""):
        params = {
            "offset": 0,
            "limit": 20,
            "searchData": {"inTransitDaysSort": "desc", "vin": vin_str}
        }
        res = http_r.run_main('get', url=gross_urls["毛利列表查询"], data=params, name="综合毛利标准设置列表查询")
        log.info("综合毛利标准设置列表查询: {}".format(res["data"]["total"]))
        if res["data"]["total"] == 0:
            log.info("综合毛利标准设置列表查询-未查到数据")
            return

        return res["data"]["list"]

    def save(self, vin_str):
        item_json = [item for item in self.query(vin_str) if not item["limitStatusDesc"] == "审核中"]
        if len(item_json) == 0:
            log.info("除掉审核中后没有可以保存提交的数据")
            return
        for item in item_json:
            item["estimatedCommission"] = 1  # 预估佣金
            item["discountStandard"] = int(item["directivePrice"]*0.92*0.07)  # 折让标准
            item["derivedStandard"] = 1  # 衍生标准
            item["estimatedGrossProfitStd"] = item["directivePrice"] - item["purchasePrice"] + item["estimatedCommission"] - item["discountStandard"] + item["derivedStandard"]
            item["discountPoints"] = "%.4f" % (item["discountStandard"]/item["directivePrice"])
            for key in list(item.keys()):
                if not item[key]:
                    del item[key]
        log.info("此次设置单车综合毛利标准: {}".format(item_json[0]["estimatedGrossProfitStd"]))
        payload = {
            "itemJson": item_json,
            "planJson": []
        }
        res = http_r.run_main('post', url=gross_urls["列表保存"], data=payload, is_json=1, name="车辆综合毛利标准列表保存")
        log.info(res["data"]["msg"])

        return res["data"]["vinList"]

    def submit_audit(self, vin_list):
        data = {
            "vinStr": ",".join(vin_list)
        }
        data = json.dumps(data)
        res = http_r.run_main('post', url=gross_urls["提交审核"],data=data, name="车辆综合毛利标准提交审核")
        log.info(res)
        audit_no = self.query(",".join(vin_list))[0]["auditNo"]

        return audit_no


gross_standard = GrossStandard()

if __name__ == '__main__':
    cc = ['3LXHU94G7ACFE5D1T']
    dd = ','.join(cc)
    ll = gross_standard.save(dd)
    print(ll)


