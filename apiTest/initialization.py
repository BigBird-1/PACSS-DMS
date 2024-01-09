import random
from common.configHttp import http_r
from apiTest.constants import globals_urls
from common import Log


log = Log.logger


class Initialization(object):
    @staticmethod
    def get_audits():
        res = http_r.run_main("get", url=globals_urls["登录用户信息"], name="获取登录用户信息")
        user_info = res["data"]["sysUser"]
        base_user = res["data"]["baseUser"]
        groups = list(res["data"]["groups"].keys())
        group_code = []  # 审批权限
        for i in res["data"]["audits"].keys():
            group_code.append(i)
        options = res["data"]["options"]  # 选项权限 例 {4010ZCCK: "整车仓库"}
        res = http_r.run_main('get', url=globals_urls["选项权限tree"], name="选项权限tree")
        all_options = {}
        for i in range(len(res["data"])):
            for item in res["data"][i]["children"]:
                all_options[item["id"]] = item["label"]
        auth_options = {}
        for key in all_options.keys():
            if key not in options.keys():
                auth_options[all_options[key]] = 12781002
            else:
                auth_options[all_options[key]] = 12781001
        auth_dict = {
            "用户信息": user_info,
            "基础用户": base_user,
            "品牌分组": groups,
            "审批权限表": group_code,
            "选项权限": auth_options
        }

        return auth_dict

    @staticmethod
    def vehicle_main(product_code=""):
        product_params = {
            "searchData": {"productCodeKey": "false", "isValid": "12781001", "productCode": product_code}
        }
        res = http_r.run_main('get', url=globals_urls["车辆主数据"], data=product_params, name="车辆主数据查询")

        return res["data"]["list"][0]

    @staticmethod
    def customer_info(phone="", customer_type=""):
        type_dict = {"个人": 10181001, "公司": 10181002, "本经销商": 10181003}
        if customer_type == "":
            customer_type = "个人"
        params = {"limit": 20, "offset": 0, "searchData": {"keyWord": phone, "customerType": type_dict[customer_type],
                                                           "funCode": "001"}}
        res = http_r.run_main('get', url=globals_urls["选择客户列表查询"], data=params, name="选择客户列表查询")
        if res["data"]["total"] == 0:
            log.info("选择客户列表查询-未查到数据")
            return
        content = res["data"]["list"][0]  # 选择第一个
        customer_no = content["customerNo"]  # 潜客编号
        item_id = content["itemId"]
        customer_name = content["customerName"]
        params = {"customerNo": customer_no, "itemId": item_id}
        client = http_r.run_main('get', url=globals_urls["客户信息"], data=params, name="客户信息info")

        return client

    @staticmethod
    def basic_params():
        res = http_r.run_main('get', url=globals_urls["基础参数设置"], name="基础参数设置查询-index")
        sales_params = {}
        y_t = "12781001"  # 因为基础参数存在两个自动出库参数,这里做特殊处理
        for k, v in res["data"]["defaultParam"].items():
            sales_params[v["itemDesc"]] = v["defaultValue"]
            if v["itemDesc"] == "自动出库" and v["id"]["itemCode"] == "8004":
                y_t = v["defaultValue"]
        sales_params["自动出库"] = y_t
        return sales_params


initial = Initialization()


if __name__ == '__main__':
    client_info = initial.customer_info(phone="17785459652")
    print(client_info)
    # sales_params1 = initial.basic_params()
    # print(sales_params1)
    # print(sales_params1["含税成本价"])
    # print(sales_params1["销售指导价"])
    # auth_dict1 = initial.get_audits()
    # print(auth_dict1["选项权限"])
    # auth_dict1 = initial.get_audits()
    # print(auth_dict1["用户信息"]["financialCode"] + auth_dict1["用户信息"]["entityShortName"])











