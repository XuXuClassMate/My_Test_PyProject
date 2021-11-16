import threading
import blog_spider
import time
from test_API.testing.Logfile import LogFile

log = LogFile()


# 普通的单线程爬虫
def single_thread():
    log.echolog("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    log.echolog("single_thread end")


def multi_thread():
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print(f"start time:{start}\n end time:{end}\n single thread cost:{end-start}seconds")
# 运行结果：
# starttime: 1637055125.735268
# endtime: 1637055165.641379
# singlethreadcost: 39.906111001968384seconds

    start = time.time()
    multi_thread()
    end = time.time()
    print(f"start time:{start}\n end time:{end}\n multi thread cost:{end - start}seconds")
# 运行结果：
# start time:1637055165.641442
#  end time:1637055178.166017
#  multi thread cost:12.524574995040894seconds

