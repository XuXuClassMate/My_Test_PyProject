import requests
import threading
import time

print(f'{time.time()}')
res = requests.get('https://www.baidu.com/s?tn=02003390_43_hao_pg&isource=infinity&iname=baidu&itype=web&ie=utf-8&wd=ceshi%20')
print(res.json())

t = threading.Thread()




