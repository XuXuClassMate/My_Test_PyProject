# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-04 08:07
IDE: PyCharm
Introduction:#
FastHttpUser使用gevent协程发送网络请求，快5-6倍
启用并发的速度快
#-----------####---------
如需按顺序执行，MyTask继承SequentialTaskSet类即可
"""
# 搞起来
from locust import task, TaskSet, constant, SequentialTaskSet
from locust.contrib.fasthttp import FastHttpUser


class MyTask(TaskSet):
    @task
    def get_fun(self):
        with self.client.request(method = 'GET', path = 'url') as res:
            print("响应文本", res.text)

    @task
    def post_fun(self):
        json = {}
        with self.client.request(mothod = 'POST', path = 'url', json = json) as res:
            print("响应文本", res.text)


# FastHttpUser使用gevent协程发送，比HttpUser快5-6倍
# 启用并发的速度快
class FastUser(FastHttpUser):
    tasks = [MyTask]
    wait_time = constant(0.5)
