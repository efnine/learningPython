from datetime import datetime
from threading import Timer
"""
This will execute a function (eg. hello_world) in the next day at 1a.m.
"""
print("Starting CRON Job...")
x=datetime.today()
y=x.replace(day=x.day, hour=20, minute=27, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print("hello world")
    print(x)

t = Timer(secs, hello_world)
t.start()