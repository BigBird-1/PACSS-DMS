import os
import pytest
import getpathInfo
import readConfig
import time
from shutil import copyfile


path = getpathInfo.get_path()
report_path = os.path.join(path, 'result')
case_path = os.path.join(path, 'testCase')  # 固定
on_off = readConfig.ReadConfig().get_email('on_off')
fake_date = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))


class AllTest(object):
    def __init__(self):  # 初始化一些参数和数据
        self.json_path = os.path.join(report_path, 'json_report')  # result/json_report/
        self.html_path = os.path.join(report_path, 'report-allure_{}'.format(fake_date))
        self.caseListFile = os.path.join(path, "caseList.txt")  # 配置执行哪些测试文件的配置文件路径
        # self.ev_path = os.path.join(self.html_path, 'environment.properties')
        self.case_list = []

    def set_case_list(self):
        """
        读取caseList.txt文件中的用例名称，并添加到case_list元素组
        """
        with open(self.caseListFile) as fb:
            for value in fb.readlines():
                data = str(value)
                if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                    self.case_list.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n

    # def run(self):
    #     self.set_case_list()
    #     for case_model in self.case_list:  # 从case_list元素组中循环取出case
    #         print(case_model + '.py')  # 打印出取出来的名称
    #         case = os.path.join(case_path, '{}.py'.format(case_model))
    #         os.system("pytest -s {} --alluredir={}".format(case, self.json_path))
    #
    #     os.system('allure generate {} -o {}'.format(self.json_path, self.html_path))
    #     for i in os.listdir(self.json_path):
    #         if 'json' in i:
    #             os.remove('{}/{}'.format(self.json_path, i))


    def run(self):
        self.set_case_list()
        for case_model in self.case_list:  # 从case_list元素组中循环取出case
            print(case_model + '.py')  # 打印出取出来的名称
            case = os.path.join(case_path, '{}.py'.format(case_model))

            pytest.main(['-s', '--alluredir=allure-results', '{}'.format(case)])

            os.system("pytest -s {} --alluredir={}".format(case, self.json_path))
            # pytest.main(['-s', '--alluredir', 'allure-results', '{}'.format(case), '--clean-allure'])

        os.system('allure generate {} -o {}'.format(self.json_path, self.html_path))
        for i in os.listdir(self.json_path):
            if 'json' in i:
                os.remove('{}/{}'.format(self.json_path, i))



if __name__ == '__main__':
    AllTest().run()
    # pytest.main(['-s', '--alluredir', 'allure-results', '{}'.format(case_path)])





