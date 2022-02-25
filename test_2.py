# coding=utf-8
# import smtplib
# from email.mime.text import MIMEText
#
# msg_from = '1655719335@qq.com'  # 发送方邮箱
# passwd = 'qhhdbhlqjiushjhg'  # 填入发送方邮箱的授权码
# msg_to = '1481179185@qq.com'  # 收件人邮箱
#
# subject = "python邮件测试"  # 主题
# content = "这是我使用python smtplib及email模块发送的邮件"     # 正文
# msg = MIMEText(content)
# msg['Subject'] = subject
# msg['From'] = msg_from
# msg['To'] = msg_to
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465) # 邮件服务器及端口号
#     s.login(msg_from, passwd)
#     s.sendmail(msg_from, msg_to, msg.as_string())
#     print("发送成功")
# except Exception as e:
#     print(e)
#     print("发送失败")
# finally:
#     s.quit()
# import os
# import getpathInfo
# caseList = []
# path = getpathInfo.get_path()
# caseListFile = os.path.join(path, "caseList.txt")
# with open(caseListFile) as fb:
#     for value in fb.readlines():
#         data = str(value)
#         caseList.append(data)
#         if data != '' and not data.startswith("#"):
#             caseList.append(data.replace("\n", ""))
#
# print(caseList)
# BlockingScheduler定时任务
from urllib.parse import urlencode

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time


# 输出时间
# def job():
#     print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     # print(datetime.now().strtime("%Y-%m-%d %H:%M:%S"))
#
#
# # BlockingScheduler
# scheduler = BlockingScheduler()
# # scheduler.add_job(job, "cron", day_of_week = "1-5", hour = 6, minute = 30)
# scheduler.add_job(job, 'interval', seconds=60)
# scheduler.start()

# scheduler.add_job(job, 'cron', hour=1, minute=5)
# hour = 19, minute = 23
# 这里表示每天的19：23
# 分执行任务
# hour = '19', minute = '23'
# 这里可以填写数字，也可以填写字符串
# hour = '19-21', minute = '23'
# 表示
# 19: 23、 20: 23、 21: 23
# 各执行一次任务

# 每300秒执行一次
# scheduler.add_job(job, 'interval', seconds=300)

# 在1月,3月,5月,7-9月，每天的下午2点，每一分钟执行一次任务
# scheduler.add_job(func=job, trigger='cron', month='1,3,5,7-9', day='*', hour='14', minute='*')

# 当前任务会在 6、7、8、11、12 月的第三个周五的 0、1、2、3 点执行
# scheduler.add_job(job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

# 从开始时间到结束时间，每隔俩小时运行一次
# scheduler.add_job(job, 'interval', hours=2, start_date='2018-01-10 09:30:00', end_date='2018-06-15 11:00:00')

# 自制定时器
# from datetime import datetime
# import time
#
#
# # 每n秒执行一次
# def timer(n):
#     while True:
#         print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         time.sleep(n)
#
#
# timer(5)

