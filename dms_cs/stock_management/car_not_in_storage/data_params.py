

def data_params():
    search_data = {
                   "brandCode": "",
                    "seriesCode": "",
                    "modelCode": "",
                    "configCode": "",
                    "productCode": "FPZ-004220 FWS-001475 FNS-001125",
                    "productName": "",
                    "vin": "20200402000000000",
                    "brandName": "",
                    "seriesName": "",
                    "modelName": ""
    }
    params = {
              "limit": 10,
              "offset": 0,
              "searchData": search_data
    }
    data = {
            "header": ["VIN", "产品代码", "品牌", "车系", "车型", "配置", "仓库名称", "库位代码", "发动机号",
                       "钥匙编号", "采购订单编号", "车辆类型", "采购价格", "采购日期", "厂家实际提车日期", "附加成本",
                       "送车人姓名", "承运商名称", "承运车牌号", "收货地址", "发货单号", "供应单位代码", "供应单位名称",
                       "验收人员", "质损状态"],
            "key": ["vin", "productCode", "brandName", "seriesName", "modelName", "configName", "storageCode",
                  "storagePositionCode", "engineNo", "keyNumber", "poNo", "vehicleType", "purchasePrice", "vsPurchaseDate",
                  "realOemPickUpDateStr", "additionalCost", "deliverymanName", "shipperName", "shipperLicense",
                  "shippingAddress", "shippingOrderNo", "vendorCode", "vendorName", "inspector", "marStatus"],
            "fileName": "未入库调拨车辆明细单"
    }

    return params, data



