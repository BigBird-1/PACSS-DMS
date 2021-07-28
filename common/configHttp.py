from urllib.parse import urlencode
import requests
import json
# import geturlParams
from common import Log
from readConfig import read_config

log = Log.logger


class RunMain(object):

    @staticmethod
    def send_post(url, data, headers, files, name):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入、headers已鉴权
        res = requests.post(url=url, data=data, headers=headers, files=files)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        log.info("{} {}-响应时间:{}".format(url, name, res.elapsed.total_seconds()))
        result = res.json()
        return result

    @staticmethod
    def send_get(url, data, headers, name):
        res = requests.get(url=url, params=data, headers=headers)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        log.info("{} {}-响应时间:{}".format(url, name, res.elapsed.total_seconds()))
        result = res.json()
        return result

    @staticmethod
    def send_put(url, data, headers, name):
        res = requests.put(url=url, params=data, headers=headers)
        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        log.info("{} {}-响应时间:{}".format(url, name, res.elapsed.total_seconds()))
        result = res.json()
        return result

    def run_main(self, method, url=None, data=None, files=None, is_json=None, name=None, flag=None):
        result = None
        # 带token的headers
        headers = self.get_token(flag)
        if isinstance(data, dict):
            # data = urlencode(data).encode()
            for k, v in data.items():
                data[k] = str(v)
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            if is_json == 1:
                data = json.dumps(data)
                headers["Content-Type"] = "application/json;charset=UTF-8"
        if files:
            del headers["Content-Type"]
        if method == 'post':
            result = self.send_post(url, data, headers, files, name)
        elif method == 'get':
            result = self.send_get(url, data, headers, name)
        elif method == 'put':
            result = self.send_put(url, data, headers, name)
        else:
            log.info("method值错误！！！")
            return
        return result

    @staticmethod
    def get_token(flag=None):
        """获取token并加到请求头里"""
        url = read_config.get_http('base_url') + "/auth/oauth/token"
        headers = {
            "Authorization": "Basic c2NvOmRtcw==",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        }
        params = {
            "username": "{}".format(read_config.get_http('username')),
            "password": "{}".format(read_config.get_http('password')),
            "entitycode": "{}".format(read_config.get_http('entity_code')),
            "isRemember": "true",
            "grant_type": "password"
        }
        if flag:
            params["entitycode"] = "{}".format(read_config.get_http('entity_code1'))
        res_dict = requests.get(url, headers=headers, params=params).json()
        try:
            token_type = res_dict["token_type"]
            access_token = res_dict["access_token"]
            # 将token放进请求头里
            headers["Authorization"] = "{} {}".format(token_type, access_token)
        except KeyError:
            log.error("未获取到token -- 鉴权失败 401 ")
            return
        headers["Content-Type"] = "application/json;charset=UTF-8"
        return headers


http_r = RunMain()


if __name__ == '__main__':
    http_r.run_main('get')



