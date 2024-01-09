from readConfig import read_config


base_url = read_config.get_http("base_url")
shipping_cars = 2  # 在途车采购数量
is_deputy_delivery = 12781002  # 是否代交车

globals_urls = {
    "基础参数设置": base_url + "/system/defaultPara/index",
    "登录用户信息":  base_url + "/admin/user/info",
    "选项权限tree": base_url + "/admin/authOption/getAuthOptionTree",

    "车辆主数据": base_url + "/sales/vehicleMasterData/getVehicleMainDataList",
    "选择客户列表查询": base_url + "/sales/salesDepositOrder/queryPoCustomer",
    "客户信息": base_url + "/sales/salesDepositOrder/returnPoCustomerInfo",
}

deposit_urls = {
    "新增页面下拉框初始化": base_url + "/sales/salesDepositOrder/initData",
    "获取预定金最低金额": base_url + "/sales/salesDepositOrder/getDepositRule",
    "预订单列表查询": base_url + "/report/salesOrderFeignUtils/searchDepositList",
    "预订单保存": base_url + "/sales/salesDepositOrder/save",
    "预订单提交审核": base_url + "/sales/salesDepositOrder/submitOaAuditingHandle",
    "预订单复制": base_url + "/sales/salesDepositOrder/copySalesDepositOrder",
    "预订单作废": base_url + "/sales/salesDepositOrder/invalid",
    "城市查询": base_url + "/sales/salesDepositOrder/getCityList",
    "动力类型查询": base_url + "/report/salesOrderFeignUtils/getProductList",
    "明细初始化": base_url + "/sales/salesDepositOrder/indexInfo",
    "配件用品查询": base_url + "/report/salesOrderFeignUtils/getPartStockList",
    "衍生服务险list": base_url + "/valueadded/vehicleExtension/api/getGmsExtPackageList",
    "精品查询页面初始化": base_url + "/report/salesOrderFeignUtils/getInitData",
    "查询代交车": base_url + "/sales/salesOrder/queryVinInfo",

    "获取产品内/外饰色": base_url + "/sales/shippingNotify/getColorList",
    "获取选装包": base_url + "/sales/shippingNotify/getOptionalList",

    "检查身份证信息": base_url + "/gms/idCardInfo/checkIdCardInfo",
    "老单据": base_url + "/sales/salesDepositOrder/isOldOrderNo",
    "新建预订退回": base_url + "/sales/salesDepositReturn/getInfo",
    "预订退回单保存": base_url + "/sales/salesDepositReturn/save",
    "预订退回单提交审核": base_url + "/sales/salesDepositReturn/submitOaReturnAuditingHandle",

    "预订单查询列表查询": base_url + "/report/salesOrderFeignUtils/searchDepositList"
}

deposit_return_urls = {
    "列表下拉初始化": "/sales/salesDepositReturn/index",

}

advances_urls = {
    "预收款登记列表查询": base_url + "/report/soPrePayReport/queryList",
    "预收款登记收款界面": base_url + "/sales/prepaidFeeReg/getRegIstrationPageDetail",
    "预收款登记收款保存": base_url + "/sales/prepaidFeeReg/save",
}

shipping_urls = {
    "新增页面初始化": base_url + "/sales/shippingNotify/getShippingNotifyInfo",
    "标准在途天数": base_url + "/sales/shippingNotify/getAvgTransitDays",
    "标准周转天数": base_url + "/sales/shippingNotify/getAvgTurnoverDays",
    "在途车保存": base_url + "/sales/shippingNotify/saveShippingNotify",
    "在途车辆管理列表查询": base_url + "/sales/shippingNotify/getShippingNotifyList",
    "获取动力类型": base_url + "/report/salesOrderFeignUtils/getProductList",

    "获取资金成本规则": base_url + "/sales/shippingNotify/getCapitalCostList",
    "获取指定资金成本": base_url + "/gms/gmsVehCostRule/getVehCostRuleById",
    "资金成本设置保存": base_url + "/sales/shippingNotify/saveShippingNotifyCaptialCost",

    "获取选装包": base_url + "/sales/shippingNotify/getOptionalList",
    "获取产品内/外饰色": base_url + "/sales/shippingNotify/getColorList",

    "在途车转入库": base_url + "/sales/shippingNotify/commitShippingNotifyToStore",
    "在途车删除": base_url + "/sales/shippingNotify/deleteShippingNotify",


    "检查是否虚销": base_url + "/sales/shippingNotify/checkFakeFlag",
    "是否存在库存": base_url + "/sales/shippingNotify/checkExsitInStock"
}

