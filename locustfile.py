import requests
from locust import TaskSet, task, HttpUser


# HttpLocust 这个类的作用是用来发送http请求的
# TaskSet   这个类是定义用户行为的，相当于loadrunnerhttp协议的脚本，jmeter里面的http请求一样，要去干嘛的
# task   这个task是一个装饰器，它用来把一个函数，装饰成一个任务，也可以指定他们的先后执行顺序


def login():
    headers = {
        "Authorization": "Basic c2NvOmRtcw==",
        # "Authorization": "Bearer f47351dc-7804-4511-91d9-18e675be47ac",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    }
    params = {
        "username": "A08D",
        "password": "QLomgFGYMWCiBg953bt8Mw==",
        "entitycode": "HD340400",
        "isRemember": "true",
        "grant_type": "password"
    }
    url = "https://dms.t.hxqcgf.com/apigateway/auth/oauth/token"
    res = requests.get(url, headers=headers, params=params).json()
    global access_token
    access_token = res["access_token"]


def query():
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    }


class BestTestIndexUser(HttpUser):
    @task
    def login(self):
        headers = {
            "Authorization": "Basic c2NvOmRtcw==",
            # "Authorization": "Bearer f47351dc-7804-4511-91d9-18e675be47ac",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        }
        params = {
            "username": "A0KP",
            "password": "MU+nhnWyl54m0ETceVmVCw==",
            "entitycode": "HD420610",
            "isRemember": "true",
            "grant_type": "password"
        }
        url = "https://dms.hxqcgf.com/apigateway/auth/oauth/token"
        res = self.client.get(url, headers=headers, params=params)
        # print(res_dict, sep="\n")

    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import os
    # os.system("locust -f locustfile.py --host=https://dms.hxqcgf.com")






