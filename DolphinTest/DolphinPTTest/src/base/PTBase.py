# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : PTBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/18 15:44

import requests

from DolphinTest.DolphinConfig import DolphinConfig
from datetime import datetime


class PTBase(DolphinConfig):
    def __init__(self, client):
        super().__init__()
        self.client = client


    def _login(self):
        request = requests.post(self.getBaseUrl() + "/login",
                                data={"userName": self.getUserName(), "userPassword": self.getPassWord()})
        if request.status_code == 200:
            return request.cookies
        else:
            return None

    """
    on_start:
    Locust task set for testing the PT system
    Perform a login operation when starting the task set and get the cookie
    """

    def on_start(self):
        self.client.cookies = self._login()

    def on_stop(self):
        self.client.clear_cookies()
        self.client.close()

    """
    DELETE function 
    parameter： url, headers, params, auth, timeout, allow_redirects, proxies, 
                verify, cert, stream, hooks, cookies
    """
    def GET(self, url, **kwargs):
        with self.client.get(url=url, name=url, catch_response=True, **kwargs) as response:
            if response.json()["code"] != 0:
                response.failure("GET name = "+ str(url) + "Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("GET name = "+ str(url) + "Request took too long")


    """
    POST function 
    parameter： url, headers, params, data, json, files, auth, timeout, allow_redirects, proxies, 
                verify, cert, stream, hooks, cookies
    """
    def POST(self, url, **kwargs):
        with self.client.post(url=url, name=url, catch_response=True, **kwargs) as response:
            if response.json()["code"] != 0:
                response.failure("POST name = "+ str(url) + "Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("POST name = "+ str(url) + "Request took too long")


    """
    PUT function 
    parameter： url, headers, params, data, json, files, auth, timeout, allow_redirects, proxies, 
                verify, cert, stream, hooks, cookies
    """
    def PUT(self, url, **kwargs):
        with self.client.put(url=url, name=url, catch_response=True, **kwargs) as response:
            if response.json()["code"] != 0:
                response.failure("PUT name = "+ str(url) + "Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("PUT name = "+ str(url) + "Request took too long")
    """
    DELETE function 
    parameter： url, headers, params, auth, timeout, allow_redirects, proxies, 
                verify, cert, stream, hooks, cookies
    """
    def DELETE(self, url, **kwargs):
        with self.client.delete(url=url, name=url, catch_response=True, **kwargs) as response:
            if response.json()["code"] != 0:
                response.failure("DELETE name = "+ str(url) + "Got wrong response")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("DELETE name = "+ str(url) + "Request took too long")


    """
    Common function for getting the current time and date
    """
    @staticmethod
    def getNowTime():
        today_date = datetime.now().date()
        today_midnight = datetime.combine(today_date, datetime.min.time())
        date = {
            "today_midnight": today_midnight.strftime("%Y-%m-%d %H:%M:%S"),
            "now_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return date

    def getUserName(self):
        return self.userName

    def getPassWord(self):
        return self.passWord

    def getBaseUrl(self):
        return self.baseUrl
