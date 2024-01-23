# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Base.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/21 17:46
import requests

from DolphinTest.logs.LogFile import LogFile
from DolphinTest.dolphinConfig import DolphinConfig

log = LogFile()


class Base:

    def __init__(self):
        self.config = DolphinConfig()
        self.username = self.config.userName
        self.password = self.config.passWord
        self.base_url = self.config.baseUrl
        self.headers: dict = {
            'Language': 'zh_CN',
            'Accept': 'application/json, text/plain, */*',
            'Sessionid': self.get_session()
        }

    def get_session(self, SessionId=None):
        if SessionId is None:
            request = requests.post(self.base_url + "/login",
                                    data={"userName": self.username, "userPassword": self.password})
            if request.status_code == 200:
                SessionId = request.json()['data']['sessionId']
                return SessionId
            else:
                print("get session error")
        else:
            return SessionId

    def get(self, url: str, **kwargs):
        response = requests.get(url=self.base_url + url, headers=self.headers, **kwargs).json()
        log.echolog("get request：" + str(url) + ", params：" + str(**kwargs))
        log.echolog("get response：" + str(response))
        return response

    def post(self, url: str, **kwargs):
        response = requests.post(url=self.base_url + url, headers=self.headers, **kwargs).json()
        log.echolog("post request：" + str(url) + ", data：" + str(**kwargs))
        log.echolog("post response：" + str(response))
        return response

    def put(self, url: str, **kwargs):
        response = requests.put(url=self.base_url + url, headers=self.headers, **kwargs).json()
        log.echolog("put request：" + str(url) + ", data：" + str(**kwargs))
        log.echolog("put response：" + str(response))
        return response

    def delete(self, url: str, **kwargs):
        response = requests.delete(url=self.base_url + url, headers=self.headers, **kwargs).json()
        log.echolog("delete request：" + str(url) + ", data：" + str(**kwargs))
        log.echolog("delete response：" + str(response))
        return response
