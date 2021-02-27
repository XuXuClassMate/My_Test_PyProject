import requests
import pytest


class Test_demo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print("json:" + r.text)
        print(r.json())
        print("request:" + str(r.request))
        print("cookies:" + str(r.cookies))
        print(r.headers)
        pytest.assume(r.status_code == 200)


class Api:
    env = {
        "default": "dev",
        "testing-studio": {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }
    }

    def test_api(self, data: dict):
        data["url"] = (data["url"]).replace("testing-studio", self.env["testing-studio"][self.env["default"]])  # env[]
