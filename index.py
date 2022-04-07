import os,sys
from pathlib import Path

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
try:
####################################################################################
    send_from = "we test lwaaz"
    send_to = ""
    subject = "hahahaha"
    body = "This is body of email"
    username = ""
    password = ""
    # attachmentPath = "/Users/dd/Desktop/rough.txt"
    ####################################################################################

    msg = MIMEMultipart()

    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    server = "smtp.gmail.com"
    port = 587
    use_tls = True

    msg.attach(MIMEText(body))

    # msg.attach(MIMEText(emailBody ,'html'))

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

    print("Message Sent")
except Exception as err:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(str([exc_type,fname,exc_tb.tb_lineno,err]))