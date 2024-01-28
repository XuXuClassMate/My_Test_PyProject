# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : project.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/26 10:22
import pytest
import requests

from DolphinTest.DolphinApiTest.src.base.ApiBase import ApiBase


class Project(ApiBase):
    def create(self, projectName: str, **kwargs):
        data = {
            "projectName": projectName,
            "description": "",
            "userName": self.getUserName()
        }
        data.update(kwargs)
        request = self.POST("/projects", data=data)
        result = self.ApiAssert(request)
        Resultant = {
            'name': result['data']['name'],
            'id': result['data']['id'],
            'code': result['data']['code']
        }
        self.log.echolog("project create api result data: " + str(Resultant))
        return Resultant

    def search(self, **kwargs):
        param = {
            "pageSize": 10,
            "pageNo": 1,
            "searchVal": ""
        }
        param.update(kwargs)
        request = self.GET("/projects", params=param)
        result = self.ApiAssert(request)
        data = {
            'name': result['data']['name'],
            'id': result['data']['id'],
            'code': result['data']['code']
        }
        self.log.echolog("project search api result data: " + str(data))
        return data

    def update(self, projectCode, projectName: str, **kwargs):
        data = {
            "projectName": projectName,
            "description": "",
            "userName": self.getUserName()
        }
        data.update(kwargs)
        request = self.PUT("/projects/" + str(projectCode), data=data)
        result = self.ApiAssert(request)
        Resultant = {
            'name': result['data']['name'],
            'id': result['data']['id'],
            'code': result['data']['code']
        }
        self.log.echolog("project update api result data: " + str(Resultant))
        return Resultant

    def delete(self, projectCode):
        request = self.DELETE("/projects/" + str(projectCode))
        if self.ApiAssert(request):
            return True
        else:
            pass
