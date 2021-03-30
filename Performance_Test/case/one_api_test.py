from locust import HttpUser, task, between


class MyTest(HttpUser):
    wait_time = between(1, 1)

    @task
    def get_studentinfo(self):
        url = 'http://api.nnzhp.cn/api/user/stu_info'
        params = {'stu_name': '小黑'}
        self.client.get(url=url, data=params, timeout=10)

    @task
    def post_login(self):
        url = 'http://api.nnzhp.cn/api/user/login'
        params = {'username': 'niuhanyang', 'passwd': 'aA123456'}
        self.client.post(url=url, data=params, timeout=10)
