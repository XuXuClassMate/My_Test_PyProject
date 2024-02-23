# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_User.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/21 12:10

from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
from DolphinTest.DolphinPTTest.src.page.User import User
from locust import HttpUser, task, between


class UserBehaviorTest(HttpUser):
    wait_time = between(1, 2)

    def __init__(self, client):
        super().__init__(client)
        self.ptbase = None
        self.user = None

    def on_start(self):
        self.ptbase = PTBase(self.client)
        self.ptbase.on_start()
        self.user = User(self.client)

    @task
    def test_get_user_info(self):
        self.user.GetUserInfo()

    @task
    def test_get_user_list(self):
        self.user.GetUserList()

    @task
    def test_update_user(self):
        self.user.UpdateUser()
