# import requests
# from bs4 import BeautifulSoup
# headers = {
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate, sdch",
# "Accept-Language": "zh-CN,zh;q=0.8",
# "Connection": "close",
# "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
# "Referer": "http://httpbin.org/",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
# }
# link = 'http://www.baidu.com/'
# # 爬取整个网页源码
# r = requests.get(link,headers = headers)
# ret = r.text
#
# # 解析网页源码
# soup = BeautifulSoup(ret,'lxml')
# # print(soup.text)
# # 爬取想要的内容
# ab = soup.find('div',class_="s-top-left s-isindex-wrap")
# print(ab.text)






# # 新建一个title.txt文本，把爬取的内容添加到这个文本
# with open('title.txt','a') as f:
#     f.write(title.text)
#
##查看文件保存路径
# import os
# print(os.path.abspath("."))

# 定制requests 把字典内容添加到url当中
# import requests
# dict1 = {'key1':'value1','key2':'value2'}
# r = requests.get('http://www.baidu.com',params=dict1)
# print(r.url)

# 定制请求头
# get方式
# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# r = requests.get('http://www.baidu.com',headers=headers)
# print(r.status_code)

import requests
from bs4 import BeautifulSoup
headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8",
"Connection": "close",
"Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
"Referer": "http://httpbin.org/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
link = 'http://www.baidu.com/'

r = requests.get(link,headers = headers)

soup = BeautifulSoup(r.text,'lxml')
# print(soup.text)

ab = soup.find('div',class_="s-top-left s-isindex-wrap")
print(ab.text)

# for ac in ab:
#     ac.find('a',class_="mnav c-font-normal c-color-t")
#     print(ac.text)



