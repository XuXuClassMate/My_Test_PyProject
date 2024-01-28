# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : ApiBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/24 14:39
import pytest
import requests
from DolphinTest.DolphinConfig import DolphinConfig
from DolphinTest.logsfile.LogFile import Logs


class ApiBase(DolphinConfig):
    SessionId = None

    def __init__(self):
        super().__init__()
        self.log = Logs("DolphinApiTest")
        ApiBase.SessionId = self.getSession()

    def getSession(self):
        if ApiBase.SessionId is None:
            request = requests.post(self.getBaseUrl() + "/login",
                                    data={"userName": self.getUserName(), "userPassword": self.getPassWord()})
            if request.status_code == 200:
                SessionId = request.json()['data']['sessionId']
                return SessionId
            else:
                print("get session error")
        else:
            return ApiBase.SessionId

    """
    GET function 
    parameter： url, params
    """

    def GET(self, url: str, **kwargs):
        response = requests.get(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("GET func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("GET func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("GET func response：" + str(response.json()))
        return response

    """
    POST function 
    parameter： url, data, json
    """

    def POST(self, url: str, **kwargs):
        response = requests.post(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("POST func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("POST func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("POST func response：" + str(response.json()))
        return response

    """
    PUT function 
    parameter： url, data, json
    """

    def PUT(self, url: str, **kwargs):
        response = requests.post(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("PUT func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("PUT func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("PUT func response：" + str(response.json()))
        return response

    """
    DELETE function 
    parameter： url, data, json
    """

    def DELETE(self, url: str, **kwargs):
        response = requests.post(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("DELETE func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("DELETE func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("DELETE func response：" + str(response.json()))
        return response

    def ApiAssert(self, response: object):
        if response.status_code in (requests.codes.ok, 201):
            self.log.echolog("HTTP Success!")
            result = response.json()
            if pytest.assume(result["code"] == 0):
                self.log.echolog("API code Success")
                return result
            else:
                self.log.echolog("API an error occurred. Status code: " + str(result["code"]))
                self.log.echolog("Error: " + str(result))
        else:
            self.log.echolog("HTTP an error occurred. Status code: " + str(response.status_code))

    def getUserName(self):
        return self.userName

    def getPassWord(self):
        return self.passWord

    def getBaseUrl(self):
        return self.baseUrl

    @staticmethod
    def getHeaders():
        Header = {
            'Language': 'zh_CN',
            'Accept': 'application/json, text/plain, */*',
            'Sessionid': ApiBase.SessionId
        }
        return Header