gross_urls = {
    "列表保存": base_url + "/sales/vehicleLimitPrice/editVehicleGrossProfitPlan",
    "提交审核": base_url + "/sales/vehicleLimitPrice/applyPriceLimitAudit",
    "毛利列表查询": base_url + "/sales/vehicleLimitPrice/getVehicleGrossProfitPlanSummary"
}

stock_entry_urls = {
    "车辆入库下拉初始化": base_url + "/sales/vsStockEntry/initData",
    "入库单查询": base_url + "/sales/vsStockEntry/searchAllSeNo",
    "入库单车辆信息": base_url + "/sales/vsStockEntry/searchVehicleInfo",
    "批量验收保存": base_url + "/sales/vsStockEntry/saveCheckOneCarAll",
    "提交审核": base_url + "/sales/vsStockEntry/postBatchAudit",
    "手动入库": base_url + "/sales/vsStockEntry/saveStock",

    "返利财务确认列表查询": base_url + "/valueadded/rebateFinancialConfirm/ajaxList",
    "返利财务确认列表initData": base_url + "/valueadded/rebateFinancialConfirm/initData",
    "财务确认详情页": base_url + "valueadded/rebateFinancialConfirm/getRebateOrderInfo",
    "财务确认编辑页": base_url + "/valueadded/rebateFinancialConfirm/edit",
    "财务确认保存": base_url + "/valueadded/rebateFinancialConfirm/update",
}

out_stock_urls = {
    "车辆出库initData": base_url + "/sales/vehicleOutStock/initData",
    "出库单选择查询": base_url + "/sales/vehicleOutStock/vehicleOutStockQuery",
    "出库单车辆信息": base_url + "/sales/vehicleOutStock/vehicleOutStockList",
    "新增出库类型查询": base_url + "/sales/vehicleOutStock/vehicleOutStockNewAdd",
    "新增出库单": base_url + "/sales/vehicleOutStock/saveDeliveryOrder",
    "出库车辆提交审核": base_url + "/sales/vehicleOutStock/submitAudit",

    "手动出库": base_url + "/sales/vehicleOutStock/vehiclesDelivery",

}

sales_urls = {
    "销售订单列表下拉初始化": base_url + "/sales/salesOrder/initData",
    "销售订单保存": base_url + "/sales/salesOrder/saveSalesOrder",
    "提交审核": base_url + "/sales/salesOrder/submitOAReview",
    "配车审核": base_url + "/sales/salesOrder/dispatchedAudit",
    "销售订单列表查询": base_url + "/report/salesOrderFeignUtils/searchSalesOrder",
    "选中vin返回信息": base_url + "/sales/salesOrder/returnVinInfo",

    "财务驳回订单状态": base_url + "/sales/transferOrder/getTransferOderStatus",
    "财务驳回订单是否收过款": base_url + "/sales/orderAudit/checkSalesOrderReceive",
    "财务驳回确定": base_url + "/sales/orderAudit/financialReject",

    "库存维护列表查询": base_url + "/report/vehicleStock/getVehicleStockList",
    "库存车辆查询": base_url + "/sales/salesOrder/queryVinInfo"
}

decoration_urls = {
    "装潢录入列表初始化": base_url + "/valueadded/decorationOrderQuery/init",
    "装潢项目选择查询": base_url + "/valueadded/decorationManage/getList",
    "仓库下拉选择": base_url + "/parts/decorationPartOut/addDecorationPartOutItemInitData",
    "装潢配件查询": base_url + "/parts/decorationPartOut/getPartStockList",
    "装潢单保存": base_url + "/valueadded/decorationOrder/saveDecorationOrder",
    "销售订单客户info": base_url + "/sales/salesQuery/getSalesCustomerInfo",
    "获取品牌": base_url + "/master/carBase/getBrandList",
    "获取车系": base_url + "/master/carBase/getSeriesList",
    "获取车型": base_url + "/master/carBase/getModelList",
    "获取配置": base_url + "/master/carBase/getConfigList",
    "获取外饰色": base_url + "/master/carBase/getSeriesOutColorMappingList",
    "新增初始化": base_url + "/valueadded/decorationOrder/initEdit",
    "销售单查询": base_url + "/sales/salesQuery/insSearchSalesOrder",

}

sales_return_urls = {
    "新建销售退回列表查询": base_url + "/sales/orderCancel/searchSalesClose",
    "退回单带出原单信息": base_url + "/sales/salesOrder/newSalesCancelDo",
    "销售退回单保存": base_url + "/sales/salesOrder/saveCancel",
    "新建页面初始化": base_url + "/sales/salesOrderReturn/initData",
    "提交审核": base_url + "/sales/salesOrderReturn/submitSalesOrderReturnOaAudit",
    "销售退回列表查询": base_url + "/sales/orderCancel/searchSalesReturn",
}

