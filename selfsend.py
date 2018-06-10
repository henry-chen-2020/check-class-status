#!/usr/local/bin/python3

import smtplib
from email.message import EmailMessage

def sendemail(address, subject, classname,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % login
    header += 'To: %s\n' % address
    header += 'Subject: %s\n\n' % subject
    message = header + str(classname)
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(address, login, message)
    server.quit()
    return problems
