import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
import random
from requests.adapters import HTTPAdapter
import os
from urllib.request import urlretrieve
from sqlite3 import connect
import mysql.connector
#爬虫初始化
url = 'https://arxiv.org/list/cs.AI/pastweek?skip=0&show=1000'
headers = {'User-Agent':FakeUserAgent().random}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')
#连接数据库
config = {
    'user' : 'root',
    'password' : 'Zsw,20021216',
    'host' : 'localhost',
    'port' : '3306',
    'database' : 'Papers'
}
con = mysql.connector.connect(**config)
#创建游标
mycursor = con.cursor(buffered = True)
#检查表存在函数
def tableExists(mycursor, name):
    stmt = "SHOW TABLES LIKE '"+name+"'"
    mycursor.execute(stmt)
    return mycursor.fetchone()
#删除表函数
def dropTable(mycursor, name):
    stmt = "DROP TABLE IF EXISTS" +name
    mycursor.execute(stmt)
    
#增添整条数据
def add_data(mycursor,val):
    sql = 'INSERT INTO safe1(No,arXiv,title,authors,date,subjects) VALUES(%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql,val)
    con.commit()
#更改一条中某个字段的数据
def modify_data(mycursor,field,old_data,new_data):
    sql = f"UPDATE safe1 SET {field}='{new_data}' WHERE {field}= '{old_data}'"
    mycursor.execute(sql)
    con.commit()
#删除某条数据记录函数
def delete_data(mycursor,field,val):
    sql = f"DELETE FROM safe1 WHERE {field}= '{val}'"
    mycursor.execute(sql)
    con.commit()
#显示当前数据库信息
def search_all_data(mycursor):
    print('arXiv title authors date subjects')
    sql = 'SELECT * FROM safe1'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
#论文标题
title_all = '#dlpage > dl > dd > div > div.list-title.mathjax'
title_all_ = soup.select(title_all)
#论文序号
number_all ='#dlpage > dl > dt > span > a:nth-child(1)'
number_all_ = soup.select(number_all)
#论文作者
authors_all ='#dlpage > dl > dd > div > div.list-authors'
authors_all_ = soup.select(authors_all)
#论文类别
subject_all = '#dlpage > dl > dd > div > div.list-subjects'
subject_all_ = soup.select(subject_all)
#论文日期
 #获取论文地址
address_content = '#dlpage > dl > dt > span > a:nth-child(1)'
address_content_all = soup.select(address_content)
address_list=[]
for address in address_content_all:
    address = address.get('href')
    address = 'https://arxiv.org' + address
    address_list.append(address)
#pdf论文下载地址
pdf_content = '#dlpage > dl > dt > span > a:nth-child(2)'
pdf_content_all = soup.select(pdf_content)

#日期字符串截取函数
def strname_date(date_char):
    flag1 = 0
    flag2 = 0
    for j in range(0,len(date_char)):
        if date_char[j] == 'n':
            flag1 = j+2
        if date_char[j] == ']':
            flag2 = j
    date_char = date_char[flag1:flag2]
    return date_char
#写入文件函数
def download_pdf(pdf_url,i):
    urlretrieve(pdf_url,fr'C:\Users\28692\Desktop\2022春招\test\Artificial_Intelligence\{i+1}.pdf')
    print(f'第{i+1}篇论文下载成功')
#写入文件到数据库
# errors='ignore：遇到非法字符（即不是utf-8标准），则跳过
# with open('papers.txt','w',errors='ignore') as f:

for i in range(0,len(title_all_)):

    response_paper = requests.get(address_list[i],headers=headers)
    html_paper = response_paper.text
    soup_paper = BeautifulSoup(html_paper,'lxml')
    paper_date_content = '#abs > div.dateline'
    paper_date_content_ = soup_paper.select(paper_date_content)
    date = strname_date(paper_date_content_[0].text)
    #去掉各字符串的前缀部分
    val=(i+1,(number_all_[i].text[6:]).strip(),(title_all_[i].text[7:]).strip(),((authors_all_[i].text[9:]).strip()).replace('\n',''),date,(subject_all_[i].text[10:]).strip())
    #去掉列表中的空字符
    add_data(mycursor,val)
    print(f"第{i+1}篇论文保存成功")
    # #下载论文pdf格式
    # pdf_address = r'https://arxiv.org' + pdf_content_all[i].get('href')
    # download_pdf(pdf_address,i)
print('hello world')


