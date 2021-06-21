# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-20 19:52
IDE: PyCharm
Introduction:
"""
from terrace.backend.src.testcase.TestCase_Text import db


def test_create_db():
    # text文本数据库创建
    db.create_all()




