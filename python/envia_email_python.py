# -*- coding:utf-8
import smtplib
password = 'XXXXXXXXX'

try:
    sender = 'cicerocasj@gmail.com'
    receivers = ['cicerocasj@gmail.com']
    subject = "Assunto do email"
    message = "Texto do email operação"

    message_text = """Subject: {assunto}\n{mensagem}""".format(assunto=subject, mensagem=message)
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.starttls()
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receivers, message_text)
    smtpObj.quit()
    print "Successfully sent email"
except smtplib.SMTPException,error:
    print str(error)
    print "Error: unable to send email"
