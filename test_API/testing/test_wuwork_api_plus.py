from test_API.src.wuwork_api import wuwork_api
import pytest
from test_API.testing.Logfile import LogFile


class Test_wuwork_api:
    def setup(self):
        self.address = wuwork_api()
        self.log = LogFile()

    def test_add_member(self):
        self.log.echolog("开始清理数据")
        # 清理数据
        res = self.address.delete_muber(userid="zhangsan")
        self.log.echolog("清理数据返回json" + str(res))
        pytest.assume(res["errcode"] == 0)
        self.log.echolog("清理数据完成")

        # 查询成员，清理验证
        self.log.echolog("查询成员，清理验证")
        res = self.address.get_member(userid="zhangsan")
        self.log.echolog("查询成员返回json" + str(res))
        pytest.assume(res["errcode"] == 60111)
        self.log.echolog("查询成员完成")

        # 创建成员
        res = self.address.add_member(userid="zhangsan", name="张三", mobile="+86 13800000002", department=[1])
        self.log.echolog("创建成员返回json" + str(res))
        pytest.assume(res["errcode"] == 0)
        # 查询成员,创建验证
        res = self.address.get_member(userid="zhangsan")
        pytest.assume(res["errcode"] == 0)

        # 更新成员
        res = self.address.update_muber(userid="zhangsan", newname="李四")
        self.log.echolog("更新成员返回json" + str(res))
        pytest.assume(res["errcode"] == 0)
        self.log.echolog("更新成员完成")
        # 查询成员，更新验证
        res = self.address.get_member(userid="zhangsan")
        pytest.assume(res["errcode"] == 0)
        self.log.echolog("查询成员完成")

    if __name__ == '__main__':
        pytest.main('vs', 'test_wuwork_api_plus.py')
