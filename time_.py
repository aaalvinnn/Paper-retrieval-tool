import datetime
from datetime import datetime as dt
import threading

def func():
    print("haha")
    timer = threading.Timer(86400,func)
    timer.start()

now_time = dt.now()
next_time = now_time + datetime.timedelta(days=+0)
next_year = next_time.date().year
next_month = next_time.date().month
next_day = next_time.date().day
#arXiv更新时间大概为每日早上10点
next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 10:00:00", "%Y-%m-%d %H:%M:%S")
timer_start_time = (next_time - now_time).total_seconds()
#print(timer_start_time)
timer = threading.Timer(timer_start_time,func)
timer.start()

