# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : User.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/21 11:55

from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase

class User(PTBase):
    def __init__(self, client):
        super().__init__(client)

    def GetUserInfo(self):
        self.GET("/users/get-user-info")

    def GetUserList(self):
        param = {
            "pageNo": 1,
            "pageSize": 10,
            "searchVal": ""
        }
        self.GET("/users/list-paging", params = param)

    def UpdateUser(self, **kwargs):
        param = {
            "userPassword": "",
            "id": 1,
            "userName":"",
            "tenantId":1,
            "email":"",
            "phone":"",
            "state": 1,
            "timeZone": "Asia/Shanghai"
        }
        param.update(kwargs)
        self.POST("/users/update", params = param)



