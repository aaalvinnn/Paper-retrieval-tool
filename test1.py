import requests
from bs4 import BeautifulSoup


url = 'https://arxiv.org/list/cs.AI/recent'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')


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
#写入文件
f = open('papers.txt','w')
for i in range(0,len(title_all_)):
    f.write(f'paper-{i+1}\n')
    #l论文序号
    f.write(number_all_[i].text)
    #print(number_all_[i].text)    
    #论文标题
    f.write(title_all_[i].text)
    #print(title_all_[i].text)
    #论文作者
    f.write(authors_all_[i].text)
    #print(authors_all_[i].text)
    #论文类别
    f.write(subject_all_[i].text)
    #print(subject_all_[i].text)
    #论文日期
    response_paper = requests.get(address_list[i],headers=headers)
    html_paper = response_paper.text
    soup_paper = BeautifulSoup(html_paper,'lxml')
    paper_date_content = '#abs > div.dateline'
    paper_date_content_ = soup_paper.select(paper_date_content)
    date = strname_date(paper_date_content_[0].text)
    #print(date)
    f.write(date)
    f.write('\n\n\n')
f.close()




    


