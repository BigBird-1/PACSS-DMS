import time
import datetime
from dateutil.relativedelta import relativedelta
from common.configHttp import http_r
from apiTest.constants import oa_urls
from common import Log, randomData

log = Log.logger
# 获取当前日期 年月日
current_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
next_year = (datetime.datetime.now()-relativedelta(years=-1)).strftime('%Y-%m-%d')


class AdministrativeAffairs(object):
    def __init__(self):
        pass

    @staticmethod
    def file_up(bill_code):
        file_path = r"C:\Users\cpr264\Desktop\阿狸.jpg"
        files = [("file", ("阿狸.jpg", open(file_path, 'rb'), "image/jpeg"))]
        data = {
            "folder": "Impor",
            "ext": "jpg, gif, png, jpeg, doc, docx, xls, xlsx, ppt, pptx, pdf, txt, zip",
            "fileSize": 31457280,
            "bill_code": bill_code
        }
        res = http_r.run_main('post', url=oa_urls["重大事项附件上传"], data=data, files=files, name="重大事项附件上传")
        file_data = res["data"]
        log.info(file_data["msg"])
        data = {
            "file": [
                {
                    "attachable_index": 0,
                    "attachment": file_data["filename"],
                    "bill_code": bill_code,
                    "creator": file_data["creator"],
                    "filename": file_data["realname"],
                    "filesize": file_data["filesize"],
                    "fileurl": file_data["fileurl"],
                    "folder": "Impor",
                    "module": "impo",
                    "remark": ""
                },
            ]

        }
        res = http_r.run_main('post', url=oa_urls["附件上传保存"], data=data, is_json=2, name="附件上传保存")
        file_s = res["data"]
        log.info("上传附件保存 {}".format(res["msg"]))
        params = {
            "module": "impo",
            "bill_code": bill_code,
            "fileds[]": int(file_s[0])
        }
        res = http_r.run_main('get', url=oa_urls["附件列表查询"], data=params, name="附件列表查询")
        print(res["data"]["data"][0])
        file_list = []
        for i in file_s:
            file_list.append(int(i))

        return file_list

    def important_matters(self):
        res = http_r.run_main('get', url=oa_urls["重大事项申请新增"], name="重大事项申请新增")
        y_t = res["data"]

        res = http_r.run_main('get', url=oa_urls["加载事项类型下拉选项"], name="加载事项类型下拉选项")
        y_g = res["data"]
        types = {}
        for item in y_g:
            types[item["label"]] = item["value"]

        data = {
            "bill_code": y_t["bill_code"],
            "company_name": y_t["company_name"],
            "icompany_id": y_t["company_id"],
            "u_name": y_t["u_name"],
            "uid": y_t["u_id"],
            "uname": y_t["u_username"],
            "d_date": current_date,
            "tel": "{}".format(randomData.random_mobile()),  # 联系方式
            "status_text": "编写中",
            "impor_type": 2,  # 事项类型*
            "attachment_ids": self.file_up(y_t["bill_code"]),  # 附件*
            "happend_time": "2022-06-20 03:00:00",  # 发生时间*

            "description": "就是 我撞了她 她要我赔",  # 事件描述*
            "supplementary_notes": "没啥好说的",  # 补充说明

            "company_drive_id": self.file_up(y_t["bill_code"]),  # 公司驾考外驾资格证*
            "economic_loss": "最少的一个亿软妹币",  # 经济损失*
            "is_insurance": 1,  # 是否有保险*
            "is_casualties": 0,  # 有无伤亡*
            "plates": randomData.random_car(),  # 车牌号

            "estimated_loss": "",
            "feedback_content": "",
            "finance_dispose_files": [],
            "finance_punish_files": [],
            "group_notes": "",
            "id": "",
            "im_id": "",
            "casualty_details": "",  # 伤亡人员及伤情
            "comp_lost": "",
            "status": 0,
            "subsidiary_files": []
        }
        res = http_r.run_main('post', url=oa_urls["重大事项申请保存"], data=data, is_json=2, name="重大事项申请保存")
        print(res)
        log.info(res["msg"])

        url_id = res["data"]["id"]


administrative_affairs = AdministrativeAffairs()


if __name__ == '__main__':
    # administrative_affairs.file_up("IMPO202206231005")
    administrative_affairs.important_matters()






