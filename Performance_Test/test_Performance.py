from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://www.baidu.com/"

    @task(1)
    def hello_world(self):
        self.client.get("/", name="访问百度首页")

    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         res = self.client.get(f"/item?id={item_id}", name="/item")
    #         print(res.text)
    # 
    # # on_start == setup
    # def on_start(self):
    #     self.client.post("/login", json={"username": "foo", "password": "bar"})

    # on_stop == teardown
    # def on_stop(self):
    #     self.client.post("/login", json={"username": "foo", "password": "bar"})
