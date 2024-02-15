# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test_ApiBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/24 15:10

from DolphinTest.DolphinApiTest.src.base.ApiBase import ApiBase


class TestApiBase:

    def setup_class(self):
        self.apibase = ApiBase()

    def test_getSession(self):
        result = self.apibase.getSession()
        print(result)

    def test_getJsonData(self, false=None, true=None):
        date = {
            "code": 0,
            "msg": "成功",
            "data": {
                "id": 58,
                "userId": 1,
                "userName": "admin",
                "code": 12460586953696,
                "name": "test_project",
                "description": "",
                "createTime": "2024-02-01 09:12:15",
                "updateTime": "2024-02-01 09:12:15",
                "perm": 0,
                "defCount": 0,
                "instRunningCount": 0
            },
            "failed": false,
            "success": true
        }

        result = self.apibase.getJsonData(date, "$.data.[id,name,code]")
        print(result)
        return result

    def test_template_json(self):
        date = {
            "type": "Oracle",
            "name": "OracleTest",
            "host": "www.xuxuclassmaet.cn",
            "port": 4453,
            "database": "default",
            "Test-add-type": "XuXuClassMate"
        }

        result = self.apibase.template_json("datasources/datasources.json", date)
        print(result)
