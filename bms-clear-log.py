#!/usr/bin/env python2.7
# clear log and send the log data to your email
# crontab command
# run the python script every 2 hours at exactly n:01 Local Time (n = even number)
# 1 */2 * * * $(which python) /path/to/file/bms-clear-log.py
import smtplib
import time
import os

TO = ['sample1@gmail.com']
GMAIL_USER = 'sample@gmail.com'
GMAIL_PASS = 'sample'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def get_current_time():
    localtime = time.asctime( time.localtime(time.time()) )
    return localtime

def send_email():
    log = f.read()
    SUBJECT = get_current_time() + ' - BMS Log'
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + (',').join(TO) + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    msg = header + '\n' + log + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    # print "Mail sent"

def clear_log():
    if os.path.exists("/path/to/file/bms-cron.log"):
        os.remove("/path/to/file/bms-cron.log")
    # else:
        # print('File does not exist')

try:
    f = open("/path/to/file/bms-cron.log", "r")
    send_email()
    clear_log()
except:
    print("An exception occurred")