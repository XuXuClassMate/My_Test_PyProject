import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [1122334455667788] * 100


# 是一个CPU密集型计算:是否为素数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # 开根号
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# 普通单线程
def single_thread():
    for number in PRIMES:
        is_prime(number)


# 多线程运行
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


# 多进程运行
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread,cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread,cost:", end - start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process,cost:", end - start, "seconds")
