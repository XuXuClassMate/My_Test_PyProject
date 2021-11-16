import requests
import threading
import time

print(f'{time.time()}')
res = requests.get(
    'https://www.baidu.com/s?tn=02003390_43_hao_pg&isource=infinity&iname=baidu&itype=web&ie=utf-8&wd=ceshi%20')
print(res.json())


# 准备一个函数
def my_func(a, b):
    do_craw(a, b)


# 创建一个线程
t = threading.Thread(target=my_func, args=(100, 200))
# 启动线程
t.start()
# 等待结束
t.join()
