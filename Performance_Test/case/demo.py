# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-03 17:39
IDE: PyCharm
Introduction:
"""

from locust import between, TaskSet, task, HttpUser, constant


# 1、编写任务类


class MyTask(TaskSet):
    # 编写任务函数：普通函数加上@task注解
    @task(1)
    def index(self):
        # 访问首页 --基于requests的网络请求(熟悉使用requests发送请求) --self.client 网络请求的客户端，sessionhe cookie可以自动保存
        with self.client.get(url = 'xpath', name="newname") as res:
            print("响应状态码", res.status_code)
            print("响应文本：", res.text)
            print("json:", res.json())


# 可多任务

class Vuser(HttpUser):
    # 使用task属性 指定用户完成的任务
    weight = 1  # 权重
    tasks = [MyTask]
    # wait_time等待时间---各任务之间的时间间隔
    wait_time = between(0, 1)  # 每个任务间隔0-1秒（单位是秒）
    # wait_time = constant(0.5)   # 固定等待时间为0.5秒


class Webuser(HttpUser):
    task = [MyTask]
    wait_time = between(0, 0.5)


class Mobile(HttpUser):
    task = [MyTask]
    wait_time = between(0, 0.5)


'''
locust基本运行---locust -f demo.py -H url
'''
