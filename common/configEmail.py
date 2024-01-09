import os
import time
# import win32com.client as win32
import datetime
import readConfig
import getpathInfo
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
# app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
to = read_conf.get_email('to')  # 从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件抄送人
fake_date = time.strftime('%Y%m%d', time.localtime(time.time()))
# mail_path = os.path.join(getpathInfo.get_path(), 'result', 'report', '{}.html'.format(fake_date))  # 获取测试报告路径
mail_path = os.path.join(getpathInfo.get_path(), 'result', 'logs')  # 获取测试报告路径


class SendEmail(object):
    # @staticmethod
    # def out_look():
    #     olook = win32.Dispatch("%s.Application" % app)
    #     mail = olook.CreateItem(win32.constants.olMailItem)
    #     mail.To = addressee  # 收件人
    #     mail.CC = cc  # 抄送
    #     mail.Subject = str(datetime.datetime.now())[0:19] + '%s' % subject  # 邮件主题
    #     mail.Attachments.Add(mail_path, 1, 1, "myFile")
    #     content = """
    #                 执行测试中……
    #                 测试已完成！！
    #                 生成报告中……
    #                 报告已生成……
    #                 报告已邮件发送！！
    #                 """
    #     mail.Body = content
    #     mail.Send()

    @staticmethod
    def fox_mail():
        # 第一步：连接到smtp服务器
        smtp = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
        # 第二步：登录smtp服务器
        smtp.login(user='1655719335@qq.com', password='ofyiqlkwtwgpcbec')
        # 第三步构建一封带附件的邮件
        # 创建一封多组件的邮件
        msg = MIMEMultipart()
        # 添加发件人
        msg['From'] = cc
        # 添加收件人
        msg['To'] = to
        # 添加主题
        msg['Subject'] = Header(subject, charset='utf8')
        try:
            # 添加邮件文本内容
            with open(mail_path, 'rb') as f:
                html = f.read()
                # 创建邮件文件内容对象
                text_content = MIMEText(html, _charset='utf8')
                # 把邮件的文本内容，添加到多组件的邮件中
                msg.attach(text_content)
                # 添加附件
                att = MIMEApplication(html)
                att.add_header('content-disposition', 'attachment', filename='{}_report.html'.format(fake_date))
                msg.attach(att)
            # 发送邮件
            smtp.send_message(msg=msg, from_addr=cc, to_addrs=to)
            print("邮件发送成功")
        except Exception as e:
            print("发送失败：{}".format(e))


if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    SendEmail().fox_mail()