# fake_date = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
# print(fake_date)
# print(type(fake_date))
# -------------------------------------------------------------------------------------------------------
# "新车销售价 - 采购价 + 预估佣金 + 大客户佣金 + 二手车佣金+预估保险毛利+金融返利+装潢销售金额 - 精品成本 - 精品减免金额+咨询服务费+劳务服务费+全损换新毛利—后期折让或退款金额金额"
#
#
# a = float(input("实际销售价"))-float(input("采购价"))+float(input("预估佣金"))+float(input("大客户佣金"))+float(input("二手车佣金"))+float(input("预估保险返利"))+float(input("金融返利"))+float(input("装潢销售金额"))-float(input("精品成本"))-float(input("精品减免金额"))+float(input("咨询服务费"))+float(input("劳务服务费"))+float(input("全损换新毛利"))-float(input("后期折让或退款金额金额"))
#
# print(a)
# ---------------------------------------------------------------------------------------------------------
# from statistics import mean
#
# list1 = [1, 2, 515]
# print(mean(list1))
# -----------------------------------------------------------------------------------------------------------------
# import click
#
#
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
#
# if __name__ == '__main__':
#     hello()
# ----------------------------------------------------------------------------------------------------------------------
# from colorama import Fore, Back, Style, init
# print (Fore.RED + "some red text")
# print (Back.GREEN + "and with a green background")
# print (Style.DIM + "and in dim text")
# print (Style.RESET_ALL)
# print ("back to normal now!!")
#
# init(autoreset=True)
# print(Fore.RED + "welcome to python !!")
# print("automatically back to default color again")
#
# d= {\"saleCouponList\": \"[]\", \"salesDeptositOrder\": {\"id\": {\"orderNo\": \"\"}, \"customerName\": \"顾问\", \"customerNo\": \"PU2103010007\", \"orderType\": \"\", \"ctCode\": 12391001, \"certificateNo\": \"610204197709053719\", \"customerPhone\": \"13141987412\", \"customerAddress\": \"湖北省武汉市那条街1号\", \"arriveNum\": 1, \"productCode\": \"FPZ-000006 FWS-000003 FNS-000003\", \"brand\": \"CADILLAC\", \"series\": \"FCX-000004\", \"seriesCodeDesc\": \"CT7\", \"model\": \"FXH-000006\", \"modelCodeDesc\": \"2020款 新款 50T 豪华运动型\", \"config\": \"FPZ-000006\", \"configCodeDesc\": \"2020款 新款 50T 豪华运动型\", \"color\": \"FWS-000003\", \"colorCodeDesc\": \"淡黑色\", \"innerColor\": \"FNS-000003\", \"innerColorDesc\": \"亚棕色\", \"directivePrice\": 678514.0, \"quantity\": \"\", \"payMode\": 10251001, \"soldBy\": 88880000002689, \"soldByDesc\": \"销售一\", \"vehiclePrice\": 678514.0, \"depositAmount\": 66666, \"sheetCreatedBy\": 88880000002689, \"sheetCreatedByDesc\": \"销售一\", \"sheetCreateDate\": \"2021-03-06\", \"decorationService\": \"测试-销售装潢项目\", \"decorationAmount\": 1111.11, \"insuranceAmount\": 2222.22, \"loanAmount\": 3333.33, \"agencyAmount\": 4444.44, \"otherItem\": \"测试-其他项目\", \"otherItemAmount\": 5555.55, \"saleCouponInfo\": \"\", \"otherService\": \"测试-其他政策（oa审核）\", \"remark\": \"\", \"remarkHtml\": \"因乙方个性化需求向厂家特定选购的车型（车价包含定制大大项目，价值121元），乙方催告后逾期未交付车辆的，甲方全额退还订金；甲方催告后逾期未提取车辆的，乙方缴纳的订金作为违约金甲方将不予退还;\"}}
#
# s= {\"saleCouponList\": \"[]\", \"salesDeptositOrder\": {\"id\": {\"orderNo\": \"\"}, \"customerName\": \"顾问\", \"customerNo\": \"PU2103010007\", \"orderType\": \"\", \"ctCode\": 12391001, \"certificateNo\": \"610204197709053719\", \"customerPhone\": \"13141987412\", \"customerAddress\": \"湖北省武汉市那条街1号\", \"arriveNum\": 1, \"productCode\": \"FPZ-000006 FWS-000003 FNS-000003\", \"brand\": \"CADILLAC\", \"series\": \"FCX-000004\", \"seriesCodeDesc\": \"CT7\", \"model\": \"FXH-000006\", \"modelCodeDesc\": \"2020款 新款 50T 豪华运动型\", \"config\": \"FPZ-000006\", \"configCodeDesc\": \"2020款 新款 50T 豪华运动型\", \"color\": \"FWS-000003\", \"colorCodeDesc\": \"淡黑色\", \"innerColor\": \"FNS-000003\", \"innerColorDesc\": \"亚棕色\", \"directivePrice\": 678514.0, \"quantity\": \"\", \"payMode\": 10251001, \"soldBy\": 88880000002689, \"soldByDesc\": \"销售一\", \"vehiclePrice\": 678514.0, \"depositAmount\": 66666, \"sheetCreatedBy\": 88880000002689, \"sheetCreatedByDesc\": \"销售一\", \"sheetCreateDate\": \"2021-03-06\", \"decorationService\": \"测试-销售装潢项目\", \"decorationAmount\": 1111.11, \"insuranceAmount\": 2222.22, \"loanAmount\": 3333.33, \"agencyAmount\": 4444.44, \"otherItem\": \"测试-其他项目\", \"otherItemAmount\": 5555.55, \"saleCouponInfo\": \"\", \"otherService\": \"测试-其他政策（oa审核）\", \"remark\": \"\", \"remarkHtml\": \"因乙方个性化需求向厂家特定选购的车型（车价包含定制大大项目，价值121元），乙方催告后逾期未交付车辆的，甲方全额退还订金；甲方催告后逾期未提取车辆的，乙方缴纳的订金作为违约金甲方将不予退还;\"}}
#
# o={"salesDeptositOrder":"{\"id\":{\"entityCode\":\"HD340400\",\"orderNo\":\"DO2103050004\"},\"contractNo\":\"SDPQ/DJ-202103006\",\"soStatus\":33330001,\"customerNo\":\"PU2103030001\",\"customerName\":\"范围\",\"customerPhone\":\"13413513984\",\"brand\":\"CADILLAC\",\"series\":\"FCX-000025\",\"model\":\"FXH-000051\",\"config\":\"FPZ-000051\",\"color\":\"FWS-000025\",\"vin\":null,\"quantity\":1,\"payMode\":10251001,\"vehiclePrice\":555555,\"depositAmount\":55555,\"decorationService\":null,\"decorationAmount\":0,\"insuranceService\":\"交强险,车损险,第三责任险,不计免赔1\",\"insuranceAmount\":0,\"loanService\":\"购车业务咨询1\",\"loanAmount\":0,\"agencyService\":\"代办业务服务1\",\"agencyAmount\":0,\"hxHuibao\":null,\"hxHuibaoAmount\":null,\"hxYanbao\":null,\"hxYanbaoAmount\":null,\"otherService\":null,\"otherAmount\":null,\"remark\":\"\",\"createDate\":\"2021-03-05 16:41:43\",\"createBy\":88880000002689,\"updateDate\":null,\"updateBy\":null,\"soldBy\":88880000002552,\"certificateNo\":\"阿大声道\",\"directivePrice\":550000,\"ctCode\":12391002,\"productCode\":\"FPZ-000051 FWS-000025 FNS-000014\",\"soNo\":null,\"oaAuditAttachment\":null,\"otherItem\":null,\"otherItemAmount\":0,\"invoiceCustomerName\":null,\"invoiceCustomerPhone\":null,\"cancelReason\":null,\"factoryModelId\":null,\"hasSign\":12781002,\"modelNamePrint\":null,\"colorNamePrint\":null,\"vehiclePriceSPrint\":null,\"vehiclePriceBPrint\":null,\"finishDate\":null,\"contractSignDate\":null,\"contractSignImg\":null,\"contractDateImg\":null,\"ver\":1,\"orderType\":92071001,\"soldbySignImg\":null,\"soldbyDateImg\":null,\"useCvr\":null,\"cvrRecordDate\":null,\"signStatus\":10731001,\"idCardImg\":null,\"idCardFrontImg\":null,\"saleCouponInfo\":\"\",\"remarkCode\":null,\"remarkHtml\":\"\",\"oldOrderNo\":\"\",\"businessType\":13001001,\"customerAddress\":\"打算打算打\",\"expireReason\":null,\"soldByDesc\":\"何新\",\"sheetCreateDate\":\"2021-03-05\",\"sheetCreatedBy\":88880000002689,\"sheetCreatedByDesc\":\"销售一\",\"deliveringDate\":\"2021-03-05 00:00:00\",\"rejectedReasonCode\":null,\"idCardImgString\":null,\"idCardFrontImgString\":null,\"arriveNum\":1,\"seriesCodeDesc\":\"DU1\",\"modelCodeDesc\":\"无限价设置车型数据-纵享丝滑\",\"configCodeDesc\":\"无限价设置车型数据-纵享丝滑\",\"colorCodeDesc\":\"南极光\",\"innerColorDesc\":\"北极光\"}"}
#
# aa = {"bill_code":"BI20210310161051211E569","company_code":"HD340400","groupCodeOrigin":["HD340400-JT0039","HD340400-JT0037","HD340400-JT0038","HD420650-JT0039","HD340400-JT0035","HD420650-JT0038","HD340400-JT0036","HD420650-JT0037","HD000000-JT0038","HD340400-JT0033","HD000000-JT0039","HD340400-JT0034","HD340400-JT0031","HD340400-JT0032","HD340400-JT0030","HD000000-JT0041","HD000000-JT0042","HD000000-JT0043","HD000000-JT0044","HD000000-JT0045","HD000000-JT0046","HD000000-JT0047","HD000000-JT0048","HD420650-JT0047","HD420650-JT0046","HD420650-JT0045","HD420650-JT0044","HD420650-JT0043","HD420650-JT0042","HD420650-JT0041","HD000000-JT0040","HD420650-JT0040","HD340400-JT0048","HD420650-JT0029","HD340400-JT0049","HD420650-JT0028","HD340400-JT0046","HD420650-JT0027","HD340400-JT0047","HD420650-JT0026","HD000000-JT0027","HD340400-JT0044","HD000000-JT0028","HD340400-JT0045","HD000000-JT0029","HD340400-JT0042","HD340400-JT0043","HD340400-JT0040","HD340400-JT0041","HD000000-JT0030","HD000000-JT0031","HD000000-JT0032","HD000000-JT0033","HD000000-JT0034","HD000000-JT0035","HD000000-JT0036","HD000000-JT0037","HD420650-JT0036","HD420650-JT0035","HD420650-JT0034","HD420650-JT0033","HD420650-JT0032","HD420650-JT0031","HD420650-JT0030","HD340400-JT0053","HD340400-JT0051","HD340400-JT0052","HD340400-JT0050","HD420650-JT0049","HD420650-JT0048","HD000000-JT0049","HD000000-JT0052","HD420650-JT0050","HD000000-JT0053","HD420650-JT0053","HD000000-JT0050","HD420650-JT0052","HD000000-JT0051","HD420650-JT0051","HD340400-DC0006","HD340400-SS0010","HD340400-DC0005","HD340400-DC0008","HD420650-DC0007","HD340400-DC0007","HD420650-DC0008","HD420650-SS0010","HD420650-SS0011","HD340400-SS0011","HD420650-DC0001","HD420650-DC0002","HD420650-DC0005","HD420650-DC0006","HD420650-DC0003","HD420650-DC0004","HD000000-JT0001","HD000000-JT0002","HD000000-JT0003","HD340400-DC0002","HD340400-DC0001","HD340400-DC0004","HD340400-DC0003","HD420650-SS0002","HD420650-SS0003","HD420650-SS0004","HD420650-SS0005","HD340400-SS0003","HD340400-SS0002","HD340400-SS0001","HD420650-SS0001","HD420650-SS0006","HD420650-SS0007","HD420650-SS0008","HD420650-SS0009","HD340400-SS0007","HD340400-SS0006","HD340400-SS0005","HD340400-SS0004","HD340400-SS0009","HD340400-SS0008","HD000000-JT0016","HD000000-JT0017","HD000000-JT0018","HD000000-JT0019","HD000000-JT0020","HD000000-JT0021","HD000000-JT0022","HD000000-JT0023","HD000000-JT0024","HD000000-JT0026","HD000000-JT0005","HD000000-JT0006","HD000000-JT0007","HD000000-JT0008","HD000000-JT0009","HD000000-JT0010","HD000000-JT0011","HD000000-JT0012","HD000000-JT0013","HD000000-JT0014","HD000000-JT0015","HD000000-DC0008","HD000000-SS0010","HD000000-SS0011","HD000000-DC0004","HD000000-DC0005","HD000000-DC0006","HD000000-DC0007","HD000000-DC0001","HD000000-DC0002","HD000000-DC0003","HD420650-JT0003","HD420650-JT0002","HD420650-JT0001","HD000000-SS0005","HD340400-JT0008","HD000000-SS0006","HD340400-JT0009","HD000000-SS0003","HD340400-JT0006","HD000000-SS0004","HD340400-JT0007","HD000000-SS0001","HD000000-SS0002","HD340400-JT0005","HD340400-JT0002","HD340400-JT0003","HD340400-JT0001","HD000000-SS0009","HD000000-SS0007","HD000000-SS0008","HD340400-JT0019","HD340400-JT0017","HD340400-JT0018","HD420650-JT0019","HD340400-JT0015","HD420650-JT0018","HD340400-JT0016","HD420650-JT0017","HD340400-JT0013","HD420650-JT0016","HD340400-JT0014","HD420650-JT0015","HD340400-JT0011","HD340400-JT0012","HD340400-JT0010","HD420650-JT0024","HD420650-JT0023","HD420650-JT0022","HD420650-JT0021","HD420650-JT0020","HD340400-JT0028","HD420650-JT0009","HD340400-JT0029","HD420650-JT0008","HD340400-JT0026","HD420650-JT0007","HD340400-JT0027","HD420650-JT0006","HD340400-JT0024","HD420650-JT0005","HD340400-JT0022","HD340400-JT0023","HD340400-JT0020","HD340400-JT0021","HD420650-JT0014","HD420650-JT0013","HD420650-JT0012","HD420650-JT0011","HD420650-JT0010"],"userCodeOrigin":88880000020602,"userNameOrigin":"销售一","depCode":None,"posCode":"GW00021","companyCode":"HD340400","companyName":"合肥华通"}

