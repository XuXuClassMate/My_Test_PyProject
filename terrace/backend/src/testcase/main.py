# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-15 18:20
IDE: PyCharm
Introduction:
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['AQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou5_yxp:ceshiren.com@stuq.ceshiren.com:23306/lagou5db' \
                                        '?charset' \
                                        '=utf8mb4'
db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # 测试名称 80个字符，不是唯一，不能为空
    name = db.Column(db.String(80), unique = False, nullable = False)
    # 用例为文本数据类型
    data = db.Column(db.String(1000), unique = False, unllable = False)
    # 备注 ，1000个字符，允许不唯一，允许为空
    remark = db.Column(db.String(1000), unique = False, nullable = True)

    def __repr__(self):
        return '<TestCase %r>' % self.name
