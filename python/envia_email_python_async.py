#!/usr/bin/env python
# -*- coding:utf-8
import multiprocessing
import datetime as dt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = 'XXXXXXXXX'
sender = 'cicerocasj@gmail.com'
receivers = [sender, 'ronaldo.andrade_funcate@inpe.br', sender, 'ronaldo.andrade_funcate@inpe.br']
subject = "Assunto do email"
message = "Apresentação de texto em utf-8 <br><h1>Tag HTML h1</h1>"
message_text = """<html><head><meta charset="utf-8"></head><body>{mensagem}</body></html>""".format(
    assunto=subject, mensagem=message
)

MESSAGE = MIMEMultipart('alternative')
MESSAGE['subject'] = subject
MESSAGE['From'] = sender

HTML_BODY = MIMEText(message_text, 'html', "utf-8")
MESSAGE.attach(HTML_BODY)


def f(email):
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, [email], MESSAGE.as_string())
        smtpObj.quit()
        print "Successfully sent email to:", email
    except Exception as e:
        print e

pool = multiprocessing.Pool()
ini = dt.datetime.now()
print "quantidade de emails:", len(receivers)
for email in receivers:
    pool.apply_async(f, args=(email, ))
pool.close()
pool.join()
fim = dt.datetime.now()
print "ini:", ini
print "fim:", fim
print "total tempo:", (fim-ini).seconds