# print(aa)
# dd = {"page":1,"perPage":15,"moduleBillCode":"DO2103100008","pageType":10,"groupCodeOrigin":["HD340400-JT0039","HD340400-JT0037","HD340400-JT0038","HD420650-JT0039","HD340400-JT0035","HD420650-JT0038","HD340400-JT0036","HD420650-JT0037","HD000000-JT0038","HD340400-JT0033","HD000000-JT0039","HD340400-JT0034","HD340400-JT0031","HD340400-JT0032","HD340400-JT0030","HD000000-JT0041","HD000000-JT0042","HD000000-JT0043","HD000000-JT0044","HD000000-JT0045","HD000000-JT0046","HD000000-JT0047","HD000000-JT0048","HD420650-JT0047","HD420650-JT0046","HD420650-JT0045","HD420650-JT0044","HD420650-JT0043","HD420650-JT0042","HD420650-JT0041","HD000000-JT0040","HD420650-JT0040","HD340400-JT0048","HD420650-JT0029","HD340400-JT0049","HD420650-JT0028","HD340400-JT0046","HD420650-JT0027","HD340400-JT0047","HD420650-JT0026","HD000000-JT0027","HD340400-JT0044","HD000000-JT0028","HD340400-JT0045","HD000000-JT0029","HD340400-JT0042","HD340400-JT0043","HD340400-JT0040","HD340400-JT0041","HD000000-JT0030","HD000000-JT0031","HD000000-JT0032","HD000000-JT0033","HD000000-JT0034","HD000000-JT0035","HD000000-JT0036","HD000000-JT0037","HD420650-JT0036","HD420650-JT0035","HD420650-JT0034","HD420650-JT0033","HD420650-JT0032","HD420650-JT0031","HD420650-JT0030","HD340400-JT0053","HD340400-JT0051","HD340400-JT0052","HD340400-JT0050","HD420650-JT0049","HD420650-JT0048","HD000000-JT0049","HD000000-JT0052","HD420650-JT0050","HD000000-JT0053","HD420650-JT0053","HD000000-JT0050","HD420650-JT0052","HD000000-JT0051","HD420650-JT0051","HD340400-DC0006","HD340400-SS0010","HD340400-DC0005","HD340400-DC0008","HD420650-DC0007","HD340400-DC0007","HD420650-DC0008","HD420650-SS0010","HD420650-SS0011","HD340400-SS0011","HD420650-DC0001","HD420650-DC0002","HD420650-DC0005","HD420650-DC0006","HD420650-DC0003","HD420650-DC0004","HD000000-JT0001","HD000000-JT0002","HD000000-JT0003","HD340400-DC0002","HD340400-DC0001","HD340400-DC0004","HD340400-DC0003","HD420650-SS0002","HD420650-SS0003","HD420650-SS0004","HD420650-SS0005","HD340400-SS0003","HD340400-SS0002","HD340400-SS0001","HD420650-SS0001","HD420650-SS0006","HD420650-SS0007","HD420650-SS0008","HD420650-SS0009","HD340400-SS0007","HD340400-SS0006","HD340400-SS0005","HD340400-SS0004","HD340400-SS0009","HD340400-SS0008","HD000000-JT0016","HD000000-JT0017","HD000000-JT0018","HD000000-JT0019","HD000000-JT0020","HD000000-JT0021","HD000000-JT0022","HD000000-JT0023","HD000000-JT0024","HD000000-JT0026","HD000000-JT0005","HD000000-JT0006","HD000000-JT0007","HD000000-JT0008","HD000000-JT0009","HD000000-JT0010","HD000000-JT0011","HD000000-JT0012","HD000000-JT0013","HD000000-JT0014","HD000000-JT0015","HD000000-DC0008","HD000000-SS0010","HD000000-SS0011","HD000000-DC0004","HD000000-DC0005","HD000000-DC0006","HD000000-DC0007","HD000000-DC0001","HD000000-DC0002","HD000000-DC0003","HD420650-JT0003","HD420650-JT0002","HD420650-JT0001","HD000000-SS0005","HD340400-JT0008","HD000000-SS0006","HD340400-JT0009","HD000000-SS0003","HD340400-JT0006","HD000000-SS0004","HD340400-JT0007","HD000000-SS0001","HD000000-SS0002","HD340400-JT0005","HD340400-JT0002","HD340400-JT0003","HD340400-JT0001","HD000000-SS0009","HD000000-SS0007","HD000000-SS0008","HD340400-JT0019","HD340400-JT0017","HD340400-JT0018","HD420650-JT0019","HD340400-JT0015","HD420650-JT0018","HD340400-JT0016","HD420650-JT0017","HD340400-JT0013","HD420650-JT0016","HD340400-JT0014","HD420650-JT0015","HD340400-JT0011","HD340400-JT0012","HD340400-JT0010","HD420650-JT0024","HD420650-JT0023","HD420650-JT0022","HD420650-JT0021","HD420650-JT0020","HD340400-JT0028","HD420650-JT0009","HD340400-JT0029","HD420650-JT0008","HD340400-JT0026","HD420650-JT0007","HD340400-JT0027","HD420650-JT0006","HD340400-JT0024","HD420650-JT0005","HD340400-JT0022","HD340400-JT0023","HD340400-JT0020","HD340400-JT0021","HD420650-JT0014","HD420650-JT0013","HD420650-JT0012","HD420650-JT0011","HD420650-JT0010"],"userCodeOrigin":88880000020602,"userNameOrigin":"销售一","depCode":None,"posCode":"GW00021","companyCode":"HD340400","companyName":"合肥华通"}
# print(dd)
#
#
# ff = {'companyCode': 'HD340400', 'companyName': '合肥华通', 'depCode': None, 'groupCodeOrigin': ['HD340400-JT0039', 'HD340400-JT0037', 'HD340400-JT0038', 'HD420650-JT0039', 'HD340400-JT0035', 'HD420650-JT0038', 'HD340400-JT0036', 'HD420650-JT0037', 'HD000000-JT0038', 'HD340400-JT0033', 'HD000000-JT0039', 'HD340400-JT0034', 'HD340400-JT0031', 'HD340400-JT0032', 'HD340400-JT0030', 'HD000000-JT0041', 'HD000000-JT0042', 'HD000000-JT0043', 'HD000000-JT0044', 'HD000000-JT0045', 'HD000000-JT0046', 'HD000000-JT0047', 'HD000000-JT0048', 'HD420650-JT0047', 'HD420650-JT0046', 'HD420650-JT0045', 'HD420650-JT0044', 'HD420650-JT0043', 'HD420650-JT0042', 'HD420650-JT0041', 'HD000000-JT0040', 'HD420650-JT0040', 'HD340400-JT0048', 'HD420650-JT0029', 'HD340400-JT0049', 'HD420650-JT0028', 'HD340400-JT0046', 'HD420650-JT0027', 'HD340400-JT0047', 'HD420650-JT0026', 'HD000000-JT0027', 'HD340400-JT0044', 'HD000000-JT0028', 'HD340400-JT0045', 'HD000000-JT0029', 'HD340400-JT0042', 'HD340400-JT0043', 'HD340400-JT0040', 'HD340400-JT0041', 'HD000000-JT0030', 'HD000000-JT0031', 'HD000000-JT0032', 'HD000000-JT0033', 'HD000000-JT0034', 'HD000000-JT0035', 'HD000000-JT0036', 'HD000000-JT0037', 'HD420650-JT0036', 'HD420650-JT0035', 'HD420650-JT0034', 'HD420650-JT0033', 'HD420650-JT0032', 'HD420650-JT0031', 'HD420650-JT0030', 'HD340400-JT0053', 'HD340400-JT0051', 'HD340400-JT0052', 'HD340400-JT0050', 'HD420650-JT0049', 'HD420650-JT0048', 'HD000000-JT0049', 'HD000000-JT0052', 'HD420650-JT0050', 'HD000000-JT0053', 'HD420650-JT0053', 'HD000000-JT0050', 'HD420650-JT0052', 'HD000000-JT0051', 'HD420650-JT0051', 'HD340400-DC0006', 'HD340400-SS0010', 'HD340400-DC0005', 'HD340400-DC0008', 'HD420650-DC0007', 'HD340400-DC0007', 'HD420650-DC0008', 'HD420650-SS0010', 'HD420650-SS0011', 'HD340400-SS0011', 'HD420650-DC0001', 'HD420650-DC0002', 'HD420650-DC0005', 'HD420650-DC0006', 'HD420650-DC0003', 'HD420650-DC0004', 'HD000000-JT0001', 'HD000000-JT0002', 'HD000000-JT0003', 'HD340400-DC0002', 'HD340400-DC0001', 'HD340400-DC0004', 'HD340400-DC0003', 'HD420650-SS0002', 'HD420650-SS0003', 'HD420650-SS0004', 'HD420650-SS0005', 'HD340400-SS0003', 'HD340400-SS0002', 'HD340400-SS0001', 'HD420650-SS0001', 'HD420650-SS0006', 'HD420650-SS0007', 'HD420650-SS0008', 'HD420650-SS0009', 'HD340400-SS0007', 'HD340400-SS0006', 'HD340400-SS0005', 'HD340400-SS0004', 'HD340400-SS0009', 'HD340400-SS0008', 'HD000000-JT0016', 'HD000000-JT0017', 'HD000000-JT0018', 'HD000000-JT0019', 'HD000000-JT0020', 'HD000000-JT0021', 'HD000000-JT0022', 'HD000000-JT0023', 'HD000000-JT0024', 'HD000000-JT0026', 'HD000000-JT0005', 'HD000000-JT0006', 'HD000000-JT0007', 'HD000000-JT0008', 'HD000000-JT0009', 'HD000000-JT0010', 'HD000000-JT0011', 'HD000000-JT0012', 'HD000000-JT0013', 'HD000000-JT0014', 'HD000000-JT0015', 'HD000000-DC0008', 'HD000000-SS0010', 'HD000000-SS0011', 'HD000000-DC0004', 'HD000000-DC0005', 'HD000000-DC0006', 'HD000000-DC0007', 'HD000000-DC0001', 'HD000000-DC0002', 'HD000000-DC0003', 'HD420650-JT0003', 'HD420650-JT0002', 'HD420650-JT0001', 'HD000000-SS0005', 'HD340400-JT0008', 'HD000000-SS0006', 'HD340400-JT0009', 'HD000000-SS0003', 'HD340400-JT0006', 'HD000000-SS0004', 'HD340400-JT0007', 'HD000000-SS0001', 'HD000000-SS0002', 'HD340400-JT0005', 'HD340400-JT0002', 'HD340400-JT0003', 'HD340400-JT0001', 'HD000000-SS0009', 'HD000000-SS0007', 'HD000000-SS0008', 'HD340400-JT0019', 'HD340400-JT0017', 'HD340400-JT0018', 'HD420650-JT0019', 'HD340400-JT0015', 'HD420650-JT0018', 'HD340400-JT0016', 'HD420650-JT0017', 'HD340400-JT0013', 'HD420650-JT0016', 'HD340400-JT0014', 'HD420650-JT0015', 'HD340400-JT0011', 'HD340400-JT0012', 'HD340400-JT0010', 'HD420650-JT0024', 'HD420650-JT0023', 'HD420650-JT0022', 'HD420650-JT0021', 'HD420650-JT0020', 'HD340400-JT0028', 'HD420650-JT0009', 'HD340400-JT0029', 'HD420650-JT0008', 'HD340400-JT0026', 'HD420650-JT0007', 'HD340400-JT0027', 'HD420650-JT0006', 'HD340400-JT0024', 'HD420650-JT0005', 'HD340400-JT0022', 'HD340400-JT0023', 'HD340400-JT0020', 'HD340400-JT0021', 'HD420650-JT0014', 'HD420650-JT0013', 'HD420650-JT0012', 'HD420650-JT0011', 'HD420650-JT0010'], 'moduleBillCode': 'DO2103110020', 'page': 1, 'pageType': 10, 'perPage': 15, 'userCodeOrigin': 88880000020602, 'userNameOrigin': '销售一', 'posCode': 'GW00021'}

