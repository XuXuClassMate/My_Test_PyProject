# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : project.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/26 10:22

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
        result = self.ApiAssert(request,"$.data.[id,name,code]")
        result_data = {
            'id': result[0],
            'name': result[1],
            'code': result[2]
        }
        self.log.echolog("project create api result data: " + str(result_data))
        return result_data

    def search(self, searchVal: str = None, **kwargs):
        param = {
            "pageSize": 10,
            "pageNo": 1,
            "searchVal": searchVal
        }
        param.update(kwargs)
        request = self.GET("/projects", params=param)
        result = self.ApiAssert(request,"$.data.totalList[:1].[id,name,code]")
        result_data = {
            'id': result[0],
            'name': result[1],
            'code': result[2]
        }
        self.log.echolog("project search api result data: " + str(result_data))
        return result_data

    def update(self, projectCode, projectName: str, **kwargs):
        data = {
            "projectName": projectName,
            "description": "",
            "userName": self.getUserName()
        }
        data.update(kwargs)
        request = self.PUT("/projects/" + str(projectCode), data=data)
        result = self.ApiAssert(request, "$.data.[:1].[id,name,code]")
        result_data = {
            'id': result[0],
            'name': result[1],
            'code': result[2]
        }
        self.log.echolog("project update api result data: " + str(result_data))
        return result_data

    def delete(self, projectCode):
        request = self.DELETE("/projects/" + str(projectCode))
        if self.ApiAssert(request):
            return True
