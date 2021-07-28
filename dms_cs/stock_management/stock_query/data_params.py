

def data_params():
    params = {
              "searchData": {"beOverdue": "0",  # 是否逾期
                             "manufactureStartDate": "",
                             "manufactureEndDate": "",
                             "firstStockInStartDate": "",
                             "firstStockInEndDate": "",
                             "firstStockOutStartDate": "",
                             "firstStockOutEndDate": "",
                             "lastStockInStartDate": "",
                             "lastStockInEndDate": "",
                             "lastStockOutStartDate": "",
                             "lastStockOutEndDate": "",
                             # "stockSta": 13041002,  # 库存状态
                             # "inStockType": 13071001,  # 入库类型
                             # "outStockType": 13241001,  # 出库类型
                             "orderStractStartDate": "",
                             "orderStractEndDate": "",
                             "hasCertificate": "",
                             # "isTestDriveCar": 12781002,  # 试乘试驾
                             # "statusDispatched": 13051001,  # 配车状态
                             "vin": "",
                             "brandCode": "",  # 品牌代码
                             "seriesCode": "",  # 车系代码
                             "modelCode": "",  # 车型代码
                             "brandName": "",  # 品牌
                             "seriesName": "",  # 车系
                             "modelName": "",  # 车型
                             "productName": "",  # 产品名称
                             "productCode": "",  # 产品代码
                             "keyNumber": "",
                             "configCode": "",
                             "colorCode": "",
                             "innerColorCode": "",
                             # "statusMar": 13061001,  # 质损状态
                             # "inTransitDays": "asc"  # 库龄排序
    },
              "limit": 10,
              "offset": 0
    }

    data = {
            "header": ["经销商简称", "是否试乘试驾", "是否有合格证", "是否虚销车", "质损状态", "配置", "颜色", "VIN",
                       "仓库", "发动机号", "合格证号", "钥匙编号", "采购日期", "采购价格", "车厂指导价", "销售指导价",
                       "批售指导价", "库位", "产品代码", "产品名称", "品牌", "车系", "车型", "库存状态", "库龄", "配车状态",
                       "生产日期", "入库类型", "首次入库日期", "首次入库单号", "最后入库日期", "最后入库单号", "出库类型",
                       "首次出库日期", "首次出库单号", "最后出库日期", "最后出库单号","出厂日期", "备注", "排气量",
                       "排放标准", "车辆免息期", "资金来源", "已知佣金合计", "限价金额", "车辆内饰", "车辆外饰"],
            "key": ["entityName", "isTestDriveCar", "hasCertificate", "fakeFlag", "marStatus", "configName", "colorName",
                  "vin", "storageName", "engineNo", "certificateNumber", "keyNumber", "vsPurchaseDate", "purchasePrice",
                  "oemDirectivePrice", "directivePrice", "wholesaleDirectivePrice", "storagePositionCode", "productCode",
                  "productName", "brandName", "seriesName", "modelName", "stockStatus", "inTransitDays", "dispatchedStatus",
                  "manufactureDate", "stockInType", "firstStockInDate", "firstSeNo", "latestStockInDate", "lastSeNo",
                  "stockOutType", "firstStockOutDate", "firstSdNo", "latestStockOutDate", "lastSdNo", "factoryDate",
                  "remark", "exhaustQuantity", "dischargeStandard", "interestholiDay", "sourceName", "rebate",
                    "limitPrice", "innerColor", "outerColor"],
            "searchData": {"beOverdue": "0", "manufactureStartDate": "", "manufactureEndDate": "",
                           "firstStockInStartDate": "", "firstStockInEndDate": "", "firstStockOutStartDate": "",
                           "firstStockOutEndDate": "", "lastStockInStartDate": "", "lastStockInEndDate": "",
                           "lastStockOutStartDate": "", "lastStockOutEndDate": "", "orderStractStartDate": "",
                           "orderStractEndDate": ""},
            "fileName": "车辆库存查询"
    }

    return params, data