# import time
# timeNum=1615527415157  # 毫秒时间戳
# timeTemp = float(timeNum/1000)
# tupTime = time.localtime(timeTemp)
# stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
# print(stadardTime)
#
# import time
# import datetime
#
# t = time.time()
# # 浮点时间
# print(t)
#
# # 10位时间戳 (秒)
# print(int(t))
#
# # 13位 时间戳 (毫秒)
# print(int(round(t * 1000)))
#
# timeStamp = 1617692174189
#
# local_str_time = datetime.datetime.fromtimestamp(timeStamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
#
# print(local_str_time)

# timeArray = time.localtime(timeStamp)
#
# otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
#
# print(otherStyleTime)  # 2013--10--10 23:40:00

# dateArray = datetime.datetime.fromtimestamp(timeStamp)
# otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
# print(otherStyleTime)

# table = [{"ex": [{"attr_name": "VIN", "attr_module_name": "vin", "value_row": "['ASUHUY6T5R4E3WT6Y','GYHY67U8U8I9I8U7']"},
#                  {"attr_name": "仓库名称", "attr_module_name": "storageName", "value_row": "['\u6574\u8f66\u4ed3\u5e93','\u6574\u8f66\u4ed3\u5e93']"}]}]
#
# ll = eval(table[0]["ex"][0]['value_row'])
# la = [{} for i in range(len(ll))]
#
# for i in range(2):
#     ll = eval(table[0]["ex"][i]['value_row'])
#     for j in range(2):
#         la[j][table[0]["ex"][i]['attr_module_name']] = ll[j]




