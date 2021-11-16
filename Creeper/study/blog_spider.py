import requests

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]


# print(urls)

# 普通的爬虫程序
def craw(url):
    res = requests.get(url)
    print(url, len(res.text))


craw(urls[0])
