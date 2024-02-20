from locust import HttpUser, task,between

class HelloWorldUser(HttpUser):
    wait_time = between(5, 15)
    def on_start(self):
        self.client.verify = False
        self.client.cookies = self.client.post("/login", {"userName": "admin", "userPassword": "dolphinscheduler123"},
                                              name="login").cookies

    @task
    def GetUserInfo(self):
        self.client.get("/users/get-user-info",name="get user info")


    @task
    def DefineUserCount(self):
        self.client.get("/projects/analysis/define-user-count?projectCode=0",name="define-user-count")
