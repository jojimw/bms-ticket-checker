#!/usr/bin/env python2.7
# check ticket availability and sends email when tickets are available
# crontab command
# run the python script every 15 minutes
# */15 * * * * $(which python) /path/to/file/bms.py >> ~/path/to/file/bms-cron.log
import urllib2
from bs4 import BeautifulSoup
import re
import smtplib
import time

# site="https://in.bookmyshow.com/buytickets/lucifer-kochi/movie-koch-ET00019224-MT/"
# date="20190426"
# MOVIE = "Lucifer"
#Replace this with your movie and city url
site = "https://in.bookmyshow.com/buytickets/avengers-endgame-kochi/movie-koch-ET00100559-MT/"
date = "20190426" #replace the date with the date for which you'd like to book tickets! Format: YYYYMMDD
MOVIE = "Avengers: Endgame"
site = site + date
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# just replace it with your prefered show timing by inspecting data-display-showtime
# show='09:00 AM'
# venue_code can be found by inspecting the element data-id for the venue where you would like to watch
# pvr lulu = 'PVKC', gold souk = 'QCKC'
venue_code = 'QCKC'
# venue_code = 'PVKC'

#mail id for which you want to get alerted
TO = [
    'sample_email_1@email.com',
    'sample_email_2@email.com'
]
# Please add your username and password here, and make sure you 
# toggle allow less secure apps to on 
# https://myaccount.google.com/lesssecureapps?pli=1 
GMAIL_USER = 'sample@email.com'
GMAIL_PASS = 'sample'

def get_current_time():
    localtime = time.asctime( time.localtime(time.time()) )
    return "Time: " + localtime + "\n"

def get_venue(venue_code):
    venue = {
        'QCKC': 'Gold Souk',
        'PVKC': 'PVR Lulu Mall'
    }
    return venue.get(venue_code)

def send_email(show, venue_code):
    VENUE = get_venue(venue_code)
    TEXT = 'The tickets are now available for the ' + show + ' show of ' + MOVIE + ' at ' + VENUE
    SUBJECT = MOVIE + ': ' + show + ' - ' + VENUE + ', Book fast'
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + (',').join(TO) + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

def get_show_times():
    show_times = []
    for i in range(2):
        for j in range(13):
            for k in range(60):
                show_time = ("0" if j < 10 else "") + `j`+":" + ("0" if k < 10 else "") + `k`+" " + ("AM" if i == 0 else "PM")
                show_times.append(show_time)
    return show_times

def check_availabitity():
    available = False
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")
    soup2 = soup.find_all('div', {'data-online': 'Y'})
    line = str(soup2)
    soup3 = BeautifulSoup(line, features="html.parser")
    soup4 = soup3.find_all('a', {'data-venue-code': venue_code})
    line1 =str(soup4)
    soup5 = BeautifulSoup(line1, features="html.parser")
    show_times_array = get_show_times()
    for show in show_times_array:
        soup6 = soup5.find_all('a', {'data-display-showtime': show})
        line2 = str(soup6)
        result = re.findall('data-availability="A"', line2)
        if len(result) > 0:
            print get_current_time() + "Available"
            send_email(show, venue_code)
            available = True
    if not available: print get_current_time() + "Not available yet" + "\n"
    
check_availabitity()