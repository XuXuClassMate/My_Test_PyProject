# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-20 19:52
IDE: PyCharm
Introduction:
"""
import requests

from terrace.backend.src.testcase.TestCase_Text import db


def test_create_testcase_db():
    # text文本数据库创建
    db.create_all()


def test_execution():
    with requests.post('http://127.0.0.1:5000/execution', json = {
        'testcase_id': 1
        }
            ) as res:
        assert res.status_code == 200

