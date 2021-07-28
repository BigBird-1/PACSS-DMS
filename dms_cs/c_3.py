import requests
import gevent
from multiprocessing import Process
from multiprocessing import Pool
from threading import Thread
import sys, io
from gevent import monkey
monkey.patch_all()

# 解决console显示乱码的编码问题
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def login(num):
    "获取token并加到请求头里"
    url = "http://10.0.15.130:31099/auth/oauth/token"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Authorization": "Basic c2NvOmRtcw==",
        "Host": "10.0.15.130:31099",
        "Origin": "http://10.0.15.130:31081",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        "Referer": "http://10.0.15.130:31081/",
        "Connection": "keep-alive"
    }
    params = {
        "username": "yangt",
        "password": "/3Dbu8g5+iHHnOxGvhwFrA==",
        "entitycode": "HD340400",
        "isRemember": "true",
        "grant_type": "password"
    }
    res = requests.get(url, headers=headers, params=params)
    res_dict = res.json()
    # 获取token
    token = res_dict["access_token"]
    # 将token放进请求头里
    headers["Authorization"] = "Bearer {}".format(token)
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    url = "http://10.0.15.130:31099/admin/user/info"
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        result = res.content.decode()
    else:
        result = "失败"
    print("第{}次 结果 {}".format(num, result))


if __name__ == '__main__':
    # p = Pool(10)
    # for i in range(5):
    #     p.apply_async(login, args=(i + 1, ))
    # p.close()
    # p.join()
    # -----------------------------------------------------------
    # ts = []
    # for i in range(5):
    #     t = Thread(target=login, args=(i + 1, ))
    #     t.start()
    #     ts.append(t)
    # for t in ts:
    #     t.join()
    # ----------------------------------------------------------------
    ts = []
    for i in range(100):
        t = gevent.spawn(login, i+1)
        ts.append(t)
    gevent.joinall(ts)
    print("执行结束..")

