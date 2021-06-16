# -*- coding: utf-8 -*-
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-15 18:31
IDE: PyCharm
Introduction:
"""
import json
from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from terrace.backend.src.testcase.main import TestCase

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)


class AddTestCaseTextService(Resource, TestCase):
    # def get(self):
    #     testcase_id = request.args.get('id', None)
    #     if testcase_id:
    #         for item in testcase_id:
    #             if item[testcase_id] == item:
    #                 return item
    #
    #         return {}
    #     else:
    #         testcases = TestCase.query.all()
    #         return [str(testcase) for testcase in testcases]

    def post(self):
        testcase = TestCase(
            id = request.json.get('id'),
            name = request.json.get('name'),
            data = request.json.get('data'),
            remark = json.dumps(request.json.get('remark'))
            )
        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase.query.all()
        return [str(testcase) for testcase in testcases]

    # def put(self):
    #     testcase = TestCase(
    #         id = request.json.get('id'),
    #         name = request.json.get('name'),
    #         data = request.json.get('data'),
    #         remark = json.dumps(request.json.get('remark'))
    #         )
    #     db.session.add(testcase)
    #     db.session.commit()

    # def delete(self):
    #     # 通过id删除测试用例
    #     testcase_id = request.json['id']
    #     # testcases = TestCase.query.all()
    #     # testcases.remove(testcase_id)
    #     # for item in testcase_id:
    #     #     if item['id'] == testcase_id:
    #     #         item.remove(testcase_id)
    #     testcases = TestCase.query.filter_by(id = id).first()
    #     db.session.delete(testcases)
    #     return [str(testcase) for testcase in testcases]


api.add_resource(AddTestCaseTextService, '/testCase/text')

if __name__ == '__main__':
    app.run(debug = True)
