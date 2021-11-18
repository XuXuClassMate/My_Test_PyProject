import concurrent.futures
import blog_spider
from test_API.testing.Logfile import LogFile

log = LogFile()

# 线程池 方法一：pool.map()批量提交，按顺序返回

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")


# parse 方法二：pool.submit() 单个提交，按顺序返回，性能更强大。
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

# 两种返回方式：第一：按照顺序打印
    # for future, url in futures.items():
    #     # print(url, future.result())

# 第二：那个先执行完成那个先返回：推荐使用第二种性能更佳~~~
    # as_completed()函数无顺序执行
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())
