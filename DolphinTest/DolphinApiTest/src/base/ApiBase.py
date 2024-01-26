# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : ApiBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/24 14:39
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
    get function 
    parameter： url, params
    """
    def get(self, url: str, **kwargs):
        response = requests.get(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("get func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("get func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("get func response：" + str(response.json()))
        return response

    """
    post function 
    parameter： url, data, json
    """
    def post(self, url: str, **kwargs):
        response = requests.post(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("post func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("post func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("post func response：" + str(response.json()))
        return response

    """
    put function 
    parameter： url, data, json
    """
    def put(self, url: str, **kwargs):
        response = requests.post(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("put func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("put func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("put func response：" + str(response.json()))
        return response

    """
    delete function 
    parameter： url, data, json
    """

    def delete(self, url: str, **kwargs):
        response = requests.post(self.getBaseUrl() + url, headers=self.getHeaders(), **kwargs)
        self.log.echolog("delete func request：" + str(self.getBaseUrl()) + str(url))
        if kwargs is not None:
            self.log.echolog("delete func kwargs：" + str(kwargs))
        else:
            pass
        self.log.echolog("delete func response：" + str(response.json()))
        return response

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
