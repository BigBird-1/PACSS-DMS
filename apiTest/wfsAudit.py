import time
from common.configHttp import http_r
from apiTest.initialization import initial
from apiTest.constants import wfs_urls
from common import Log


log = Log.logger
auth_dict = initial.get_audits()  # 用户的权限信息
entity_code = auth_dict["用户信息"]["id"]['entityCode']
org_code = auth_dict["用户信息"]["orgCode"]
base_user_id = auth_dict["基础用户"]['userId']
entity_short_name = auth_dict["用户信息"]['entityShortName']
user_name = auth_dict["用户信息"]['userName']
position_code = auth_dict["用户信息"]['positionCode']
group_code = auth_dict["审批权限表"]  # 审批权限
groups = auth_dict["品牌分组"]
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class ToDo(object):
    def __init__(self):
        self.bill_code = None
        self.task_code = None
        self.module_bill_code = None
        self.company_code = None
        self.module_name = None
        self.bill_type = None
        self.module_code = None
        self.tnode_code = None
        self.sys_code = None
        self.attr_ex_data = {}

    def query(self, order_no):
        payload = {"companyCode": entity_code, "companyName": entity_short_name, "depCode": org_code,
                   "groupCodeOrigin": group_code, "defDocErpCode": groups,
                   "attrExValueMin": order_no,
                   "page": 1, "pageType": 10, "perPage": 15, "userCodeOrigin": base_user_id,
                   "userNameOrigin": user_name, "posCode": position_code}
        for i in range(30):
            res = http_r.run_main('post', url=wfs_urls["代办事项查询"], data=payload, is_json=2, name="代办事项列表查询")
            log.info("代办事项查询结果: {}".format(res['data']['total']))
            if len(res['data']['data']) != 0:
                self.bill_code = res['data']['data'][0]['billCode']
                self.task_code = res['data']['data'][0]['taskCode']
                self.module_bill_code = res['data']['data'][0]['moduleBillCode']
                self.company_code = res['data']['data'][0]['companyCode']  # 哪个公司提交的
                company_name = res['data']['data'][0]['companyName']
                self.module_name = res['data']['data'][0]['moduleName']  # 模块名称
                self.bill_type = res['data']['data'][0]['billType']  # 单据类型
                log.info("billType:{} billCode:{} taskCode:{}".format(self.bill_type, self.bill_code, self.task_code))
                time.sleep(2)
                break
        else:
            log.error("代办事项里查不到数据")
            return

    def audit_node(self):
        """流程审核节点"""
        payload = {"companyCode": entity_code, "companyName": entity_short_name, "depCode": org_code,
                   "company_code": self.company_code, "defDocErpCode": groups,
                   "groupCodeOrigin": group_code, "bill_code": self.bill_code,
                   "userCodeOrigin": base_user_id, "userNameOrigin": user_name, "posCode": position_code}
        res = http_r.run_main('post', url=wfs_urls["获取审核信息"], data=payload, is_json=2, name="获取审核节点信息")
        audit_list = res['data'][0]
        audit_node = [i["audit_name"] for i in audit_list]
        log.info("---当前订单所有审核节点{}".format(audit_node[1:]))

        return audit_list

    def from_data(self):
        """审核的数据信息"""
        # ------------------主表单信息组装------------------------------------------------------------------------------
        params = {"bill_code": self.bill_code,
                  "task_code": self.task_code,
                  "module_bill_code": self.module_bill_code,
                  "company_code": self.company_code,
                  "audit": "Y",
                  "userCodeOrigin": base_user_id}
        res = http_r.run_main('get', url=wfs_urls["获取审核信息"], data=params, name="获取审核表单信息")
        self.module_code = res['data']['module_code']
        self.sys_code = res['data']['sys_code']
        self.tnode_code = res['data']['tnode_code']
        for item in res['data']['attr_ex_data']:
            self.attr_ex_data[item['attr_module_name']] = item['attr_ex_value']
        # ------------------子表单信息组装(批量审核)--------------------------------------------------------------------
        if self.module_name in ["车辆采购入库审核", "固定资产", "单车综合毛利标准审核", "特殊订单审核"]:
            table = res['data']['attr_ex_data_sub_table']
            try:
                y_t = table[0]
                value_row = eval(y_t["sub_attr_ex"][0]['attr_ex_value_row'])
            except Exception as e:
                log.warning(e)
                y_t = table[1]
                value_row = eval(y_t["sub_attr_ex"][0]['attr_ex_value_row'])
            order_info = [{} for i in range(len(value_row))]  # 子表单
            row_num = y_t['row_num']
            for i in range(row_num):
                value_row = eval(y_t["sub_attr_ex"][i]['attr_ex_value_row'])
                for j in range(len(value_row)):
                    order_info[j][y_t["sub_attr_ex"][i]['attr_module_name']] = value_row[j]
            if self.module_name in ["车辆采购入库审核", "单车综合毛利标准审核"]:
                for i in order_info:
                    i['auditStatus'] = "0"  # 全部通过
            if self.module_name == "车辆采购入库审核":
                self.attr_ex_data["orderInfo"] = order_info
            elif self.module_name in["单车综合毛利标准审核", "特殊订单审核"]:
                self.attr_ex_data["detailList"] = order_info
            elif self.module_name == "固定资产":
                self.attr_ex_data["car_infos"] = order_info

    def can_end(self):
        """是否可以终结审核"""
        payload = {"companyCode": entity_code, "companyName": entity_short_name, "depCode": org_code,
                   "defDocErpCode": groups, "groupCodeOrigin": group_code, "bill_code": self.bill_code,
                   "company_code": self.company_code, "userCodeOrigin": base_user_id, "userNameOrigin": user_name,
                   "posCode": position_code}
        res = http_r.run_main('post', url=wfs_urls["是否可终结"], data=payload, is_json=2, name="当前审核节点是否可终结")
        log.info(res)

        return res["data"]["can_end"]

    def next_auditor(self, audit_code):
        """查询下级审核人"""
        payload = {
            "attr_ex_data": self.attr_ex_data,
            "audit_company": "{}-{}".format(self.company_code, audit_code),
            "bill_code": self.bill_code,
            "companyCode": entity_code,
            "companyName": entity_short_name,
            "company_code": self.company_code,
            "defDocErpCode": groups,
            "depCode": org_code,
            "groupCodeOrigin": group_code,
            "posCode": position_code,
            "userCodeOrigin": base_user_id,
            "userNameOrigin": user_name
        }
        res = http_r.run_main('post', url=wfs_urls["下一级审批人员列表"], data=payload, is_json=2, name="下一级审批人员列表查询")
        next_info = None
        if res["message"] == "下级审核：总部审核":
            y_t = res["data"]
            for item in y_t[::-1]:
                if item["end_audit_name"] == "可终结":
                    next_info = item
                    break

        return next_info

    def audit(self, audit_result, audit_content, next_audit_code, next_code="", next_user="", end=None):
        payload = {
            "appoint_audit_code": next_code,
            "appoint_audit_userid": next_user,
            "task_code": self.task_code,
            "tnode_code": self.tnode_code,
            "sys_code": self.sys_code,
            "module_code": self.module_code,
            "bill_code": self.bill_code,
            "module_bill_code": self.module_bill_code,
            "company_code": self.company_code,
            "audit_result": audit_result,
            "audit_content": audit_content,
            "next_audit_code": next_audit_code,
            "attr_ex_data": self.attr_ex_data,
            "groupCodeOrigin": group_code,
            "userCodeOrigin": base_user_id,
            "userNameOrigin": user_name,
            "depCode": org_code,
            "defDocErpCode": groups,
            "posCode": position_code,
            "companyCode": entity_code,
            "companyName": entity_short_name
        }
        if end:
            payload["end_audit"] = end
            payload["audit_content"] = "终结"
            del payload["appoint_audit_code"]
            del payload["appoint_audit_userid"]
        res = http_r.run_main('post', url=wfs_urls["审核通过/驳回"], data=payload, is_json=2, name="审核结果-通过/驳回")

        return res

    def audit_flow(self, order_no):
        """
        :param order_no: 订单单号
        :return:
        """
        self.query(order_no)
        self.from_data()
        node_list = self.audit_node()
        for i in range(1, len(node_list)):
            now_audit_code = node_list[i]["now_audit_code"]
            audit_result = "Y"
            audit_content = "同意"
            # ------------------------------------------------------------------------------------------------------------
            if self.bill_type == "综合毛利审核":
                if node_list[i]["audit_name"] == "子公司总经理":
                    next_info = self.next_auditor(now_audit_code)
                    if next_info:
                        next_code = next_info["audit_code"]
                        next_user = next_info["userId"]
                        self.audit(audit_result, audit_content, now_audit_code,
                                   next_code=next_code, next_user=next_user)
                        now_audit_code = next_code  # 指定的下级审核节点
                        self.audit(audit_result, audit_content, now_audit_code, end="Y")
                        log.info("{}-{}: {} 终结审核".format(next_info["group_name"], next_info["positionName"],
                                                         next_info["userName"]))
                        break
            # ------------------------------------------------------------------------------------------------------------
            is_end = self.can_end()
            if is_end == "Y":
                res = self.audit(audit_result, audit_content, now_audit_code, end="Y")
                log.info("{}---可终结审核: {}, 审核已终结".format(res, node_list[i]["audit_name"]))
                break
            res = self.audit(audit_result, audit_content, now_audit_code)
            log.info("{}---{}审核通过".format(res, node_list[i]["audit_name"]))


to_do = ToDo()


if __name__ == '__main__':
    to_do.audit_flow("GDZC202304111001")
    # to_do.query("")





