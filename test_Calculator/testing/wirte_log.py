import time

print(time)


def time_log():
    time_log1 = time.strftime("%Y年-%m月-%d日  %H:%M:%S")


with open('/test_Calculator/testing/logs'
          f'/{time.strftime("%Y年-%m月-%d日")}/{time.strftime("")}.log', 'a') as log:
    log.write(f'-{time_log} 状态：{time_log}')
