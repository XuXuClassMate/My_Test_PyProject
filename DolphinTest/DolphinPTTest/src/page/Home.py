# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Home.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/18 17:15
from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase

class Home(PTBase):
    def __init__(self, client):
        super().__init__(client)

    def TaskStateCount(self):
        param = {
            "startDate": self.getNowTime()["today_midnight"],
            "endDate": self.getNowTime()["now_time"] ,
            "projectCode": 0
        }
        self.GET("/projects/analysis/task-state-count", params=param)
    def DefineUserCount(self):
        param = {
            "projectCode": 0
        }
        self.GET("/projects/analysis/define-user-count", params=param)

    def ProcessStateCount(self):
        param = {
            "startDate": self.getNowTime()["today_midnight"],
            "endDate": self.getNowTime()["now_time"],
            "projectCode": 0
        }
        self.GET("/projects/analysis/process-state-count", params=param)
