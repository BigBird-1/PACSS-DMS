import requests
import json
from common import Log
from readConfig import read_config

log = Log.logger


class RunMain(object):

    @staticmethod
    def send_post(url, data, headers, files, name):
        res = requests.post(url=url, data=data, headers=headers, files=files)
        log.info("{} {}-响应时间:{}".format(url, name, res.elapsed.total_seconds()))
        result = res.json()
        return result

    @staticmethod
    def send_get(url, data, headers, name):
        res = requests.get(url=url, params=data, headers=headers)
        log.info("{} {}-响应时间:{}".format(url, name, res.elapsed.total_seconds()))
        result = res.json()
        return result

    @staticmethod
    def send_put(url, data, headers, name):
        res = requests.put(url=url, data=data, headers=headers)
        log.info("{} {}-响应时间:{}".format(url, name, res.elapsed.total_seconds()))
        result = res.json()
        return result

    def run_main(self, method, url=None, data=None, files=None, is_json=None, name=None, flag=None):
        """
        接口处理器
        :param method: 请求方式
        :param url: 接口地址
        :param data: 请求体/请求参数
        :param files: 上传文件
        :param is_json: 标记是否json格式
        :param name: 接口中文描述
        :param flag: 切换店铺标记
        :return: 字典格式的响应数据
        """
        result = None
        headers = self.get_token(flag)  # 带token的请求头
        # -------------------------对data数据格式进行处理---------------------------------------------------------------
        if isinstance(data, dict):
            if is_json == 2:
                data = json.dumps(data)
            elif is_json == 1:
                # data = urlencode(data).encode()
                for k, v in data.items():
                    data[k] = str(v)
                data = json.dumps(data)
            else:
                # data = urlencode(data).encode()
                for k, v in data.items():
                    data[k] = str(v)
                headers["Content-Type"] = "application/x-www-form-urlencoded"
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
            token_type = res_dict["token_type"].capitalize()
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



