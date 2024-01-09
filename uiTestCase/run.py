# -*- coding:utf-8 -*
# @FileName:   run.py
# @Author:     刘峰
# @CreateTime: 2022/7/23 9:31

"""
    执行整个项目的入口
"""
import pytest, allure, os
import threading


def run(path):
    pytest.main(['-s', path, '--alluredir', './result', '--clean-alluredir'])
    # pytest.main(['-s', '--reruns', '1', path, '--alluredir', './result', '--clean-alluredir'])
    # pytest.main(['-s', '--reruns', '1', path, '--alluredir', './result'])

    os.system("allure generate ./result -o ./report --clean")
    # os.system("allure serve ./result")


if __name__ == '__main__':
    path = './test_cases/erp售后业务系统/test_售后维修业务流程.py'
    run(path)

    # path1 = './test_cases/erp售后业务系统/test_售后维修业务流程.py'
    # path2 = './test_cases/erp售后业务系统/售后客户管理/test_车主车辆管理.py'
    # path_list = [path1, path2]
    # th = []
    # for path in path_list:
    #     th.append(threading.Thread(target=run, args=[path,]))
    # for t in th:
    #     t.start()