# for i in range(2):
#     la[i]['attr_module_name'] = ll[i]

# print(la)


# aa = {"salesOrderDetailVoStr":"{\"abortingReason\":null,\"allocatingType\":null,\"soNo\":null,\"soStatus\":13011010,\"fixedAssetsType\":null,\"payMode\":10251001,\"mediaType\":null,\"stockOutDate\":null,\"payOff\":null,\"sheetCreateDate\":\"2021-03-22 13:39:11\",\"sheetCreatedBy\":88880000002689,\"sheetCreatedByDesc\":\"销售一\",\"createByDesc\":null,\"customerNo\":\"PU2103190001\",\"customerName\":\"杨涛\",\"prePay\":null,\"phone\":\"13632548529\",\"relatedOrderNo\":null,\"contractNo\":null,\"oldVin\":null,\"oldLicense\":null,\"fristOwnerDriver\":null,\"secondOwnerDriver\":null,\"businessOpportunityDesc\":null,\"venderLocalCheck\":null,\"mediaCustomerCode\":null,\"isBuyCommercialInsurance\":null,\"remarkCode\":null,\"remarkHtml\":\"经甲乙双方友好协商，乙方自愿支付车辆运输费用555元;\",\"oaAuditRemark\":\"OA审核备注\",\"oaAttachFileId\":null,\"fileName\":null,\"contractDate\":\"2021-03-22 13:39:11\",\"contractEarnest\":null,\"deliveryMode\":13021001,\"deliveringDate\":\"2021-03-24T16:00:00.000Z\",\"invoiceMode\":13031001,\"address\":\"那条街1号\",\"depositAmount\":null,\"customerType\":10181001,\"ctCode\":12391002,\"certificateNo\":\"343434324234234234234\",\"soldBy\":96690000012546,\"soldByDesc\":\"徐春艳\",\"purchaseType\":null,\"oldBrandSeries\":null,\"contactorName\":\"杨涛\",\"loanFlag\":null,\"coupon\":null,\"productCode\":\"FPZ-000006 FWS-000003 FNS-000003\",\"productName\":\"2020款 新款 50T 豪华运动型\",\"vin\":\"ML8PUG6Z4T3JW5V0D\",\"storageCode\":\"ZCCK\",\"storagePositionCode\":null,\"dispatchedDate\":\"2021-03-22\",\"dispatchedBy\":88880000002689,\"warehouse\":null,\"directivePrice\":678514,\"actualPrice\":660000,\"cashSaleDiscount\":18514,\"newCarDiscount\":10000,\"secondHandCarDiscount\":2000,\"bigCustomerDiscount\":3000,\"otherDiscount\":3514,\"estimateInsCommission\":11,\"financeRebate\":22,\"estimateCommission\":33,\"bigCustomersCommission\":44,\"secondHandCommission\":55,\"purchasePrice\":616524,\"derivedRemark\":\"衍生条款备注\",\"decorationAmount\":null,\"secondCarVin\":null,\"remark\":null,\"orderType\":92071001,\"oaRemark\":null,\"vehicleAmount\":null,\"rebate\":\"25846.00\",\"vehicleGrossProfit\":null,\"extendTotalAmount\":null,\"extendTotalGrossProfit\":null,\"orderTotalAmount\":null,\"ordertotalGrossProfit\":null,\"brandCode\":\"CADILLAC\",\"seriesCode\":\"FCX-000004\",\"seriesCodeDesc\":\"CT7\",\"modelCode\":\"FXH-000006\",\"modelCodeDesc\":\"2020款 新款 50T 豪华运动型\",\"configCode\":\"FPZ-000006\",\"configCodeDesc\":\"2020款 新款 50T 豪华运动型\",\"innerColor\":\"FNS-000003\",\"innerColorDesc\":\"亚棕色\",\"colorCode\":\"FWS-000003\",\"colorCodeDesc\":\"淡黑色\",\"isLoan\":12781002,\"financialInstitution\":null,\"maintenanceOnlyCode\":null,\"threeGuaranteesOnlyCode\":null,\"tempVin\":null,\"isRealChange\":null,\"realChangeVin\":\"DDEDEDEDEDEDEDEDE\",\"otherAmountObject\":[11981003,11981004],\"otherAmount\":66,\"lossReplacementProfit\":77,\"discountRefundAmount\":88,\"decorationDerateAmount\":99,\"isHasDiscount\":12781001,\"discountItem\":[14111001,14111003],\"otherServiceSum\":null,\"orderSum\":678514,\"orderReceivableSum\":\"660000.00\",\"carReceivableSum\":null,\"vehicleFavorableSubsidy\":null,\"marginalStandard\":1,\"storeNum\":2,\"engineNo\":\"EQ8100Q1\",\"certificateNumber\":\"SQ67IJ692\",\"isModifyDerivedBusiness\":null,\"businessType\":null,\"relatedDecorationOrderList\":[],\"cancelRelatedDecorationOrderList\":[],\"relatedServiceOrderList\":[],\"cancelRelatedServiceOrderList\":[],\"relatedLoanOrderList\":[],\"cancelRelatedLoanOrderList\":[],\"idCardImgString\":null,\"order_receivable_sum\":660000,\"printAmountSum\":66,\"order_sum\":678514,\"dispatchedByDesc\":\"销售一\"}"}
# print(aa)
from dataGenerated.randomData import random_vin

