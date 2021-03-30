from locust import HttpUser, task, between
from datetime import datetime


class wuwork_login_and_get_list(HttpUser):
    wait_time = between(1, 2)
    host = "https://qyapi.weixin.qq.com/"

    def on_start(self):
        url = "cgi-bin/gettoken?corpid=ww2ef8a1f13d444dfd&corpsecret=0FzKHtapsva" \
              "-Uyk8WCURTXE3sXhq6zGsFCg6Yx0BGlU"
        r = self.client.get(url, name="token获取").json()
        self.token = r["access_token"]
        if r["errcode"] == 0:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2] + "token获取正确")
        else:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2] + "token获取失败：" + r)

    @task
    def get_member(self, userid="1008611"):
        url = f"cgi-bin/user/get?access_token={self.token}&userid={userid}"
        res = self.client.get(url, name="接口查询").json()
        if res["errcode"] == 0:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2] + "查询验证正确")
        else:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2] + "查询验证错误：" + res)
