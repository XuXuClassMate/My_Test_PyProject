# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-16 10:07
IDE: PyCharm
Introduction:
"""
import json
from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['AQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou5:hogwarts@stuq.ceshiren.com:23306/lagou5db?charset' \
                                        '=utf8mb4'
db = SQLAlchemy(app)


class TestCase_File(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # 测试名称 80个字符，不是唯一，不能为空
    name = db.Column(db.String(80), unique = False, nullable = False)
    # 用例为文件数据类型
    file = db.Column(db.String(1000), unique = False, nullable = False)
    # 备注 ，1000个字符，允许不唯一，允许为空
    remark = db.Column(db.String(1000), unique = False, nullable = True)

    def __repr__(self):
        return '<TestCase_File %r>' % self.name


class TestCaseTextService(Resource):
    def get(self):
        testcase_id = request.args.get('id', None)
        if testcase_id:
            for item in testcase_id:
                if item[testcase_id] == item:
                    return item

            return {}
        else:
            testcases = TestCase_File.query.all()
            return [str(testcase) for testcase in testcases]

    def post(self):
        testcase = TestCase_File(
            id = request.json.get('id'),
            name = request.json.get('name'),
            file = request.json.get('file'),
            remark = json.dumps(request.json.get('remark'))
            )
        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase_File.query.all()
        return [str(testcase) for testcase in testcases]

    def put(self):
        testcase = TestCase_File(
            id = request.json.get('id'),
            name = request.json.get('name'),
            file = request.json.get('file'),
            remark = json.dumps(request.json.get('remark'))
            )
        db.session.add(testcase)
        db.session.commit()

    def delete(self):
        # 通过id删除测试用例
        testcase_id = request.json['id']
        # testcases = TestCaseText.query.all()
        # testcases.remove(testcase_id)
        # for item in testcase_id:
        #     if item['id'] == testcase_id:
        #         item.remove(testcase_id)
        testcase = TestCase_File.query.filter_by(id = testcase_id).first()
        testcases = TestCase_File.query.all()
        db.session.delete(testcase)
        return [str(testcase) for testcase in testcases]


api.add_resource(TestCaseTextService, '/testCase/file')


if __name__ == '__main__':
    app.run(debug = True)
