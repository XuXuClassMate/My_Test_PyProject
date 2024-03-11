# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_E2EBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/24 17:32
from DolphinTest.DolphinE2ETest.src.base.E2EBase import E2EBase


class Test_E2EBase:
    def setup_class(self):
        self.base = E2EBase()
    def test_login_with_cookie(self):
        self.base.login_with_cookie()

    def test_save_cookie(self):
        self.base.save_cookie()

    def test_save_to_file(self):
        assert True

    def test_load_cookie(self):
        self.base.load_cookie()

    def test_login(self):
        self.base.login()

    def test_navigate_to(self):
        self.base.navigate_to('/ui/projects/12646073406304/workflow-definition')
        self.base.click_element("text='工作流定义'")

    def test_find_element(self):
        pass

    def test_close_browser(self):
        pass

    def test_click_element(self):
        pass
