import json
import math

import flask
from concurrent.futures import ProcessPoolExecutor

app = flask.Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqert_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqert_n + 1, 2):
        if n % 2 == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.splir(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == '__main__':
    # 多线程哪里定义都可以，多进程为了数据共享，需要再main函数中在run函数之前初始
    # 化ProcessPoolExecutor()函数，可以在上面的方法中使用这个函数完成数据共享
    process_pool = ProcessPoolExecutor()
    app.run()
