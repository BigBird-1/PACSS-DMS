import os
import time
import common.HTMLTestRunnerEN as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from BeautifulReport import BeautifulReport
# from tomorrow import threads
from common.configEmail import SendEmail
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom
from common import Log


path = getpathInfo.get_path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
fake_date = time.strftime('%Y%m%d', time.localtime(time.time()))


log = Log.logger


class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        global resultPath
        resultPath = os.path.join(report_path, 'report')  # result/report/t.html
        self.caseListFile = os.path.join(path, "caseList.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "apiTestCase")  # 真正的测试断言文件路径
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

    def set_case_suite(self):
        """
        创建测试集
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list:  # 从case_list元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
            print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite  # 返回测试集

    # @threads(5)
    def run(self):
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            print('try')
            # print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                print('if-suit')
                runner = BeautifulReport(suit)
                runner.report(filename="WeiBo报告_{}".format(fake_date), report_dir=resultPath, description='预订单')
                # with open(resultPath, 'wb') as fp:  # 打开result/report/20200618_report.html测试报告文件，如果不存在就创建
                #     # 调用HTMLTestRunner
                #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='DMS_XS')
                #     runner.run(suit)
            else:
                log.info("Have no case to test.")
        except Exception as e:
            log.info(str(e))

        finally:
            log.info(" *********TEST END*********")
        # 判断邮件发送的开关
        if on_off == 'on':
            SendEmail().fox_mail()
        else:
            log.info(" 邮件发送开关配置未开启\n\n")

# pythoncom.CoInitialize()
# 定时任务
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-6', hour=14, minute=20)
# scheduler.start()


if __name__ == '__main__':
    AllTest().run()

