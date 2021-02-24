import pytest
import requests


class Test_wuwork_api:
    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2ef8a1f13d444dfd&corpsecret=0FzKHtapsva" \
              "-Uyk8WCURTXE3sXhq6zGsFCg6Yx0BGlU"
        r = requests.get(url)
        res = r.json()
        pytest.assume(res["errcode"] == 0
        pytest.assume(res["access_token"] is not None)
        return res["access_token"]

    data = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "+86 13800000002",
        "department": [1]
    }

    def test_add_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}"
        r = requests.post(url, json=self.data)
        res = r.json()
        pytest.assume(res['errmsg'] == "created")

    def test_update_muber(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}"
        update_data = {
            "userid": f"{self.data['userid']}",
            "name": "李四", }
        r = requests.post(url, json=update_data)
        res = r.json()
        pytest.assume(res['errmsg'] == "updated")

    def test_delete_muber(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.test_get_token()}&userid={self.data['userid']}"
        r = requests.get(url)
        res = r.json()
        pytest.assume(res['errmsg'] == "deleted")

    if __name__ == '__main__':
        pytest.main(['-vs', 'test_wuwork_api.py'])
