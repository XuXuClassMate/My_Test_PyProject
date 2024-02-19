# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_Home.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/19 17:36
from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
from locust import HttpUser, task, between
class HomeUserBehavior(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.ptbase = None
    wait_time = between(1, 2)
    def on_start(self):
        self.ptbase = PTBase()
        self.ptbase.on_start()
    @task(1)
    def test_task_state_count(self):
        self.ptbase.TaskStateCount()

    @task(2)
    def test_task_state(self):
        self.ptbase.TaskStateCount()