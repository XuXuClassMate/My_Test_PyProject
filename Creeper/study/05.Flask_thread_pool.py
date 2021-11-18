import time
import flask
import json
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
# 对ThreadPoolExecutor进行全局初始化
pool = ThreadPoolExecutor()


# 使用线程池针对web服务优化

def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


'''
优化前：
@app.route("/")
def index():
    result_file = read_file()
    result_db = read_db()
    result_api = read_api()
    return json.dumps({
        "result_file": result_file,
        "result_db": result_db,
        "result_api": result_api
    })
'''


# 优化后,三个线程并发运行
@app.route("/")
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result()
    })


if __name__ == '__main__':
    app.run()
