# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : tenant.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/6 10:17
from DolphinTest.DolphinApiTest.src.base.ApiBase import ApiBase


class Tenant(ApiBase):
    def create(self, tenantName: str, **kwargs):
        getTenantId = self.GET("/queues/list")
        tenantId = self.ApiAssert(getTenantId, "$.data.id")
        verify_param = {
            "tenantCode": tenantName
        }
        verify = self.GET("/tenants/verify-code", params=verify_param)
        if self.ApiAssert(verify) is False:
            self.log.echolog("This tenant is not allowed to create：" + tenantName)
        data = {
            "tenantCode": tenantName,
            "queueId": tenantId,
            "description": ""
        }
        data.update(kwargs)
        request = self.POST("/tenants", data=data)
        result = self.ApiAssert(request, "$.data.[id,tenantCode]")
        result_data = {
            'tenantId': result[0],
            'tenantName': result[1],
        }
        self.log.echolog("tenant create api result data: " + str(result_data))
        return result_data

    def update(self, tenantId: str, tenantName: str, **kwargs):
        data = {
            "tenantCode": tenantName,
            "queueId": 1,
            "description": "",
            "id": tenantId
        }
        data.update(kwargs)
        request = self.PUT("/tenants/" + tenantId, data=data)
        if self.ApiAssert(request):
            return True

    def search(self, searchVal: str = None, **kwargs):
        param = {
            "pageSize": 10,
            "pageNo": 1,
            "searchVal": searchVal
        }
        param.update(kwargs)
        request = self.GET("/tenants", params=param)
        result = self.ApiAssert(request, "$.data.totalList[:1].[id,tenantCode]")
        result_data = {
            'tenantId': result[0],
            'tenantName': result[1],
        }
        self.log.echolog("tenants search api result data: " + str(result_data))
        return result_data

    def delete(self, tenantId):
        request = self.DELETE("/tenants/" + str(tenantId))
        if self.ApiAssert(request):
            return True
