# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : ds_api.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2023/12/9 16:49
from locust import TaskSet, task, HttpUser, between

base_url = "http://8.130.66.9:12345/dolphinscheduler"


class DS_Api_Test(TaskSet):
    # 编写任务函数：普通函数加上@task注解
    # 可多任务
    @task
    def get_calendar_list(self):
        # 访问首页 --基于requests的网络请求(熟悉使用requests发送请求) --self.client 网络请求的客户端，session cookie可以自动保存
        with self.client.get(url='/calendar?pageNo=1&pageSize=10&searchVal=', name="获取日历列表") as res:
            print("耗时", res.elapsed.total_seconds())
            print("响应状态码", res.status_code)
            print("响应文本：", res.text)
            print("json:", res.json())
            if "true" in res.text:
                res.success()
            else:
                res.failure("this's  request fail")

    @task
    def get_projects_list(self):
        with self.client.get(url='/projects?pageSize=10&pageNo=1&searchVal=', name="获取项目列表") as res:
            print("耗时", res.elapsed.total_seconds())
            print("响应状态码", res.status_code)
            print("响应文本：", res.text)
            print("json:", res.json())
            if "true" in res.text:
                res.success()
            else:
                res.failure("this's  request fail")


class V_user(HttpUser):
    # 使用task属性 指定用户完成的任务
    weight = 1  # 权重
    tasks = [DS_Api_Test]
    # wait_time等待时间---各任务之间的时间间隔
    wait_time = between(0, 1)  # 每个任务间隔0-1秒（单位是秒）
    # wait_time = constant(0.5)   # 固定等待时间为0.5秒


class Web_user(HttpUser):
    task = [DS_Api_Test]
    wait_time = between(0, 0.5)


class Mobile_user(HttpUser):
    task = [DS_Api_Test]
    wait_time = between(0, 0.5)


'''
locust基本运行---locust -f base_demo.py -H url
不启动界面 --- locust -f base_demo.py --headless -u 用户数量 -r 每秒启动的用户数 -H url -t 运行时间
--csv 结果文件
'''
