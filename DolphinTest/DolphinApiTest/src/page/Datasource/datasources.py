# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : resources.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/14 09:41
from DolphinTest.DolphinApiTest.src.base.ApiBase import ApiBase


class Datasources(ApiBase):
    def connect(self, dataList: dict):
        data = self.template_json("datasources/datasources.json", dataList)
        request = self.POST("/datasources/connect", data=data)
        if self.ApiAssert(request):
            return True

    def create(self, dataList: dict):
        data = self.template_json("datasources/datasources.json", dataList)
        request = self.POST("/datasources", data=data)
        result = self.ApiAssert(request, "$.data")
        result_data = {
            'code': result[0]
        }
        self.log.echolog("datasources create api result data: " + str(result_data))
        return result_data

    def update(self, datasource_code, dataList: dict):
        data = self.template_json("datasources/datasources.json", dataList)
        request = self.POST("/datasources/" + datasource_code, data=data)
        result = self.ApiAssert(request, "$.data")
        result_data = {
            'code': result[0]
        }
        self.log.echolog("datasources update api result data: " + str(result_data))
        return result_data

    def search(self, searchVal: str = None, **kwargs):
        param = {
            "pageSize": 10,
            "pageNo": 1,
            "searchVal": searchVal
        }
        param.update(kwargs)
        request = self.GET("/datasources", params=param)
        result = self.ApiAssert(request, "$.data.totalList[:1].[id,name,code]")
        result_data = {
            'id': result[0],
            'name': result[1],
            'code': result[2]
        }
        self.log.echolog("datasources search api result data: " + str(result_data))
        return result_data

    def delete(self, datasource_code):
        request = self.DELETE("/datasources/" + datasource_code)
        if self.ApiAssert(request):
            return True
