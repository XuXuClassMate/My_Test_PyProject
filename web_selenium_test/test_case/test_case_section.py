from time import sleep
from web_selenium_test.Page.main_page import MainPage


class TestSection:
    main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    def test_add_section(self):
        # 实例化HomePage类
        # main = MainPage()
        # 1.登录页面跳转到首页 2.首页跳转到通讯录页面 3.通讯录页面跳转到添加部门页面 4.添加部门 5.获取部门信息
        result1 = self.main.goto_section().add_section('测试部')
        sleep(2)
        result = result1.get_section_list()
        print(f"添加部门列表：{result}")
        assert '测试部' in result

    def test_update_section(self):
        # 更新部门名称 测试部 -->测试部修改
        result2 = self.main.goto_section().update_section('测试部修改')
        sleep(2)
        result = result2.get_section_list()
        print(f"修改部门列表：{result}")
        assert '测试部修改' in result

    def test_delete_section(self):
        # 删除测试部门名称 "测试部修改"
        result3 = self.main.goto_section().delete_section()
        sleep(2)
        result = result3.get_section_list()
        print(f"删除后部门列表：{result}")
        assert '测试部修改' not in result
