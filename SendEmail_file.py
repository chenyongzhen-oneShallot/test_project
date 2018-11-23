# encoding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import unittest
import time
import os


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


## ==============定义发送附件邮件==========
def send_file(file_new):
    smtpserver = 'smtp.163.com'
    user = ''
    password = ''
    sender = ''
    receiver = ['']
    # subject='**自动化测试报告'
    file = open(file_new, 'r').read()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    subject = 'OpenAPI自动化测试报告--' + now
    # att=MIMEText(sendfile,"base64","utf-8")
    att = MIMEText(file, "html", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["ContenT-Disposition"] = "attachment;filename = 'OpenAPI自动化测试报告.html '"

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = ''
    msgRoot['To'] = ""
    # msgRoot.attach(att)
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    # lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序 win
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # linux
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new
