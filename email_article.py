import smtplib
from datetime import datetime

from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour = 3, minute = 30, second = 30, microsecond = 0)
delta_t=y-x

secs=delta_t.seconds+1

def email():



t = Timer(secs, hello_world)
t.start()