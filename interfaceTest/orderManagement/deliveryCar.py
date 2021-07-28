from common.configHttp import http_r
from interfaceTest.constants import delivery_urls
from interfaceTest.wfsAudit import to_do
from common import Log

log = Log.logger


class DeliveryCar(object):
    def __init__(self):
        pass

    @staticmethod
    def dispatched_confirm(so_no):
        """配车确认"""
        params = {"searchData": {"soStatus": 13011025, "keyWord": so_no}, "limit": 20, "offset": 0}
        res = http_r.run_main('get', url=delivery_urls["交车确认列表页查询"], data=params, name="交车确认列表页查询")
        if res["data"]["total"] == 1:
            if res["data"]["list"][0]["isDispatchedConfirm"] == 12781002:
                data = {"soNo": so_no}
                res = http_r.run_main('post', url=delivery_urls["配车确认"], data=data, name="配车确认审核")
                return res
            else:
                return "已配车确认"
        else:
            log.error("配车确认-交车确认列表未查到数据")
            return

    @staticmethod
    def file_up(so_no):
        file_path = r"C:\Users\cpr264\Desktop\JPG测试图片.jpg"
        files = [("file", ("JPG测试图片.jpg", open(file_path, 'rb'), "image/jpeg"))]
        res = http_r.run_main('post', url=delivery_urls["交车上传附件"], files=files, name="交车上传附件")
        file_data = eval(res["data"])
        data = {
            "soNo": so_no,
            "oaAttachFileId": file_data["id"]["fileId"],
            "remark": "交车确认无商业险审核 -- 备注测试"}
        res = http_r.run_main('post', url=delivery_urls["附件外网地址"], data=data, name="获取附件外网地址")
        vehicle_file = res["data"]["vehicleDeliveryExtranetFile"]
        log.info("{}---附件外网地址: {}".format(res, vehicle_file))
        del data["oaAttachFileId"]
        data["vehicleDeliveryExtranetFile"] = vehicle_file
        res = http_r.run_main('post', url=delivery_urls["交车确认提交审核"], data=data, name="交车确认提交审核")
        log.info(res)

    @staticmethod
    def query(self, so_no=""):
        params = {"searchData": {"soStatus": 13011025, "keyWord": so_no}, "limit": 20, "offset": 0}
        res = http_r.run_main('get', url=delivery_urls["交车确认列表页查询"], data=params, name="交车确认列表页查询")
        if res["data"]["total"] == 0:
            log.error("交车确认列表页查询未查到数据")
            return
        return res["data"]["list"][0]

    def delivery(self, so_no, vin):
        y_t = self.query(so_no)
        params = {"soNo": so_no}
        res = http_r.run_main('get', url=delivery_urls["是否需要交车提示"], data=params, name="是否需要交车提示")
        log.info(res)
        params = {"soNo": so_no, "vin": vin}
        # ----------------------------------------------------------------------------------------------------------
        if y_t["businessType"] == "一般销售":
            res = http_r.run_main('get', url=delivery_urls["交车确认之前的校验"], data=params, name="交车确认之前的校验")
            log.info(res)
            if res["data"]["code"] == -1:
                log.error(res["data"]["message"])
                return
            res = http_r.run_main('get', url=delivery_urls["判断交车确认无商业险审核"], data=params, name="判断交车确认无商业险审核")
            log.info(res)
            if res["data"]["code"] == -1:
                log.info(res["data"]["message"])
                self.file_up(so_no)
                to_do.audit_flow(so_no)
                if not self.query(so_no):
                    log.error("交车确认无商业险审核后订单在交车确认列表里查不到,请核实")
                    return
        # ----------------------------------------------------------------------------------------------------------
        res = http_r.run_main('get', url=delivery_urls["车辆返利页面"], data=params, name="进入车辆返利页面")
        param_json = res["data"]["tvc"]
        param_json["rebate"] = res["data"]["rebate"]
        param_json["directivePrice"] = res["data"]["tvs"]["directivePrice"]
        param_json["venderLocalCheck"] = 96151002  # 是否厂家本地考核
        if res["data"]["fakeFlag"] == 12781002:
            param_json["deliveryCommission"] = 12000  # 交车佣金
            param_json["rebate"] += 12000
            for key in list(param_json.keys()):
                if not param_json[key]:
                    param_json[key] = 0
        data = {
            "soNo": so_no, "vin": res["data"]["tvc"]["id"]["vin"], "venderLocalCheck": 96151002,
            "paramJson": param_json}
        res = http_r.run_main('post', url=delivery_urls["车辆返利保存"], data=data, name="车辆返利保存")
        log.info(res)


delivery_car = DeliveryCar()


if __name__ == '__main__':
    delivery_car.delivery("SN2104150004", "2TWBX9GAXF8PREU7Y")
























