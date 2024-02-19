# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_PTBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/19 11:00
from locust import HttpUser
from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
class Test_PTBase:
    def setup_class(self):
        self.pt = PTBase()
    def test__login(self):
        print(self.pt._login())

    def test_on_start(self):
        assert True

    def test_on_stop(self):
        assert True

    def test_get(self):
        assert True

    def test_get_now_time(self):
        print(self.pt.getNowTime())
        print("today_midnight")
        print(self.pt.getNowTime()["today_midnight"])
        print("now_time")
        print(self.pt.getNowTime()["now_time"])


    def test_get_user_name(self):
        print(self.pt.getUserName())

    def test_get_pass_word(self):
        print(self.pt.getPassWord())

    def test_get_base_url(self):
        print(self.pt.getBaseUrl())
