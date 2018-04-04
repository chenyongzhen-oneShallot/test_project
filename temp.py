def send_mail(filepath,to_list, sub, content):
    # 创建一个带附件的实例
    msg = MIMEMultipart('alternative')
    #msg['Subject'] = Header("subject", 'utf-8')

    # html格式构造
    content2='''数据统计从3月1日创建时间开始\n
更多信息请查下http://172.16.0.140:8000/libra/bug/?type=day#'''

    html = """
    <html> 
      <head></head> 
      <body> 
          <p>
            大家好：
              <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;以下是本日缺陷统计报告，请查收！
           <br><img src="cid:image1"></br> 
          </p>
          <p style="font-size:12;color:gray">
        说明：
           <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;1、其他分类包含：产品、平台服务部、UI、测试等处理的缺陷
        <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;2、数据统计从3月1日创建时间开始，每日数据周期为前一日20点到当日20点
        <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;3、更多信息请查下
            <a href=http://172.16.0.140:8000/libra/bug/?type=day#>http://172.16.0.140:8000/libra/bug/?type=day#</a>
          </p>
      </body> 
    </html> 
    """
    htm = MIMEText(html, 'html', 'utf-8')
    msg.attach(htm)

    # 正文
    #     txt1=MIMEText(content,_subtype='html',_charset='gb2312')
    #     msg.attach(txt1)
    # 添加附件
    # att1 = MIMEText(open('file\\123.txt', 'rb').read(), 'base64', 'gb2312')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = \
    #     'attachment; filename="123.txt"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # msg.attach(att1)

    # att2 = MIMEText(open('file\\abc.png', 'rb').read(), 'base64', 'gb2312')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = \
    #     'attachment; filename="abc.png"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # msg.attach(att2)
    #     添加图片

    file1 = str(filepath)
    fp = open(file1, 'rb')
    image = MIMEImage(fp.read())
    fp.close()
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    #me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    #     msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = "禅道"
    #msg['To'] = ";".join(to_list)
    msg['To'] = ','.join(to_list)
    sender = mail_user
    receivers = to_list
    # try:
    #s = smtplib.SMTP_SSL(mail_host, 465)
    s = smtplib.SMTP(mail_host, 25)
    s.login(mail_user, mail_pass)
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()
    return True
    # except:
    #     print ("when connect,exception")
    #     return False


# if send_mail("../file/abc.png",['245224130@qq.com'], "[RCA_FTP_Download]","TTTTTTTTTTTEEEEEEEEEESSSSSSSSSSSSSSSTTTTTTTTTT"):
#     print ("send success")
# else:
#     print ("send failed")


