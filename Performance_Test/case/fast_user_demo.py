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
import csv
import math
import queue
import pymysql
from locust import task, TaskSet, constant, SequentialTaskSet, HttpUser, between, LoadTestShape
from locust.contrib.fasthttp import FastHttpUser


class MyTask(TaskSet):
    @task
    def get_fun(self):
        with self.client.request(method = 'GET', path = 'url') as res:
            print("响应文本", res.text)

    @task
    def post_fun(self):
        # 3、获取到消息队列，获取一条数据
        data = self.user.queueData.get()
        print("数据是：", data)
        with self.client.request(mothod = 'POST', path = 'url', json = data) as res:
            print("响应文本", res.text)

        # 如果需要循环使用消息队列的数据，只需吧该数据再次添加到消息队列即可
        self.user.queueData.put_nowait(data)


# 数据参数化
class MyLogInTask(TaskSet):
    # 获取数据库中的数据
    def GetSqlData(self):
        # 获取数据库连接对象
        conn = pymysql.connect(host = "127.0.0.1", database = "shop", user = "admin", password = "root")
        cursor = conn.cursor()  # 获取游标对象
        sql = 'select username,password from user;'
        cursor.execute(sql)  # 执行sql语句
        result = cursor.fetchall()  # 获取查询的所有结果
        cursor.close()  # 关闭游标
        conn.commit()  # 提交
        conn.close()  # 关闭数据库连接
        return result

    # 每个人执行任务的时候，查一次数据库
    def on_start(self):
        # 使用类属性self.DataList记录所有的用户名和密码
        self.DataList = self.GetSqlData()

    @task
    def LogIn(self):
        for data in self.DataList:
            d = {'username': data[0], 'password': data[1]}
            self.client.post(url = '/shop/mlogin', data = d)


class MyLogInTask2(TaskSet):
    # 获取csv中的数据
    def GetCsvData(self):
        f = open(file = './**.csv', mode = 'r', encoding = 'utf-8-sig')
        result = csv.reader()
        return result

    def on_start(self):
        self.datalist = self.GetCsvData()

    @task
    def login(self):
        for data in self.datalist:
            d = {'username': data[0], 'password': data[1]}
            self.client.post(url = '/shop/mlogin', data = d)


class MyUser(HttpUser):
    # 1、获取消息队列的对象
    queueData = queue.Queue()
    # 2、把数据放在消息队列中
    for i in range(100):
        data = {'name': 'zhangsan' + str(i), 'pwd': 'abc' + str(i)}
        # data数据添加到消息队列中
        queueData.put_nowait(data)
    tasks = [MyTask, MyLogInTask, MyLogInTask2]
    wait_time = between(0, 0.5)


# 自定义负载测试
# 参考locust git地址：https://github.com/locustio/locust/tree/master/examples/custom_shape
class DoubleWave(LoadTestShape):
    """
    A shape to immitate some specific user behaviour. In this example, midday
    and evening meal times. First peak of users appear at time_limit/3 and
    second peak appears at 2*time_limit/3
    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit  600/s -- total length of test
    """

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                    (self.peak_one_users - self.min_users)
                    * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                    + (self.peak_two_users - self.min_users)
                    * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                    + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None


# FastHttpUser使用gevent协程发送，比HttpUser快5-6倍
# 启用并发的速度快
class FastUser(FastHttpUser):
    tasks = [MyTask]
    wait_time = constant(0.5)
