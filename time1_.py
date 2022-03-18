import datetime
from datetime import datetime as dt
import threading
import ms
import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
import random
import pachong
import time

#爬虫初始化
def get_all_this_page(url):
    headers = {'User-Agent':FakeUserAgent().random}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    return soup
def func():
    #每日更新文章的首页地址,设置show=500不用翻页
    url = 'https://arxiv.org/list/cs.CV/19?skip=0&show=5'
    spider = pachong.pc(url)
    #获取该页面文章数量
    ta = '#dlpage > dl > dd > div > div.list-title.mathjax'
    ta_ = spider.soup.select(ta)
    #连接数据库
    database = ms.Database()
    for i in ta_:
        #减少访问频率
        time.sleep(random.random()*3)
        date_url = spider.get_address(i)
        val = (i+220000,spider.get_arxiv(i),spider.get_title(i),spider.get_authors(i),spider.get_date(date_url,i),spider.get_subject(i),spider.get_pdf(i))
        database.add_data(val)
    print("今日论文爬取完成")
    timer = threading.Timer(86400,func)
    timer.start()

now_time = dt.now()
#调试时将1更改为了0，记得改回去
next_time = now_time + datetime.timedelta(days=+0)
next_year = next_time.date().year
next_month = next_time.date().month
next_day = next_time.date().day
#arXiv更新时间大概为每日早上10点
next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 18:33:00", "%Y-%m-%d %H:%M:%S")
timer_start_time = (next_time - now_time).total_seconds()
#print(timer_start_time)
timer = threading.Timer(timer_start_time,func)
print('hh')
timer.start()
print('hh')