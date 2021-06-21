# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-20 14:58
IDE: PyCharm
Introduction:
"""
import base64
import random
import time

from flask import Flask, request

app = Flask(__name__)

users = {
    "magigo": ["123456"]
    }


def gen_token(uid):
    token = base64.b64encode(':'.json([str(uid), str(random.random()), str(time.time() + 7200)]))
    users[uid].append(token)
    return token


def verify_token(token):
    # base64的解密
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/index', methods = ['POST', 'GET'])
def index():
    print(request.headers)
    return 'Hello'


@app.route('/login', methods = ['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return "need auth"


@app.route('/test', methods = ['POST', 'GET'])
def tes123():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'


if __name__ == '__main__':
    app.run(debug = True)
