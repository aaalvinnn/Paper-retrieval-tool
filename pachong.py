
import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
import random
from requests.adapters import HTTPAdapter
import os
from urllib.request import urlretrieve
from sqlite3 import connect



class pc(object):
    #初始化
    def __init__(self,url):
        headers = {'User-Agent':FakeUserAgent().random}
        proxies = {
                'http': 'http://{}'.format('118.190.151.7:3'),
                'https': 'https://{}'.format('118.190.151.7:3'),            
            }
        response = requests.get(url=url,headers=headers)
        html = response.text
        self.soup = BeautifulSoup(html, 'lxml')
    #获取该页面某链接soup
    def get_soup(self,url):
        headers = {'User-Agent':FakeUserAgent().random}
        response = requests.get(url=url,headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        return soup
    #获取arxiv号
    def get_arxiv(self,i):
        arxiv_all ='#dlpage > dl > dt > span > a:nth-child(1)'
        arxiv_all_ = self.soup.select(arxiv_all)
        return (arxiv_all_[i].text[6:]).strip()
    #获取标题
    def get_title(self,i):
        title_all = '#dlpage > dl > dd > div > div.list-title.mathjax'
        title_all_ = self.soup.select(title_all)
        return (title_all_[i].text[7:]).strip()
    #获取作者
    def get_authors(self,i):
        authors_all ='#dlpage > dl > dd > div > div.list-authors'
        authors_all_ = self.soup.select(authors_all)
        return ((authors_all_[i].text[9:]).strip()).replace('\n','')
    #获取类别
    def get_subject(self,i):
        subject_all = '#dlpage > dl > dd > div > div.list-subjects'
        subject_all_ = self.soup.select(subject_all)
        return (subject_all_[i].text[10:]).strip()
    #获取论文地址
    def get_address(self,i):
        address_content = '#dlpage > dl > dt > span > a:nth-child(1)'
        address_content_all = self.soup.select(address_content)
        address = address_content_all[i].get('href')
        address = 'https://arxiv.org' + address
        return address
    #获取日期
    def get_date(self,url,i):
        paper_date_content = '#abs > div.dateline'
        headers = {'User-Agent':FakeUserAgent().random}
        response = requests.get(url=url,headers=headers)
        html = response.text
        soup_paper = BeautifulSoup(html, 'lxml')
        paper_date_content_ = soup_paper.select(paper_date_content)
        date = paper_date_content_[i].text
        #处理日期字符串
        flag1 = 0
        flag2 = 0
        for j in range(0,len(date)):
            if date[j] == 'n' and date[j-1] == 'o':
                flag1 = j+2
            if date[j] == ']' or date[j] == '(':
                flag2 = j
                break
        date = date[flag1:flag2]
        return date
    #获取pdf下载地址
    def get_pdf(self,i):
        pdf_content = '#dlpage > dl > dt > span > a:nth-child(2)'
        pdf_content_all = self.soup.select(pdf_content)
        pdf_address = r'https://arxiv.org' + pdf_content_all[i].get('href')
        return pdf_address

url = r'https://arxiv.org/list/cs.AI/pastweek?skip=0&show=500'
abc =pc(url)
a = abc.get_pdf(0)
print(a)


    
    