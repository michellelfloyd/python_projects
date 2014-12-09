import time
import datetime
f = open("dates.txt", "r")

for t in f:
    #datetime is function converting epoch second to date and time
    #time.time is now in epoch seconds(float)
    now = datetime.datetime.fromtimestamp(time.time())
    now_e = time.mktime(now.timetuple())
    diff = float(now_e) - float(t)
    past = datetime.date.fromtimestamp(float(t))
    sec_day = 86400
    day_ago = diff / sec_day
    pretty_ago = int(round(day_ago))
    print past, 'happened', pretty_ago, 'days ago.'

f.close()
