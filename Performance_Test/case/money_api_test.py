from locust import HttpUser, TaskSet, task, between


def setup():
    print("接口性能测试初始化")


def teardown():
    print("接口性能测试完成")


class MyTest(HttpUser):
    wait_time = between(1, 1)

    def on_start(self):
        print("接口性能测试运行开始")

    @task(2)
    def get_studentinfo(self):
        url = 'http://api.nnzhp.cn/api/user/stu_info'
        params = {'stu_name': '小黑'}
        with self.client.get(url=url, data=params, timeout=10, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')
                print("获取学生信息接口")

    @task(1)
    def post_login(self):
        url = 'http://api.nnzhp.cn/api/user/login'
        params = {'username': 'niuhanyang', 'passwd': 'aA123456'}
        with self.client.post(url=url, data=params, timeout=10, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')
                print("登录接口")

    def on_stop(self):
        print("接口性能测试运行结束")
