import random
import string
import time
from decimal import Decimal


def new_shipping_car():
    # 生成17位vin 大写字母数字随机组合
    vin = ''.join(random.sample(string.ascii_uppercase + string.digits, 17))
    # 采购价格，税率，不含税采购价，税额
    purchase_price = Decimal(660000).quantize(Decimal('0.00'))
    tax = Decimal(round(random.uniform(0, 1), 2)).quantize(Decimal('0.00'))
    no_tax_vehicle_cost = Decimal(purchase_price/(1 + tax)).quantize(Decimal('0.00'))
    tax_amount = Decimal(purchase_price - purchase_price/(1+tax)).quantize(Decimal('0.00'))
    # 获取当前日期 年月日
    fake_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 构造请求数据
    new_data = {
            "paramJson": {"businessType": 13071002,  # 业务类型*
                          "vendorCode": "888888888888",  # 供应商代码*
                          "vendorName": "OEM",  # 供应商名称*
                          "isLargeConsumer": 12781002,  # 是否大客户*

                          "productCode": "FPZ-004199 FWS-001460 FNS-001111",  # 产品代码*
                          "factoryModelName": "Q50L 2.0T进取版",  # 厂家车型*
                          "directivePrice": 100000,  # 销售指导价 （带出）
                          "factoryDirectivePrice": "",  # 厂家指导价  （带出）

                          "id": {"entityCode": "", "vin": vin},
                          "sourceCode": "4576",  # 资金来源*
                          "dischargeStandard": 30101008,  # 排放标准*
                          "vehicleType": 80151001,  # 车辆类型*
                          "interestholiDay": "200",  # 车辆免息天数*
                          "acceptBillDay": "200",  # 承兑开票天数*
                          "engineNo": "",  # 发动机号
                          "purchasePrice": str(purchase_price),  # 采购价格*
                          "tax": str(tax),  # 税率*
                          "notaxVehicleCost": 0,  # 不含税采购价* （自动算）
                          "taxAmount": 0,  # 税额（自动算）

                          "fakeFlag": random.choice([12781002, 12781001]),  # 是否虚销
                          "fakeDate": "",  # 虚销日期

                          "shippingDate": fake_date,  # 发车日期
                          "arrivingDate": fake_date,  # 预计到货日期
                          "shippingOrderNo": "",  # 货号
                          "carryOrderNo": "",  # 运输单号
                          "deliverymanName": "",  # 运输联系人
                          "shipperName": "",  # 运输商
                          "certificateLocated": "",  # 合格证所在地
                          "certificateNumber": "",  # 合格证编号
                          "vehiclePerson": "",  # 接车人
                          "manufactureRebate": "",  # 厂家返利
                          "shippingAddress": "",  # 收货地址
                          "foNo": "",  # 厂家订单编号
                          "poNo": ""},  # 采购计划单号
            "standardCommission": "2500.00",  # 标准提车佣金
            "deliveryCommission": "",  # 标准交车佣金
            "isAdd": "true"
    }
    if new_data["paramJson"]["fakeFlag"] == 12781001:
        new_data["paramJson"]["fakeDate"] = fake_date  # 虚销日期
    # 构造查询参数
    params = {
            "searchData": {"shippingStartDate": "",  # 发车开始日期
                           "shippingEndDate": "",  # 发车结束日期
                           "vendorCode": "",  # 供应商
                           "productCode": "",  # 产品代码
                           "isInStock": 12781002,  # 是否入库
                           "arrivingStartDate": "",  # 预计到货开始日期
                           "arrivingEndDate": "",  # 预计到货结束日期
                           "vin": "WKK125JUH36251J01",  # 车架号
                           "shippingOrderNo": "",  # 货号
                           "foNo": "",  # 厂家订单编号
                           "createStartDate": "",  # 制单开始日期
                           "createEndDate": "",  # 制单结束日期
                           "vendorName": ""},  # 供应商名称
            "limit": 10,
            "offset": 0
    }

    excel_data = {
            "header": ["VIN", "标准提车佣金", "标准交车佣金", "供应商名称", "发动机号", "发车日期", "预计到货日期",
                       "制单日期", "接车人", "产品代码", "产品名称", "采购价格","收货地址", "是否入库", "入库单号",
                       "业务类型"],
            "key": ["vin", "standardCommission", "deliveryCommission", "vendorName", "engineNo", "shippingDateStr",
                  "arrivingDateStr", "createDateStr", "vehiclePerson", "productCode", "productName", "purchasePrice",
                  "shippingAddress", "isInStock", "seNo", "businessTypeDesc"],
            "searchData": {"shippingStartDate": "", "shippingEndDate": "", "vendorCode": "", "productCode": "",
                           "isInStock": 12781002, "arrivingStartDate": "", "arrivingEndDate": "", "vin": "",
                           "shippingOrderNo": "", "foNo": "", "createStartDate": "", "createEndDate": "",
                           "vendorName": ""},
            "fileName": "在途车辆管理"
    }

    return new_data, params, excel_data
