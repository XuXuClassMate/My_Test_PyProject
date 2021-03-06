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
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
app.config['AQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou5:hogwarts@stuq.ceshiren.com:23306/lagou5db?charset' \
                                        '=utf8mb4'
db = SQLAlchemy(app)
jenkins = Jenkins(
    'http://localhost:8080/',
    username="admin",
    # 需要用户管理添加token
    password="11ec796312b80c8841f4eef5394b74af26"
)


# 测试用例的管理
class TestCase_Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 测试名称 80个字符，不是唯一，不能为空
    name = db.Column(db.String(80), unique=False, nullable=False)
    # 用例为文本数据类型
    data = db.Column(db.String(1000), unique=False, nullable=False)
    # 备注 ，1000个字符，允许不唯一，允许为空
    remark = db.Column(db.String(1000), unique=False, nullable=True)

    def __repr__(self):
        return '<TestCase_Text %r>' % self.name


class TestCaseTextService(Resource):
    def get(self):
        testcase_id = request.args.get('id', None)
        app.logger.info({'id': testcase_id})
        if testcase_id:
            for item in testcase_id:
                if item[testcase_id] == item:
                    return item
            return {}
        else:
            testcases = TestCase_Text.query.all()
            return [str(testcase) for testcase in testcases]

    def post(self):
        testcase = TestCase_Text(
            id=request.json.get('id'),
            name=request.json.get('name'),
            data=request.json.get('data'),
            remark=json.dumps(request.json.get('remark'))
        )
        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase_Text.query.all()
        return [str(testcase) for testcase in testcases]

    def put(self):
        testcase = TestCase_Text(
            id=request.json.get('id'),
            name=request.json.get('name'),
            data=request.json.get('data'),
            remark=json.dumps(request.json.get('remark'))
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
        testcase = TestCase_Text.query.filter_by(id=testcase_id).first()
        testcases = TestCase_Text.query.all()
        db.session.delete(testcase)
        return [str(testcase) for testcase in testcases]


'''
测试套件  一个套件包括一个带有顺序的测试用例列表
更复杂的情况是一个套件，可以包含自套件，自套件之间具备穿并行关系
xUnit概念
pytest dir => [test_1.py::test_a, test_1.py::test_b,test_2.py::test_c]
suite test_python.py
suite [test_1.py::test_a, test_1.py::test_b,test_2.py::test_c]
'''


class Suite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    testcases = db.Column(db.String(1000), unique=False, nullable=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'testcases': json.loads(self.testcases)
        }

    def __repr__(self):
        return f'<Suite id={self.id}    {self.name}>'


class SuiteService:
    def get(self):
        id = request.args.get('id', None)
        app.logger.info({'id': id})
        if id:
            suite = Suite.query.filter_by(id=id).first()
            return str(suite)
        else:
            suites = Suite.query.all()
            return [Suite.as_dict() for suite in suites]

    def post(self):
        suite = Suite(
            name=request.json.get('name'),
            testcases=json.dumps(request.json.get('testcases'))
        )
        db.session.add(suite)
        db.session.commit()

        suites = Suite.query.all()
        return [str(suite) for suite in suites]


# 根据套件的ID，渠道对应的存在的套件，并把太监的数据发给jenkins进行执行
class ExcutionService(Resource):
    def post(self):
        suite_id = request.json.get('suite_id')
        suite = Suite.query.filter_by(id=suite_id)

        jenkins.jobs['testcase_id'].invoke(
            build_params={
                'suite': json.dumps(suite.as_dict()),
                'command': f'git clone https://github.com/yanxuping/My_Test_Project.git .; pytest {suite.testcases}'
            }
        )


class Result:
    pass


# jenkins通过curl命令或者其他的客户端工具，把测试结果，主要是junit.xml allure报告上传
class ResultService(Resource):
    pass


api.add_resource(TestCaseTextService, '/testCase/text')
api.add_resource(SuiteService, '/suite')
api.add_resource(ExcutionService, '/execution')

if __name__ == '__main__':
    app.run(debug=True)
