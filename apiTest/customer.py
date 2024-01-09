import random
import time
import datetime
from common.configHttp import http_r
from common.randomData import random_mobile, random_name


# ct_no = randomData.random_card()
# 获取当前日期 年月日
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
mobile = random_mobile()
name = random_name()


url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/customerServiceList"
res = http_r.run_main('get', url)
sold_dict = res["data"]["list"]
sold_by = random.choice(list(sold_dict.keys()))
sold_desc = sold_dict[sold_by]
url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/addArriveShop"
come_time = current_time
data = {
    "soldBy": sold_by,
    "visitTime": come_time,
    "visitor": 1
}
res = http_r.run_main('post', url, data=data)
print(res)
url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/flowList"
params = {"s_visit_time": current_date, "e_visit_time": current_date, "sold_by": sold_by, "page": 1, "pageSize": 50}
res = http_r.run_main('get', url, data=params)
flow = random.choice(res["data"]["list"])
if flow["leaveTime"] == "":
    d1 = datetime.datetime.now()
    d2 = d1 + datetime.timedelta(hours=2)
    d3 = d2.strftime("%Y-%m-%d %H:%M:%S")
    flow["leaveTime"] = d3
print(flow)
url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/doEditLeaveTime"
res = http_r.run_main('post', url, data=flow)
print(res)
# ----------------------------------------------------------------------------------------------------------------------
# url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/editFlow"
# params = {"itemId": ""}
# res = http_r.run_main('get', url, data=params)
# detail = res["data"]["detail"]
#
# url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/customerDetail"
# params = {"phone": ""}
# res = http_r.run_main('get', url, data=params)
# detail2 = res["data"]["detail"]
data = {
    "customerName": "二网客户-{}".format(name),
    "contactorMobile": mobile,
    "gender": 10061001,

    "province": 420000,
    "city": 4201,
    "district": 420100,
    "address": "那条街1号",
    "ct_code": 12391007,
    "certificate_no": "Z7158485-1",

    "budget_amount": 1000000,
    "visitor": flow["visitor"],
    "visitTime": flow["visitTime"],
    "leaveTime": flow["leaveTime"],
    "mediaType": 12983004,  # 渠道大类
    "media_type_desc": "二网零售",
    "cusSource": 13111000,  # 客户来源
    "cus_source_desc": "二网",
    "customerFlow": 14601001,  # 客流性质
    "soldBy": sold_by,
    "sold_by_desc": sold_desc,
    "intentBrand": "CADILLAC",
    "intent_brand_name": "凯迪拉克",
    "intentSeries": "FCX-000004",
    "intent_series_name": "CT7",
    "usedCarChange": 12781002,  # 二手车置换
    "isDrive": 12781002,  # 是否试乘试驾
    "remark": "测试 -- 备注",
    "isWeb": 0,
    "pay_amount_mode": 96131001,  # 付款方式
    "pre_time": 13541009,  # 预计购车日期
    "offer_amount": 2000000,
    "recommendBrand": "CADILLAC",
    "recommendSeries": "FCX-000004",
    "buy_purpose": 13461001,
    "used_brand": 10000001,
    "used_series": 10000001,
    "competitor_brand": 10000001,
    "competitor_series": 10000001,
    "item_id": flow["itemId"]
}
print(data)
url = "https://dms.t.hxqcgf.com/apigateway/crm-sales/Api/V1/CustomerFlow/addFlow"
# url = "http://10.0.15.134:18080/view/qa-pre/job/PACSS-CRM-PC-preRelease/"
res = http_r.run_main('post', url, data=data)
print(res)