delivery_urls = {
    "交车上传附件": base_url + "/system/attachInfo/api/fileUpload",
    "附件外网地址": base_url + "/sales/salesOrderDelivery/saveVehicleDeliveryUploadFile",
    "交车确认提交审核": base_url + "/sales/salesOrderDelivery/submitOaAuditing",
    "交车确认之前的校验": base_url + "/sales/salesOrderDelivery/checkBeforeDeliveryConfirm",
    "判断交车确认无商业险审核": base_url + "/sales/salesOrderDelivery/checkIsHasCommercialInsurance",
    "车辆返利页面": base_url + "/sales/salesOrderDelivery/getVehicleRebate",
    "车辆返利保存": base_url + "/sales/salesOrderDelivery/submitVehicleDelivery",
    "交车确认列表页查询": base_url + "/report/salesOrderFeignUtils/salesOrderDeliveryList",
    "是否需要交车提示": base_url + "/sales/salesOrderDelivery/needConfirm",

    "配车确认": base_url + "/sales/salesOrder/dispatchedAudit"
}

transfer_urls = {
    "客户选择页查询": base_url + "/report/partCustomer/partContomerList",
    "车辆信息": base_url + "/sales/transferOrder/showStockVin",
    "调拨订单保存": base_url + "/sales/transferOrder/saveTtSalesOrder",
    "提交审核": base_url + "/sales/transferOrder/submitAudit",
    "调拨订单列表查询": base_url + "/sales/transferOrder/list",
    "调拨订单新增initData": base_url + "/sales/transferOrder/initData",

    "调拨退回列表查询": base_url + "/sales/orderCancel/searchSalesReturn",

    "库存维护列表查询": base_url + "/report/vehicleStock/getVehicleStockList",
    "库存车辆查询": base_url + "/sales/salesOrder/queryVinInfo"
}

gathering_urls = {
    "收款详情": base_url + "/sales/selesSettlement/getDetail",
    "新增收款页": base_url + "/sales/selesSettlement/toCustomerGatheringPage",
    "收款保存": base_url + "/sales/selesSettlement/save",
    "结算收款列表查询": base_url + "/sales/selesSettlement/list",
}

car_inventory_urls = {
    "新增盘点单": base_url + "/sales/carInventory/addCarInventory",
    "差异情况说明-查看": base_url + "/sales/differenceInventory/toInventoryDiffExplain",
    "差异情况说明-保存": base_url + "/sales/differenceInventory/saveOrUpdateInventoryExplain",
}

wfs_urls = {
    "代办事项查询": base_url + "/dms-wfs-es/bpm/wfs/es/billHandle",
    "获取审核信息": base_url + "/dms-wfs/bpm/wfs/getBillFlow",
    "是否可终结": base_url + "/dms-wfs/bpm/wfs/bill/preEndAudit",
    "审核通过/驳回": base_url + "/dms-wfs/bpm/wfs/audit",
    "下一级审批人员列表": base_url + "/dms-wfs/bpm/wfs/bill/audit/user",
}

oa_urls = {
    "公司OA": base_url + "/dms-ad/oa/organization/range/company",

    "获取erp库存车": base_url + "/sales/vehicleStock/api/getVehicleStockListApi",
    "固定资产采购申请": base_url + "/dms-ad/fap/faps",
    "固定资产车采购申请提交审核": base_url + "/dms-ad/fap/faps/{}/send-audit",
    "固定资产采购综合查询": base_url + "/dms-ad/fap/faps",

    "车辆信息综合查询": base_url + "/dms-ad/car/car/search",
    "车辆入库附件上传": base_url + "/dms-ad/car/car_bill/file",
    "固定资产车入库": base_url + "/dms-ad/car/car_bill/{}",
    "固定资产车入库提交审核": base_url + "/dms-ad/car/car_bill/{}/submit",
    "进入入库页": base_url + "/dms-ad/car/car_bill/{}",

    "重大事项申请新增": base_url + "/dms-ad/office/importance/code",
    "加载事项类型下拉选项": base_url + "/dms-ad/office/importance/types",
    "重大事项申请保存": base_url + "/dms-ad/office/importance",
    "重大事项附件上传": base_url + "/dms-ad/mark/upload/file",
    "附件上传保存": base_url + "/dms-ad/mark/attachment/file",
    "附件列表查询": base_url + "/dms-ad/mark/attachment/file",

    "流程管理查询": base_url + "/dms-wfs/bpm/wfs/task",
    "流程管理版本": base_url + "/dms-wfs/bpm/wfs/setTaskVersion",
    "流程复制": base_url + "/dms-wfs/bpm/wfs/task/clone",
    "流程删除": base_url + "/dms-wfs/bpm/wfs/setTaskVersion",

}


if __name__ == '__main__':
    print(shipping_urls)



