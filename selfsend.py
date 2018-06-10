#!/usr/local/bin/python3

import smtplib

def sendemail(address, subject, classname,
              login="is.testingscripts@gmail.com",
              password="Lower05!",
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % login
    header += 'To: %s\n' % address
    header += 'Subject: %s\n\n' % subject
    message = header + str(classname)
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    server.sendmail(login, address, message)
    server.quit()

if __name__ == '__main__':
    sendemail("wc73@yahoo.com", "test", "body")
