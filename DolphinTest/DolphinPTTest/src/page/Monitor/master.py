# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : master.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/21 19:31

from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase
class Master(PTBase):
    def __init__(self, client):
        super().__init__(client)

    def Get_Master(self):
        self.GET("/monitor/masters")