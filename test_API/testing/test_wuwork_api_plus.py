from test_API.src.wuwork_api import wuwork_api
import pytest


class Test_wuwork_api:
    def setup(self):
        self.address = wuwork_api()

    def test_add_member(self):
        # 清理数据
        res = self.address.delete_muber(userid="zhangsan")
        pytest.assume(res["errcode"] == 0)

        # 查询成员，清理验证
        self.address.get_member(userid="zhangsan")

        # 创建成员
        self.address.add_member(userid="zhangsan", name="张三", mobile="+86 13800000002", department=[1])
        # 查询成员,创建验证
        self.address.get_member(userid="zhangsan")

        # 更新成员
        self.address.update_muber(userid="zhangsan", newname="李四")
        # 查询成员，更新验证
        self.address.get_member(userid="zhangsan")