# aa = '6DKEX4825TJ7UZ51P,SEJC645A5HTLMYGR2'
# bb = ['A5FCPZJU9RSB17EY9']
# cc = ','.join(bb)
# if aa == cc:
#     print(11)
# print(cc)
import requests
# from common.configHttp import RunMain
#
#
# file_path = r"C:\Users\cpr264\Desktop\JPG测试图片.jpg"
#
# # headers = RunMain().get_token()
# # headers["Content-Type"] = "multipart/form-data"
# # del headers["Content-Type"]
# url = "https://dms.t.hxqcgf.com/apigateway/system/attachInfo/api/fileUpload"
# file = open(file_path, 'rb')
# files = [("file", ("JPG测试图片.jpg", file, "image/jpeg"))]
# # print(headers)
# print(files)
# # res = requests.post(url, headers=headers, data={}, files=files)
# # print(res.json())
#
# res = RunMain().run_main('post', url, files=files)
# print(res)
# print(res["data"])
# dd = eval(res["data"])
# print(dd["newFileName"])
import random, json

# second = [3, 4, 5, 7, 8][random.randint(0, 4)]
#
# print(second)

# current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#
#
# import datetime
#
# today = datetime.date.today()
# oneday = datetime.timedelta(days=2)
# yesterday = today-oneday
#
# tomorrow=today+oneday
#
# print(type(tomorrow))
# print(tomorrow)

