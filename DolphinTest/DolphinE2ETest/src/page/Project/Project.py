# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Project.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/25 18:54
from DolphinTest.DolphinE2ETest.src.base.E2EBase import E2EBase


class Project(E2EBase):
    def __init__(self):
        super().__init__()
        self.click_element('[role="menuitem"][name="项目管理"] div')

    def create(self, project_name):
        pass

    def delete(self, project_name):
        pass
    def update(self, project_name):
        pass

    def search(self, project_name):
        pass

    def enter(self, project_name:str):
        self.click_element(f"text='{project_name}'")
