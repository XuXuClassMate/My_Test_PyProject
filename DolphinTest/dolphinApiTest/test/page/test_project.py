# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_project.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/26 11:41
import pytest
import pytest_assume.plugin

from DolphinTest.DolphinApiTest.src.page import project


class TestProject:
    def setup_class(self):
        self.project = project.Project()

    def test_create(self):
        name = self.project.create("test_project")
        pytest.assume(name['name'] == 'test_project')