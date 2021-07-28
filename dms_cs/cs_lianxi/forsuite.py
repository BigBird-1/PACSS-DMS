import os
import unittest

from HtmlTestRunner import HTMLTestRunner

from dms_cs.cs_lianxi.fortest1 import ForTest1
from dms_cs.cs_lianxi.fortest2 import ForTest2

# 创建测试套件 -- list
suite = unittest.TestSuite()
# 添加测试用例到 测试套件
# suite.addTest(ForTest1("test_1"))
# suite.addTest(ForTest1("test_2"))

case = [ForTest1("test_1"), ForTest1("test_2"), ForTest2("test_3"), ForTest2("test_4")]
suite.addTests(case)
# 通过TextTestRunner对象运行
# runner = unittest.TextTestRunner()
# runner.run(suite)

report_name = "军进林"
report_title = "林进军的测试报告"
report_path = "./report/"
report_file = report_path + 'report2.html'
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_file, 'w', encoding='utf-8') as f:
    # suite.addTests(unittest.TestLoader().loadTestsFromName(''))
    suite.addTests(case)
    runner = HTMLTestRunner(stream=f, report_name=report_name, report_title=report_title)
    runner.run(suite)
