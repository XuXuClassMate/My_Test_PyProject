# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Project.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/22 20:30
from DolphinTest.dolphinApiTest.src.base import Base
import pytest


class Project(Base):
    def create(self, projectName: str, **kwargs):
        request = self.post("/projects", data={
            "projectName": projectName,
            "description": None,
            "userName": self.username
        })
        pytest.assume(request["errcode"] == 0)
        pytest.assume(request["access_token"] is not None)
        return request
