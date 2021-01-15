from time import sleep
import re

from web_selenium_test.Page.main_page import MainPage


class TestAddSection:
    main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    def test_add_section(self):
        # 实例化HomePage类
        # main = MainPage()
        # 1.登录页面跳转到首页 2.首页跳转到通讯录页面 3.通讯录页面跳转到添加部门页面 4.添加部门 5.获取部门信息
        section = self.main.goto_add_section().add_section('测试部')
        sleep(2)
        result = section.get_list()
        print(result)
        assert '测试部' in result
