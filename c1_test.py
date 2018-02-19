from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 打开url
# 1. 网页或服务器不存在:HTTPError异常
# 调用BeautifulSoup对象里的标签不存在
# 1. 返回none对象

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

# 将可能发生的两种错误都放在一个函数中,通过返回值来确定

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)