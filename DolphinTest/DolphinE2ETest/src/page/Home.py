# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Home.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/24 16:50
from DolphinTest.DolphinE2ETest.src.base.E2EBase import E2EBase


class Home(E2EBase):
    def __init__(self):
        super().__init__()
        self.click_element('[role="menuitem"][name="首页"] span')

    def click_home_button(self):
        self.click_element('[role="heading"][name="任务状态统计"]')



