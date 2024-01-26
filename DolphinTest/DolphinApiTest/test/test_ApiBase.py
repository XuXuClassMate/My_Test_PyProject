# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_ApiBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/24 15:10
from DolphinTest.DolphinApiTest.src.base.ApiBase import ApiBase


class TestApiBase:

    def setup_class(self):
        self.apibase = ApiBase()

    def test_getSession(self):
        result = self.apibase.getSession()
        print(result)

