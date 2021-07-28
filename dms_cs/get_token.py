from urllib.parse import urlencode

import requests


def get_token():
    """获取token并加到请求头里"""
    url = "http://10.0.15.130:31099/auth/oauth/token"
    headers = {
        # "Accept": "application/json, text/plain, */*",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Authorization": "Basic c2NvOmRtcw==",
        # "Host": "10.0.15.130:31099",
        # "Origin": "http://10.0.15.130:31081",
        # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        # "Referer": "http://10.0.15.130:31081/",
        # "Connection": "keep-alive"
    }
    params = {
        "username": "9047",
        "password": "SFSGZ6DoiQ5HcN0uXJBU1g==",
        "entitycode": "HD340400",
        "isRemember": "true",
        "grant_type": "password"
    }
    res = requests.get(url, headers=headers, params=params)
    res_dict = res.json()
    # print(res_dict)
    # 获取token
    try:
        token = res_dict["access_token"]
        # print("access_token：{}".format(token))
        # 将token放进请求头里
        headers["Authorization"] = "Bearer {}".format(token)
    except KeyError:
        print("账号或密码错误 未拿到token")
        return
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    return headers


heraders = get_token()
print(heraders)
# url = "http://10.0.15.134:9999/sales/salesDepositOrder/goEditPage"
# params = {
#     "orderNo": "DO2006050001"
# }
#
# res = requests.get(url, headers=heraders, params=params)
# print(res.json())