from datetime import timedelta,datetime


# def get_date(date, time_interval):
#     """
#
#     :param date:                    间隔的时间 整型  前几天 为负数 100 后几天为正数 -100
#     :param time_interval:           字符类型时间 年月日   ‘20200101’
#     :return:                        字符类型时间 年月日   ‘20200101’
#     """
#     start_date = datetime.strptime(date, '20210424')
#     now_date = timedelta(days=time_interval)
#     a = start_date + now_date
#
#     return a.strftime('20210424')
#
# print(get_date(2, "20210424"))

# import datetime
# d1 = datetime.datetime.now()
# d3 = d1 - datetime.timedelta(days=10)
# print(d1)
# print(d3.strftime("%Y-%m-%d"))


# a=0.2343545434564
#
# print('%.4f'%a)
# # print('%3f'%a)
# # print('%03f'%a)
# # print('%15f'%a)
#
# s = 3
# g = 3
# c = "%.4f" % (s/g)
# print(c)
# print(type(c))

# a = " 21321 "
# b = a.strip()
# print(b)
from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime

from pymongo import MongoClient
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


# 输出时间
# def job():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler


# scheduler = BlockingScheduler()
# scheduler.add_job(job, 'cron', day_of_week='1-5', hour=17, minute=15)
# scheduler.add_job(job, 'interval', seconds=5)
# scheduler.start()


