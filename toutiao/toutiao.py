from urllib.parse import urlencode

data = {
    'offset': 3,
    'keyword': 'test'
}

print(urlencode(data))

