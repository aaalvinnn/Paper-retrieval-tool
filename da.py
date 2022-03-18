import requests
from bs4 import BeautifulSoup
import random
from requests.adapters import HTTPAdapter
import os
from urllib.request import urlretrieve
from sqlite3 import connect
import time

#爬虫初始化
def pc(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    return soup
#写入文件函数
def download_pdf(pdf_url,i,arxiv,nums):
    urlretrieve(pdf_url,fr'/usr/local/tomcat/tomcat9/webapps/papers/{arxiv}.pdf')
    #urlretrieve(pdf_url,fr'C:\Users\28692\Desktop\test\{arxiv}.pdf')
    print(f'第{i+nums}篇论文下载成功')
#8是论文首页页码数
nums = 492
for j in range(0,8):
    page = 2000*j
    url = f'https://arxiv.org/list/cs.CV/20?skip={page+nums}&show=2000'
    soup = pc(url)
    #论文序号
    number_all ='#dlpage > dl > dt > span > a:nth-child(1)'
    number_all_ = soup.select(number_all)
    for i in range(0,len(number_all_)):
        time.sleep(random.random()*3)
        #pdf论文下载地址
        pdf_content = '#dlpage > dl > dt > span > a:nth-child(2)'
        pdf_content_all = soup.select(pdf_content)
        arxiv = number_all_[i].text[6:]
        pdf_url = r'https://arxiv.org' + pdf_content_all[i].get('href')
        #判断文件夹中是否已经存在该文件
        if(os.path.exists(fr'/usr/local/tomcat/tomcat9/webapps/papers/{arxiv}.pdf')):
            print(f"第{i+1}篇文章已在文件夹中")
            continue
        else:
            download_pdf(pdf_url,i,arxiv,nums)