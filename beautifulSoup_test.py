import requests
from bs4 import BeautifulSoup

# from document https://www.crummy.com/software/BeautifulSoup/bs4/doc/

html_doc = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">    Elsie   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""
soup = BeautifulSoup(html_doc,'lxml')
print(soup.prettify())


# for link in soup.find_all('a'):
#     # the same as 
#     # print(link['href']) 
#     print(link.get('href'))

'''
1. tags
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#multi-valued-attributes
这里要稍微记一下,对部分标签返回列表,对其他标签返回字符串
2. navigableString
用string方法,表示标签内的内容
不可编辑,不过可使用replace_with方法替换
如果要在其他地方使用这个字符串,需要使用unicode()方法将其替换为正常字符串
不然,就会一直携带者对原html文件内容的引用
3. BeautifulSoup
4. Comment还有其他类似的类
'''

link = soup.body
# print(link)
# link = link.next_sibling
# print(link)
# link = link.next_sibling
# print(link)
# link = link.next_sibling
# print(link)
print(type(link.contents))
print(type(link.children))
print(type(link.descendants))
print(type(link.parents))
print(type(link.next_siblings))
print(type(link.next_elements))

# while link != None:
#     print(link)
#     print('-----------------------')
#     link = link.next_element