# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_ApiBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/24 15:10
from DolphinTest.DolphinApiTest.src.ApiBase import ApiBase



def test_getSession():
    apibase = ApiBase()
    result = apibase.getSession()
    print(result)

class TestMyClass:
    def test_addition(self):
        print(111)

    def test_subtraction(self):
        assert 3 - 1 == 2