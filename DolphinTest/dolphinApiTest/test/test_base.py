# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_base.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/21 19:53
from DolphinTest.dolphinApiTest.src.base.Base import Base


def test_login():
    base = Base()
    # r = base.send("get", base.base_url+"/users/get-user-info")
    a = base.get(url="/users/get-user-info")
    print("get-user-info：")
    print(a)
    b = base.get(url="/users/get-user-info")
    print("get-user-info：")
    print(b)
    c = base.get(url="/users/get-user-info")
    print("get-user-info：")
    print(c)

