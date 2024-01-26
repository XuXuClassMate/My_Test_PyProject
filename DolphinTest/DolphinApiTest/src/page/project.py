# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : project.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/26 10:22
import pytest

from DolphinTest.DolphinApiTest.src.base.ApiBase import ApiBase


class Project(ApiBase):
    def create(self, projectName: str, **kwargs):
        data = {
            "projectName": projectName,
            "description": "",
            "userName": self.getUserName()
        }
        data.update(kwargs)
        request = self.post("/projects", data=data)
        print("status_code" + str(request.status_code))
        pytest.assume(request.status_code == 201)
        result = request.json()
        pytest.assume(result["code"] == 0)
        data = {
            'name': result['data']['name'],
            'id': result['data']['id'],
            'code': result['data']['code']
        }
        self.log.echolog(str(data))
        return data
