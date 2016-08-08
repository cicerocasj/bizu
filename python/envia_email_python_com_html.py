# -*- coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
password = 'XXXXXXXXXX'


try:
    sender = 'cicerocasj@gmail.com'
    receivers = [sender]
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

    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.starttls()
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receivers, MESSAGE.as_string())
    smtpObj.quit()
    print "Successfully sent email"
except smtplib.SMTPException,error:
    print str(error)
    print "Error: unable to send email"