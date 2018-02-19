from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html,"lxml")

# # 抽取只包含在<span class="green"></span> 标签里的文字
# nameList = bsObj.findAll("span", {"class":"green"})
# for name in nameList:
#     print(name.get_text())


# nameList = bsObj.findAll(text="the prince")
# for name in nameList:
#     print(name)


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())