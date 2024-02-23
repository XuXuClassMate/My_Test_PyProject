# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_Home.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/19 17:36
from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
from DolphinTest.DolphinPTTest.src.page.Home import Home
from locust import HttpUser, task, between
class HomeBehaviorTest(HttpUser):
    wait_time = between(1, 2)

    def __init__(self,client):
        super().__init__(client)
        self.ptbase = None
        self.home = None

    def on_start(self):
        self.ptbase =  PTBase(self.client)
        self.ptbase.on_start()
        self.home = Home(self.client)

    def on_stop(self):
        self.ptbase.on_stop()
    @task(10)
    def test_TaskStateCount(self):
        self.home.TaskStateCount()


    @task(20)
    def test_DefineUserCount(self):
        self.home.DefineUserCount()

    @task(30)
    def test_ProcessStateCount(self):
        self.home.ProcessStateCount()


