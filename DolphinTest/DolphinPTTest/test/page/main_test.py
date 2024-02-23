# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : main_test.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/22 21:08

from locust import TaskSet, task, between, HttpUser
from DolphinTest.DolphinPTTest.test.page.test_User import UserBehaviorTest
from DolphinTest.DolphinPTTest.test.page.test_Home import HomeBehaviorTest

class TestUserBehavior(TaskSet):
    tasks = {UserBehaviorTest:1, HomeBehaviorTest:1}

    @task
    def _task(self):
        pass

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [TestUserBehavior]