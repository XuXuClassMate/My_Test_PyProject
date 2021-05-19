from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


# env FLASK_APP=flask_app flask run 运行接口
# env FLASK_ENV=development FLASK_APP=flask_app flask run 开发模式运行接口

# -----------------------#####-----------------------

# 创建路由
@app.route("/login", methods=['get', 'post'])
def login():
    res = {
        "method": request.method,
        "url": request.path,
        "args": request.args  # 参数
    }
    return res
