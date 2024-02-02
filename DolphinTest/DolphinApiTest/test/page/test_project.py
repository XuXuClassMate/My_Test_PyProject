# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_project.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/26 11:41
import pytest

from DolphinTest.DolphinApiTest.src.page import project


class TestProject:
    def setup_class(self):
        self.project = project.Project()

    def teardown_class(self):
        code = self.project.search('test_project')
        assert self.project.delete(projectCode=code["code"])

    def test_create(self):
        name = self.project.create("test_project")
        pytest.assume(name['name'] == 'test_project')

    def test_search(self):
        name = self.project.search(searchVal='test_project')
        pytest.assume(name['name'] == 'test_project')

    def test_update(self):
        code = self.project.search('test_project')
        name = self.project.update(projectCode=code["code"], projectName="test_project_update")
        pytest.assume(name['name'] == 'test_project_update')

    # Redefine execution in teardown
    # def test_delete(self):
    #     code = self.project.search('test_project_update')
    #     assert self.project.delete(projectCode=code["code"])
