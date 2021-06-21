# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-20 20:00
IDE: PyCharm
Introduction:
"""
from terrace.backend.src.testcase.TestCase_File import db


def test_create_filedb():
    # file类型表创建
    db.create_all()
