import time
from apiTest.orderManagement.depositOrder import deposit_order
from apiTest.stockManagement.shippingCar import shipping_car
from apiTest.stockManagement.vehiclesStockEntry import stock_entry
from apiTest.orderManagement.salesOrder import sales_order
from apiTest.derivativesBusiness.decorationOrder import decoration_order
from apiTest.orderManagement.salesReturn import sales_return
from apiTest.orderManagement.transferOrder import transfer_order
from apiTest.orderManagement.deliveryCar import delivery_car
from apiTest.stockManagement.vehicleGrossStandard import gross_standard
from apiTest.stockManagement.vehicleOutStock import out_stock
from apiTest.wfsAudit import to_do
from apiTest.salesSettlement.advancePayment import advance_payment
from apiTest.salesSettlement.settlementGathering import settlement_gathering
from apiTest.initialization import initial
from apiTest.constants import is_deputy_delivery
from apiTest.fixedAssets.purchasingApplication import fixed_assets
from common import Log
import readConfig
from common.configEmail import SendEmail


log = Log.logger
sales_params = initial.basic_params()


class RunFlow(object):
    def __init__(self):
        pass

    @staticmethod
    def into_stock(in_type, vin, se_no="", flag=None):
        """车辆入库:采购入库,调拨入库,销售退回入库,调拨退回入库"""
        vin_1 = vin[:17]
        y_t = stock_entry.query(vin=vin_1, se_no=se_no, flag=flag)
        if not y_t:
            return
        se_no = y_t["入库单号"]
        stock_entry.check_car(se_no, vin, flag=flag)
        stock_entry.submit_audit(se_no, vin, flag=flag)
        time.sleep(5)
        y_t = stock_entry.query(vin=vin_1, se_no=se_no, flag=flag)
        if not y_t:
            return
        vehicle_info = y_t["车辆信息"]
        # -----------------------------------提交审核后-----------------------------------------------------------------
        if vehicle_info["auditStatus"] == "审核中":
            to_do.audit_flow(se_no)
            time.sleep(5)
            y_t = stock_entry.query(vin=vin_1, se_no=se_no, flag=flag)  # 审核后再查一次
            if not y_t:
                return
            vehicle_info = y_t["车辆信息"]
            if vehicle_info["auditStatus"] == "审核中":
                log.info("入库审核通过后状态未改变,ERP还是审核中: {}".format(se_no))
                return
            elif vehicle_info["auditStatus"] == "审核驳回":
                log.info("审核驳回")
                return
        elif vehicle_info["auditStatus"] == "审核驳回":
            log.info("入库审核提交后自动驳回: {}".format(vin))
        # ---------------------------------入库审核通过后---------------------------------------------------------------
        if in_type == "调拨入库":
            stock_entry.rebate_confirm(se_no, flag=flag)
            stock_entry.in_store(se_no, vin, flag=flag)
        elif sales_params["车辆入库审核通过自动入库"] == "12781002" and in_type != "调拨入库":
            stock_entry.in_store(se_no, vin, flag=flag)
        log.info("车辆已入库:{} -----(入库完成)-----".format(vin))

    @staticmethod
    def leave_stock(out_type, vin, flag=None):
        """车辆出库: 采购退回出库, 销售出库, 调拨出库, 调拨退回出库"""
        sd_no = out_stock.create_order(out_type, vin, flag=flag)
        if out_type in ["采购退回出库", "调拨退回出库"]:
            out_stock.submit_audit(vin, sd_no, out_type, flag=flag)
            time.sleep(5)
            vehicle_info = out_stock.query_order(vin=vin, flag=flag)
            # -------------------------提交审核后-----------------------------------------------------------------------
            if vehicle_info["auditStatusName"] == "审核中":
                to_do.audit_flow(vin)
                vehicle_info = out_stock.query_order(vin=vin, flag=flag)  # 审核完再查一次
                time.sleep(5)
                if vehicle_info["auditStatusName"] == "审核中":
                    log.info("出库审核通过后状态未改变,ERP还是审核中: {}".format(vin))
                    return
                elif vehicle_info["auditStatusName"] == "审核驳回":
                    log.info("审核驳回")
                    return
            elif vehicle_info["auditStatusName"] == "审核驳回":
                log.info("审核驳回")
                return
            # --------------------------出库审核通过后------------------------------------------------------------------
            if sales_params["整车{}审核通过自动出库".format(out_type)] == "12781002":
                out_stock.out_store(sd_no, flag=flag)
            else:
                log.info("整车{}审核通过自动出库 : {} -----(出库完成)-----".format(out_type, vin))
        elif out_type in ["销售出库", "调拨出库"]:
            out_stock.out_store(sd_no, flag=flag)

    @staticmethod
    def gross_flow(vin_str):
        """
        单车综合毛利标准设置
        :param vin_str: 字符串 “HGYGTFRFREDR4ER5T”
        :return:
        """
        vin_list = gross_standard.save(vin_str)
        audit_no = gross_standard.submit_audit(vin_list)
        to_do.audit_flow(audit_no)

    def shipping_flow(self, vin=None):
        """整车采购入库流程"""
        vin_list = shipping_car.new_save(vin)
        vin_s = ','.join(vin_list)
        if sales_params["计算单车资金成本"] == "12781001" and is_deputy_delivery == 12781002:
            shipping_car.capital_cost(vin_s)
        se_no = shipping_car.to_store(vin_s)
        self.into_stock("厂家采购入库", vin_s, se_no=se_no)

        return vin_list

    @staticmethod
    def deposit_flow(code_desc, phone=""):
        """
        购车建议书流程
        :param code_desc: 证件类型: 其他 机构代码 护照 军官证 居名身份证
        :param phone: 手机号
        :return:
        """
        order_no, mobile = deposit_order.new_save(code_desc, phone)
        deposit_order.submit_audit(order_no)
        time.sleep(10)
        order_info = deposit_order.query(order_no)
        # --------------------提交审核后--------------------------------------------------------------------------------
        if order_info["soStatusDesc"] == "审核中":
            to_do.audit_flow(order_no)
            time.sleep(5)
            order_info = deposit_order.query(order_no)  # 审核后再次查询
            if order_info["soStatusDesc"] == "审核中":
                log.info("购车建议书审核通过后状态未改变,ERP还是审核中: {}".format(order_no))
                return
            elif order_info["soStatusDesc"] == "审核驳回":
                log.info("审核驳回")
                return
        elif order_info["soStatusDesc"] == "审核驳回":
            log.info("{}单据被自动驳回".format(order_no))
            return
        # -------------------订单审核通过后-----------------------------------------------------------------------------
        advance_payment.gathering(order_no)

        return order_no, mobile

    @staticmethod
    def deposit_return_flow(order_no):
        """
        购车建议书退回流程
        :param order_no: 购车建议书单号
        :return:
        """
        return_no = deposit_order.order_return(order_no)
        order_info = deposit_order.query(return_no)
        if order_info["soStatusDesc"] == "未提交":
            deposit_order.submit_return_audit(return_no)
            time.sleep(3)
            order_info = deposit_order.query(return_no)
            if order_info["soStatusDesc"] == "审核中":
                to_do.audit_flow(return_no)
                time.sleep(3)
                order_info = deposit_order.query(return_no)
                if order_info["soStatusDesc"] == "审核中":
                    return
                elif order_info["soStatusDesc"] == "审核驳回":
                    return
            elif order_info["soStatusDesc"] == "审核驳回":
                log.info("{}单据被自动驳回".format(return_no))
                return
            advance_payment.gathering(return_no)
        elif order_info["soStatusDesc"] == "审核中":
            log.info("已存在的退回单在审核中: {}".format(return_no))
            return
        elif order_info["soStatusDesc"] == "退款中":
            advance_payment.gathering(return_no)

        return return_no

    @staticmethod
    def sales_flow(vin, phone="", customer_type=""):
        """销售订单出库流程"""
        is_dispatched_audit = sales_order.is_dispatch_audit(vin)
        so_no, customer_type = sales_order.new_save(vin, phone, customer_type)
        # decoration_order.new_save(so_no=so_no)
        sales_order.submit_audit(so_no)
        time.sleep(10)
        order_info = sales_order.order_query(so_no)
        if order_info["soStatus"] == "未提交":
            sales_order.submit_audit(so_no)
            time.sleep(10)
        order_info = sales_order.order_query(so_no)
        # -----------------------提交审核之后---------------------------------------------------------------------------
        if order_info["soStatus"] == "审核中":
            to_do.audit_flow(so_no)
            time.sleep(5)
            order_info = sales_order.order_query(so_no)
            if order_info["soStatus"] == "审核中":
                log.info("销售订单审核通过后状态未改变,ERP还是审核中: {}".format(so_no))
                return
            elif order_info["soStatus"] == "审核驳回":
                return
        elif order_info["soStatus"] == "审核驳回":
            log.info("提交后 自动驳回")
            return
        # ---------------------销售订单审核通过后-----------------------------------------------------------------------
        res = delivery_car.dispatched_confirm(so_no)
        if not res:
            return
        elif isinstance(res, dict) and res["code"] == 400:
            log.info(res["message"])
            return
        if is_dispatched_audit == 12781001 and customer_type != 10181003 and res != "已配车确认":
            to_do.audit_flow(so_no)
            time.sleep(5)
            order_info = sales_order.order_query(so_no)
            if order_info["soStatus"] == "审核中":
                log.info("销售订单配车审核通过后状态未改变,ERP还是审核中: {}".format(so_no))
                return
        log.info("已配车确认 : {}".format(vin))
        settlement_gathering.gathering(so_no)
        y_t = delivery_car.delivery(so_no, vin)
        if y_t == -1:
            log.error("交车确认失败")
            return
        if sales_params["自动出库"] == "12781002":  # 基础参数未勾需要手动出库
            sd_no = out_stock.create_order("销售出库", vin)
            out_stock.out_store(sd_no)
        log.info("车辆已出库:{} -----(销售订单已关单:{})-----".format(vin, so_no))

        return so_no

    def sales_return_flow(self, key_word=""):
        """销售订单退回流程"""
        return_no, vin = sales_return.new_save(key_word)
        sales_return.submit_audit(return_no)
        time.sleep(5)
        y_t = sales_return.query(return_no)
        # ---------------------提交审核后-------------------------------------------------------------------------------
        if y_t["soStatus"] == "审核中":
            to_do.audit_flow(return_no)
            time.sleep(5)
            y_t = sales_return.query(return_no)
            if y_t["soStatus"] == "审核中":
                log.info("销售退回订单审核通过后状态未改变,ERP还是审核中: {}".format(return_no))
                return
            elif y_t["soStatus"] == "审核驳回":
                log.info("审核驳回")
                return
        elif y_t["soStatus"] == "审核驳回":
            log.info("提交后立即审核驳回")
            return
        # -----------------退回订单审核通过后---------------------------------------------------------------------------
        if sales_params["销售退回订单审核通过自动入库"] == "12781002":
            self.into_stock("销售退回入库", vin)
        log.info("车辆已入库:{},-----(销售退回订单已完成:{})-----".format(vin, return_no))

    def transfer_flow(self, vin):
        """调拨订单出库流程"""
        so_no = transfer_order.new_save(vin)
        transfer_order.submit_audit(so_no)
        time.sleep(6)
        order_info = transfer_order.order_query(so_no)
        # --------------------提交审核后--------------------------------------------------------------------------------
        if order_info["soStatus"] == "审核中":
            to_do.audit_flow(so_no)
            time.sleep(6)
            order_info = transfer_order.order_query(so_no)
            if order_info["soStatus"] == "审核驳回":
                log.info("审核驳回,可以再次提交审核")
                return
            elif order_info["soStatus"] == "审核中":
                log.info("调拨订单审核通过后状态未改变,ERP还是审核中: {}".format(so_no))
                return
        elif order_info["soStatus"] == "审核驳回":
            log.info("单据提交并立即被驳回了")
            return
        # ----------------订单审核通过后--------------------------------------------------------------------------------
        settlement_gathering.gathering(so_no)
        delivery_car.delivery(so_no, vin)
        if sales_params["自动出库"] == "12781002":  # 基础参数未勾需要手动出库
            self.leave_stock("调拨出库", vin)
        log.info("车辆已出库:{} -----(调拨订单已关单:{})-----".format(vin, so_no))

    def transfer_return_flow(self, vin):
        """调拨入库退回流程:1.调拨车辆入库(B店) 2.调拨车辆退回出库(B店) 3.调拨退回单审核(A店) 4.调拨退回车辆入库(A店)"""
        self.into_stock("调拨入库", vin, flag=1)
        log.info("-----(B店调拨车辆入库完成)-----")
        self.leave_stock("调拨退回出库", vin, flag=1)
        log.info("-----(B店调拨车辆退回出库完成)-----")
        time.sleep(5)
        order_info = transfer_order.order_cancel(vin)  # 调拨退回单查询
        so_no = order_info["soNo"]
        # -------------调拨退回单自动提交审核---------------------------------------------------------------------------
        if order_info["soStatus"] == "审核中":
            to_do.audit_flow(so_no)
            time.sleep(10)
            order_info = transfer_order.order_cancel(vin)
            if order_info["soStatus"] == "审核中":
                log.info("调拨退回订单审核通过后状态未改变,ERP还是审核中: {}".format(so_no))
                return
            elif order_info["soStatus"] == "审核驳回":
                return
        elif order_info["soStatus"] == "审核驳回":
            return
        elif order_info["soStatus"] == "等待退回入库":
            self.into_stock("调拨退回入库", vin)
        # --------------审核通过后--------------------------------------------------------------------------------------
        # if sales_params["调拨退回订单审核通过自动入库"] == "12781002":
        #     self.into_stock("调拨退回入库", vin)
        log.info("车辆已入库:{},-----(调拨退回订单已完成:{})-----".format(vin, so_no))

    @staticmethod
    def fixed_assets_flow(apply_type, buy_trench, vin=""):
        """
        固定资产车采购申请
        :return: 申请的车架号
        """
        order_no, url_id, vin_1 = fixed_assets.save(apply_type, buy_trench, vin)
        fixed_assets.submit_audit(url_id, "固定资产车采购申请提交审核")
        to_do.audit_flow(order_no)
        y_t = fixed_assets.query(order_no)
        if y_t["status_text"] == "已批准":
            log.info("固定资产车采购申请已完成 单据编号{}".format(order_no))
        else:
            log.error("审核通过 状态不一致，当前状态：{}".format(y_t["status_text"]))
            return

        return vin_1

    @staticmethod
    def assets_store(vin):
        """固定资产车入库"""
        y_t = fixed_assets.query1(vin)
        url_id = y_t["id"]
        order_no = fixed_assets.to_store(url_id)
        fixed_assets.submit_audit(url_id, "固定资产车入库提交审核")
        to_do.audit_flow(order_no)
        time.sleep(2)
        y_t = fixed_assets.query1(vin)
        log.info("车架号：{}，库存状态：{}，使用状态：{}".format(vin, y_t["inventory_status_name"], y_t["car_state_name"]))

    def oa_assets_store(self, apply_type, buy_trench, vin=""):
        """固定资产车采购申请-ERP销售出库-入库"""
        vin_1 = self.fixed_assets_flow(apply_type, buy_trench, vin)
        time.sleep(2)
        if apply_type in ["试乘试驾车", "服务替换车"] and buy_trench == "自店采购":
            self.sales_flow(vin_1, customer_type="本经销商")
            time.sleep(2)
        self.assets_store(vin_1)

    def erp_sales_flow(self, phone=""):
        """
        销售主体流程接口自动化: 车辆采购入库->单车综合毛利标准设置->购车建议书->购车建议书退回->购车建议书转销售订单
                                ->销售订单出库->销售订单退回->调拨订单出库->调拨退回入库->车辆采购退回出库
        :param phone: 明确客户保证购车建议书转销售订单
        :return:
        """
        vin_l = self.shipping_flow()
        vin_s = vin_l[0]
        self.gross_flow(vin_s)
        deposit_no, y_t = self.deposit_flow("居民身份证")
        self.deposit_return_flow(deposit_no)
        y_t, mobile = self.deposit_flow("居民身份证", phone=phone)
        sales_no = self.sales_flow(vin_s, phone=mobile)
        self.sales_return_flow(sales_no)
        self.transfer_flow(vin_s)
        self.transfer_return_flow(vin_s)
        self.leave_stock("采购退回出库", vin_s)

        on_off = readConfig.ReadConfig().get_email('on_off')
        if on_off == 'on':
            SendEmail().fox_mail()
        else:
            log.info(" 邮件发送开关配置未开启\n\n")


flow = RunFlow()

if __name__ == '__main__':
    # flow.erp_sales_flow(phone="")
    vin_l1 = flow.shipping_flow()
    vin1 = vin_l1[0]
    ss = ','.join(vin_l1)
    flow.gross_flow(ss)
    # flow.sales_flow(vin1, phone="13632708205", customer_type="")
    # flow.sales_return_flow("1BLDC8A609KGZ0UFS")
    # flow.oa_assets_store("试乘试驾车", "自店采购", vin="LEFCJCDC79HP30D0D")
    # flow.fixed_assets_flow("工作车", "")























