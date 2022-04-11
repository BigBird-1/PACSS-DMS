import time
from common.configHttp import http_r
from interfaceTest.initialization import initial
from interfaceTest.constants import decoration_urls
from common import Log


log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class DecorationOrder(object):
    def __init__(self):
        pass

    @staticmethod
    def new_save(so_no=""):
        auth_dict = initial.get_audits()
        user_name = auth_dict["用户信息"]['userName']  # 登陆用户信息
        user_id = auth_dict["用户信息"]['id']['userId']
        #  -------------------------------------------------------------------------------------------------------------
        params = {"searchData": {"labourCode": "CSZH001"}}
        res = http_r.run_main('get', url=decoration_urls["装潢项目选择查询"], data=params, name="装潢项目选择查询")
        if res["data"]["total"] == 0:
            log.warning("没有查询到装潢项目")
            return
        project = res["data"]["list"][0]
        #  -------------------------------------------------------------------------------------------------------------
        res = http_r.run_main('get', url=decoration_urls["仓库下拉选择"], name="仓库下拉选择")
        yt = {}
        if not res["data"]["storages"]:
            return
        for item in res["data"]["storages"]:
            yt[item["storageName"]] = item["id"]["storageCode"]
        params = {"limit": 20, "offset": 0, "searchData": {"storageCode": yt["销售精品仓库"], "stockQuantity": "12781001"}}
        res = http_r.run_main('get', url=decoration_urls["装潢配件查询"], data=params, name="装潢配件查询")
        if res["data"]["total"] == 0:
            log.warning("销售精品仓库 - 未查询到库存大于0的配件")
            return
        accessories = res["data"]["list"][0]
        #  -------------------------------------------------------------------------------------------------------------
        params = {"searchData": {"keyWord": so_no}, "limit": 20, "offset": 0}
        res = http_r.run_main('get', url=decoration_urls["销售单查询"], data=params, name="销售单查询")
        order_info = res["data"]["list"][0]
        #  -------------------------------------------------------------------------------------------------------------
        project["upholsterCode"] = project["labourCode"]
        project["upholsterName"] = project["labourName"]
        project["discount"] = 1  # 折扣率
        project["labourAmount"] = 200  # 工时费
        project["realLabourAmount"] = project["labourAmount"]*project["discount"]  # 实收工时费
        project["receiveAmount"] = str(round(project["realLabourAmount"], 2))
        project["accountMode"] = 13991003
        project["consignExterior"] = 12781002

        accessories["remark"] = "配件-备注"
        accessories["partRealSalesPrice"] = accessories["salesPrice"]  # 销售指导价
        accessories["discount"] = 1  # 折扣率
        accessories["partQuantity"] = 1  # 配件数量
        accessories["realPrice"] = accessories["salesPrice"]*accessories["discount"]  # 实际销售单价
        accessories["partSalesAmount"] = accessories["realPrice"]*accessories["partQuantity"]  # 销售金额
        accessories["partCostAmount"] = accessories["costPrice"]*accessories["partQuantity"]  # 配件成本金额
        accessories["partCostPrice"] = accessories["costPrice"]  # 配件成本单价不含税
        accessories["accountMode"] = 13991003
        accessories["storageCode"] = accessories["id"]["storageCode"]
        accessories["partNo"] = accessories["id"]["partNo"]

        for key in list(project.keys()):
            if not project[key]:
                del project[key]

        for key in list(accessories.keys()):
            if not accessories[key]:
                del accessories[key]
        # --------------------------------------------------------------------------------------------------------------
        data = {
            "formJson": {
                "id": {"entityCode": "", "decorationNo": ""}, "sheetCreateDate": current_date,
                "sheetCreatedBy": user_id, "decType": 14051002, "orderWere": user_id,
                "soStatus": 14001001, "completeTag": "", "remark": "",

                "customerNo": order_info["customerNo"], "customerName": order_info["customerName"],
                "contactorName": order_info["contactorName"], "contactorPhone": order_info["phone"],
                "vin": order_info["vin"], "license": "",

                "isFixedAssetsType": "12781002", "fixedAssetsTyp": "", "isFixedAssetsTypeDesc": "否",
                "fixedAssetsTypeDesc": "",

                "brandCode": order_info["brand"], "seriesCode": order_info["series"],
                "modelCode": order_info["model"], "configCode": order_info["config"],
                "colorCode": order_info["color"],
                "brandCodeDesc": order_info["brandName"], "seriesCodeDesc": order_info["seriesName"],
                "modelCodeDesc": order_info["modelName"], "configCodeDesc": order_info["configName"],
                "colorCodeDesc": order_info["colorName"],

                "soNo": so_no, "estimateBeginTime": "", "estimateEndTime": current_date, "completedDate": "",
                "inspectorDesc": "",

                "totalAmount": project["realLabourAmount"]+accessories["partSalesAmount"],
                "sumTotalCostOfAmount": accessories["partCostAmount"], "discountAmount": 0,
                "receiveableAmount": project["realLabourAmount"]+accessories["partSalesAmount"],

                "totalDecAmount": project["realLabourAmount"], "ownerDecAmount": project["realLabourAmount"],

                "partTotalPartAmount": accessories["partSalesAmount"],
                "SumDecorationCostAmount": accessories["partCostAmount"],
                "partOwnerPartAmount": accessories["partSalesAmount"],

                "partTotalDecAmount": 0, "sumTotalCostAmount": 0, "partOwnerDecAmount": 0,
                "guideAmount": 0, "partPresentDecAmount": 0,
                "presentDecAmount": 0,
                "partPresentPartAmount": 0, "realReceiveAmount": 0,
                "consumedIntegralAmount": 0, "consumedIntegral": 0, "consumedRepairFund": 0, "oaFileName": "",
                "oaFileAddress": "", "sheetCreatedByDesc": user_name, "orderWereDesc": user_name, "fixedAssetsType": "",
                "isReplaceFlag": 12781002
            },
            "soPartArr": [accessories],  # 配件
            "soUpholsterSelfArr": [project],  # 项目
            "partArr": [],
            "deletedPart": [],
            "deletedSoPart": [],
            "deletedUpholster": [],
            "replacePartIdArr": "",
            "replaceSoPartIdArr": "",
            "isAdd": "true"
        }
        res = http_r.run_main('post', url=decoration_urls["装潢单保存"], data=data, name="装潢单保存")
        decoration_no = res["data"]["decorationNo"]
        log.info("{}-关联销售装潢单新建成功-{}".format(so_no, decoration_no))

        return decoration_no


decoration_order = DecorationOrder()


if __name__ == '__main__':
    decoration_order.new_save(so_no="SN2203210003")

