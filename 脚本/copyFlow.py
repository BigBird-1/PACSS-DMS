import os
import requests
import time
import xlwings as xw

path = os.path.split(os.path.realpath(__file__))[0]
current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
file_path = os.path.join(path, 'flow_file')


class CopyFlow(object):

    info_dict = {
        "test_1": {"url": "https://dms.t.hxqcgf.com/apigateway", "account": ["HD340400", "AG6N", "LJ7LMXrU9lronyFk4qkGFw=="]},
        "test_2": {"url": "https://dms.hxqcgf.com/apigateway", "account": ["HD420610", "G1SB", "Dxv+ilzJncHFspBFjLvxzw=="]},
        "test_3": {"url": "https://pacss.hxqcgf.com/apigateway", "account": ["XX420001", "GPBP", "QLomgFGYMWCiBg953bt8Mw=="]}
    }

    def __init__(self):
        self.app = None
        self.wb = None
        self.sht = None

    @staticmethod
    def query(headers, task_code):
        url = "https://dms.t.hxqcgf.com/apigateway/dms-wfs/bpm/wfs/task"
        params = {
            "page": 1,
            "per_page": 15,
            "task_name": "",
            "task_code": task_code,
            # "userCodeOrigin": 88880000062054
        }
        res = requests.get(url=url, params=params, headers=headers)

        return res.json()

    def open_excel(self):
        excel_path = os.path.join(file_path, "复制审核流用.xls")
        # 连接到工作簿
        self.app = xw.App(visible=False, add_book=False)
        self.wb = self.app.books.open(excel_path)
        # 打开工作表 通过名字或者索引
        self.sht = self.wb.sheets["Sheet1"]
        # sht = self.wb.sheets[0]

    def read_code(self):
        """读取流程业务流编码和表单编码存入字典并添加到列表"""
        e_u_ps = []
        self.open_excel()
        # 获取sheet1工作表里的行数，列数
        n_rows = self.sht.used_range.last_cell.row
        n_cols = self.sht.used_range.last_cell.column
        # 获取第一行整行内容
        keys = self.sht.range('A1').expand('right').value
        # 读取业务流名称/编码/表单编码 并保存
        for i in range(2, n_rows+1):
            eup_dict = {}
            for j in range(1, n_cols+1):
                # 获取单元格数据
                c_cell = self.sht.range(i, j).value
                # 将一行数据添加到字典中
                eup_dict[keys[j-1]] = c_cell
            # 将字典添加到列表中
            e_u_ps.append(eup_dict)
        return e_u_ps, n_rows, n_cols

    def code_dict(self, task_code, task_name):
        code_list,  n_rows, n_cols = self.read_code()
        code_dict = {}
        for item in code_list:
            if item["业务流编码"] == task_code:
                code_dict = item
                break
        else:
            print("未维护流程表格，请按提示输入信息维护")
            code_1 = input("请输入测试线表单编码,TA开头的")
            code_2 = input("请输入预上线表单编码,TA开头的")
            code_3 = input("请输入正式线表单编码,TA开头的")
            code_dict = {"业务流名称": task_name, "业务流编码": task_code, "测试线": code_1, "预上线": code_2, "正式线": code_3}
            # 将数据写入excel
            self.sht.range('A{}'.format(n_rows+1)).value = [task_name, task_code, code_1, code_2, code_3]
            self.wb.save()

        return code_dict

    def login_s(self, num):
        url = self.info_dict["test_{}".format(num)]["url"] + "/auth/oauth/token"
        info = self.info_dict["test_{}".format(num)]["account"]
        headers = {
            "Authorization": "Basic c2NvOmRtcw==",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        }
        params = {
            "entitycode": "{}".format(info[0]),
            "username": "{}".format(info[1]),
            "password": "{}".format(info[2]),
            "isRemember": "true",
            "grant_type": "password"
        }
        res_dict = requests.get(url, headers=headers, params=params).json()
        try:
            token_type = res_dict["token_type"].capitalize()
            access_token = res_dict["access_token"]
            # 将token放进请求头里
            headers["Authorization"] = "{} {}".format(token_type, access_token)
        except KeyError:
            print("未获取到token -- 鉴权失败 401 ")
            return

        return headers

    @staticmethod
    def download_flow(task_code, task_version, url):

        res = requests.get(url, stream=True)
        txt_name = "{}-{}-{}.txt".format(task_code, task_version, current_time)
        txt_path = os.path.join(file_path, txt_name)

        with open(txt_path, 'wb') as f:
            # f.write(res.text)
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print("----下载流程完成----")

        return txt_path, txt_name

    @staticmethod
    def copy_flow(headers, url, form_code1, form_code2, txt_name, txt_path):

        data = {"table_mapping": '{"%s":"%s"}' % (form_code1, form_code2)}
        for k, v in data.items():
            data[k] = str(v)
        with open(txt_path, 'rb') as f:
            files = [("file", ("{}".format(txt_name), f, "text/plain"))]
            # res = http_r.run_main('post', url=url, data=data, files=files)
            res = requests.post(headers=headers, url=url, data=data, files=files)

        print(res.json())

    @staticmethod
    def delete_txt(txt_name):
        for i in os.listdir(file_path):
            if txt_name in i:
                os.remove('{}/{}'.format(file_path, i))

    def run(self):
        # 下载流程
        print("***************下载业务流程文件*****************")
        dd = None
        for i in range(100000):
            task_code = input("输入需要下载的业务流编码(TK开头)：")
            dd = self.query(self.login_s(1), task_code)
            if dd["data"]["total"] == 1 and task_code:
                break
            else:
                print("匹配出多个结果，请选择一个")
                for item in dd["data"]["data"]:
                    print(item["task_code"], item["task_name"])
                continue
        task_code = dd["data"]["data"][0]["task_code"]
        task_name = dd["data"]["data"][0]["task_name"]
        code_dict = self.code_dict(task_code, task_name)
        task_version = input("输入需要下载的版本数：")
        while True:
            down_env = input("需要下载流程的环境（1：测试线 2：预上线 3：正式线） =>")
            if down_env in ["1", "2", "3"]:
                break
        print("正在下载中......")
        url = self.info_dict["test_{}".format(down_env)]["url"] + "/dms-wfs/system/get_task_from_outurl?task_code={}&task_version={}&download=Y".format(task_code, task_version)
        txt_path, txt_name = self.download_flow(task_code, task_version, url)
        # 复制流程----------------------------------------------------------------------------------------------------
        print("****************复制业务流程*****************")
        y_t = {"1": "测试线", "2": "预上线", "3": "正式线"}
        while True:
            copy_env = input("复制流程到（1：测试线 2：预上线 3：正式线） 多环境（例：12）=>")
            if copy_env in ["1", "2", "3", "12", "13", "23", "21", "31", "32"]:
                break
        form_code = code_dict[y_t[down_env]]
        for i in copy_env:
            headers = self.login_s(i)
            url = self.info_dict["test_{}".format(i)]["url"] + "/dms-wfs/system/copy_task_from_file"
            print("正在复制到{}中……".format(y_t[i]))
            self.copy_flow(headers, url, form_code, code_dict[y_t[i]], txt_name, txt_path)
            print("----复制流程到{}完成----".format(y_t[i]))
        # 删除.txt文件
        self.delete_txt(txt_name)
        print("----删除{}成功----".format(txt_name))

        self.wb.close()
        self.app.quit()


copy_flow = CopyFlow()


if __name__ == '__main__':
    copy_flow.run()













