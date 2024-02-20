# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_Home.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/19 17:36
from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
from DolphinTest.DolphinPTTest.src.page.Home import Home
from locust import HttpUser, task, between
class HomeUserBehavior(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        ptbase =  PTBase(self.client)
        ptbase.on_start()

    @task
    def test_home(self):
        home =  Home(self.client)
        home.TaskStateCount()

