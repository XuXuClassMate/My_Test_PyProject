import requests
from bs4 import BeautifulSoup

from test_API.testing.Logfile import LogFile

log = LogFile()
urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]


# print(urls)

# 普通的爬虫程序
def craw(url):
    res = requests.get(url)
    # print(url, len(res.text))
    log.echolog(f"{urls},len: {len(res.text)}")
    return res.text


def parse(html):
    # class ="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]
    pass


if __name__ == '__main__':
    for result in parse(craw(urls[0])):
        log.echolog(str(result))
        print(result)
