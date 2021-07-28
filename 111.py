# import unittest
# from common.HTMLTestRunnerEN import HTMLTestRunner
#
#
# class NewBrand(unittest.TestCase):
#
#     def test_01(self):
#         print(111)
#
#
# suite = unittest.TestSuite()
# # loader = unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(NewBrand))
# suite.addTest(NewBrand('test_01'))
# # runner = unittest.TextTestRunner()
# filename = r'F:\DMS_2020\aaa.html'
# with open(filename, 'wb') as f:
#     runner = HTMLTestRunner(stream=f)
#     runner.run(suite)
# from testCase.test01case import NewBrand
#
# suite = unittest.TestSuite()
# # loader = unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(NewBrand))
# suite.addTest(NewBrand('test_case'))
# # runner = unittest.TextTestRunner()
# with open('./ce1.html', 'wb') as f:
#     runner = HTMLTestRunner(stream=f)
#     runner.run(suite)
# a = "case/test01"
# case_name = a.split("/")[-1]
# print(case_name)
# print(type(case_name))


def func(fn):
    def wrapper(*args, **kwargs):
        print(1111)
        return fn(*args, **kwargs)
    return wrapper


@func  # test = func(test)
def test(num):
    print(num)


def log_with_param(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)


# test_with_param(3)
# import os
# import getpathInfo
#
#
# path = getpathInfo.get_path()
# report_path = os.path.join(path, 'result/report')
#
# print(os.path.abspath(report_path))
# import time
# import requests
# from tomorrow import threads
#
# urls = [
#     'http://www.baidu.com',
#     'http://www.163.com',
#     'http://www.bilibili.com',
#     'http://www.jd.com',
#     'http://www.12306.com',
#     'http://www.sohu.com',
#     'http://www.taobao.com'
# ]
#
#
# @threads(10)
# def download(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
#     }
#     return requests.get(url, headers=headers)
#
#
# if __name__ == "__main__":
#     import time
#
#     start = time.time()
#     responses = [download(url) for url in urls]
#     html = [response.text for response in responses]
#     end = time.time()
#     print("Time: %f seconds" % (end - start))
# import unittest
# from nose_parameterized import parameterized
#
# c = [[11,22,33], [22,34,44]]
#
# class Dd(unittest.TestCase):
#
#     @parameterized.expand(c)
#     def test_1(self, a, b, c):
#         print(c)
#         if a == 11:
#             self.assertEqual(b, 22)
#         if a == 22:
#             self.assertEqual(c, 55)
#
# if __name__ == '__main__':
#     unittest.main()
# import random
# import string
#
#
# vin = ''.join(random.sample(string.ascii_uppercase + string.digits, 17))
#
#
# print(vin)


# name = "321"
# print(name[::-1])

# d1 = {"aa": 1, "bb": ""}
#
# d2 = {"cc": d1["aa"], "dd": d1["bb"] if d1["bb"] is not "" else "33"}
#
# print(d2)
# dict = {"aa": "null"}

"""销售订单新增初始化/apigateway/sales/salesOrder/initData
梯度加压，每10秒增加100个线程，运行100秒增加到1000个线程后维持1000个线程继续运行100s"""
import datetime
import requests
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from common.configHttp import RunMain
from statistics import mean


headers = RunMain().get_token()
url = "https://dms.t.hxqcgf.com/apigateway/sales/salesOrder/initData"


def func():
    res = requests.get(headers=headers, url=url)
    t1 = res.elapsed.total_seconds()
    # print(t1)
    return t1

    # if res.status_code == 200:
    #     print(".")
    # else:
    #     print("F")


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=200)
    t_list = []
    first = datetime.datetime.now()
    for i in range(1000):
        t_list.append(pool.apply_async(func))
        # pool.apply_async(func)   # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("Sub-process(es) done.")
    end = datetime.datetime.now()
    t = (end - first).seconds
    list1 = [x.get() for x in t_list]  # 取出所有子进程的返回值
    n = len(list1)
    l = mean(list1)
    c = n*l/t
    print(n, l, t, c)
    # pool = ThreadPoolExecutor(max_workers=100)
    # for i in range(100):
    #     pass