# MongoDB 参数
# host = '127.0.0.1'
# port = 27017
# client = MongoClient(host, port)

# 存储方式
# jobstores = {
#     'mongo': MongoDBJobStore(collection='job', database='test', client=client),
#     'default': MemoryJobStore()
# }
# executors = {
#     'default': ThreadPoolExecutor(10),
#     'processpool': ProcessPoolExecutor(3)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }
# scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
# scheduler.add_job(job, 'interval', seconds=5, jobstore='mongo')
# scheduler.start()

# import threading
#
#
# ll = ["A08D", "A00Y", "E55E"]
#
#
# def send_request(name):
#     headers = {
#         "Authorization": "Basic c2NvOmRtcw==",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
#     }
#     params = {
#         "username": name,
#         "password": "QLomgFGYMWCiBg953bt8Mw==",
#         "entitycode": "HD340400",
#         "isRemember": "true",
#         "grant_type": "password"
#     }
#     url = "https://dms.t.hxqcgf.com/apigateway/auth/oauth/token"
#     res_dict = requests.get(url, headers=headers, params=params).json()
#     # print(res_dict, sep="\n")
#     access_token = res_dict["access_token"]
#     print(access_token)
#
#
# def test_one(name):
#     for j in range(10):
#         send_request(name)
#
#
# threads = []
# for i in range(len(ll)):
#     t = threading.Thread(target=test_one, args=(ll[i],), name="T" + str(i))
#     t.setDaemon(True)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()


# def ll(a, b, c):
#     print(a*b/(1-c))
#
#
# ll(340.36, 1.13, 0.3)
# import requests
#
#
# headers = {
#         "Authorization": "Basic c2NvOmRtcw==",
#         # "Authorization": "Bearer f47351dc-7804-4511-91d9-18e675be47ac",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
#     }
# params = {
#     "username": "A08D",
#     "password": "QLomgFGYMWCiBg953bt8Mw==",
#     "entitycode": "HD340400",
#     "isRemember": "true",
#     "grant_type": "password"
# }
# url = "https://dms.t.hxqcgf.com/apigateway/auth/oauth/token"
# res = requests.get(url, headers=headers, params=params).json()
# token_type = res["token_type"]
# access_token = res["access_token"]
# # 将token放进请求头里
# token = "{} {}".format(token_type, access_token)
#
# headers["Authorization"] = "Bearer 0fd53311-983a-4448-9d58-7f8fccf97e11"
# headers["Content-Type"] = "application/x-www-form-urlencoded"


# url1 = "https://dms.t.hxqcgf.com/apigateway/parts/partStock/getPartStockList"
# params = {"searchData": {"mainGroupCode": "00", "subGroupCode": "0005", "stockQuantity": 12781002, "subGroupName": "精品"},
#           "offset": 0, "limit": 20}
#
# res = requests.get(url1, params=params, headers=headers).json()
# print(res)
# print(headers)
# list1 = []
# for i in res["data"]["list"]:
#     list1.append(i["part_no"])
#
# url2 = "https://dms.t.hxqcgf.com/apigateway/report/salesOrderFeignUtils/getPartStockList"
#
# params = {
#         "limit": 1300,
#         "offset": 0,
#         "searchData": {"typeCode":99961001}
# }
# res = requests.get(url1, params=params, headers=headers).json()
# list2 = []
# for i in res["data"]["list"]:
#     list1.append(i["partNo"])
# if len(list1) >= len(list2):
#     for i in list1:
#         if i not in list2:
#             print(i)
# import pytest
# import time
#
#
# def test_01():
#     time.sleep(2)
#     print('这里是testcase01')
#
#
# def test_02():
#     time.sleep(3)
#     print('这里是testcase02')
#
#
# def test_03():
#     time.sleep(4)
#     print('这里是testcase03')
#
#
# def test_04():
#     time.sleep(5)
#     print('这里是testcase04')
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', __file__, '-n=2'])


from math import radians, cos, sin, asin, sqrt
from geopy.distance import geodesic


# 公式计算两点间距离（m）

def geodistance(lng1, lat1, lng2, lat2):
    # lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance / 1000, 3)
    return distance

    # 返回 446.721 千米

# 调用geopy包中的方法
print(geodesic((22.537046, 114.058992), (30.472123, 114.338239)).m)  # 计算两个坐标直线距离
print(geodesic((22.537046, 114.058992), (30.472123, 114.338239)).km)  # 计算两个坐标直线距离
# 返回 447.2497993542003 千米

# 南昌：华东交通大学（120.12802999999997,30.28708）
# 杭州：浙江工商大学（115.86572000000001,28.7427）
# 用百度地图测量结果：447.02km

print(geodistance(114.058992, 22.537046, 114.338239, 30.472123))


