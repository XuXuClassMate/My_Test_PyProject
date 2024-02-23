# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : statistic.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/21 19:39

from DolphinTest.DolphinPTTest.src.base.PTBase import PTBase

class Statistic(PTBase):
    def __init__(self, client):
        super().__init__(client)

    def GetQueueCount(self):
        self.GET("/projects/analysis/queue-count")

    def GetCommandStateCount(self):
        self.GET("/projects/analysis/command-state-count")