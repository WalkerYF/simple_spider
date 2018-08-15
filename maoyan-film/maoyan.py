import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield item

def main():
    url = "https://maoyan.com/board/4"
    html = get_one_page(url)
    return html


if __name__ == '__main__':
    html = main()
    print(html)
    for i in parse_one_page(html):
        print(i)

