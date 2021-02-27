import requests


class Base:
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2ef8a1f13d444dfd&corpsecret=0FzKHtapsva" \
              "-Uyk8WCURTXE3sXhq6zGsFCg6Yx0BGlU"
        r = requests.get(url).json()
        self.token = r["access_token"]
        # 声明一个Session
        self.session = requests.Session()
        # 把token放入到SessionS中
        self.session.params = {"access_token": self.token}

    def send(self, *args, **kwargs):
        # 位置参数 关键字参数
        r = self.session.request(*args, **kwargs)
        return r.json()
