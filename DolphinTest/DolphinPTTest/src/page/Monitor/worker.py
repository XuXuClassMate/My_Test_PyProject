# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : worker.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/21 19:34

from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
class Worker(PTBase):
    def __init__(self, client):
        super().__init__(client)

    def Get_Worker(self):
        self.GET("/monitor/workers")
