# from urllib import request
# url ='http://www.weather.com.cn/weather1d/101210101.shtml#input'
# response = request.urlopen(url,timeout=1)
# print(response.read().decode('utf-8'))


# from urllib import parse
# from urllib import request
#
# data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
# # print(data)
#
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))
#
#
# response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response2.read())


# response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)

# import urllib
# import socket
#
# try:
#     response3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
#
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
#
# dict = {
# 'name': 'value'
# }
#
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))






# # get请求
# import requests
# url = 'http://httpbin.org/get'
# data = {'key': 'value', 'abc': 'xyz'}
# # .get是使用get方式请求url，字典类型的data不用进行额外处理
# response = requests.get(url,data)
# print(response.text)

# # post请求
# import requests
# url = 'http://httpbin.org/post'
# data = {'key': 'value', 'abc': 'xyz'}
# # .post表示为post方法
# response = requests.post(url,data)
# # 返回类型为json格式
# print(response.json())

# import requests
# import re
# content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
#
# # print(content)
#
#
# # < div class ="grid-item work-thumbnail" >
# # < a href="(.*?)".*?title">(.*?)</div>
# # < div class ="author" > LynnWei < / div >
#
# pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
# results = re.findall(pattern, content)
# # print(results)
#
# for result in results:
#     url, name = result
#     print(url, re.sub('\s', '', name))






'''
beautiful soup的安装和使用
'''

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html_doc, 'lxml')
#
# print(soup.prettify())










#
# # 找到title标签
# print(soup.title)
#
# # title 标签里的内容
# print(soup.title.string)


# # 找到p标签
# print(soup.p)
#
# # 找到p标签class的名字
# print(soup.p['class'])
#
# # 找到第一个a标签
# print(soup.a)
#
# # 找到所有的a标签
# print(soup.find_all('a'))
#
#
# # 找到id为link3的的标签
# print(soup.find(id="link3"))
#
# # 找到所有<a>标签的链接
# for link in soup.find_all('a'):
#     print(link.get('href'))
#
# # 找到文档中所有的文本内容
# print(soup.get_text())