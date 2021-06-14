import json

from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['AQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagoou5:ceshiren.com@stuq.ceshiren.com:23306/lagou5db' \
                                        '?charset' \
                                        '=utf8mb4'
db = SQLAlchemy(app)


# testcases = []


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = False, nullable = False)  # 测试名称 80个字符，不是唯一，不能为空
    steps = db.Column(db.String(1000), unique = False, nullable = True)  # 备注 ，1000个字符，允许不唯一，允许为空

    def __repr__(self):
        return '<TestCase %r>' % self.name


class TestCaseService(Resource):
    def get(self):
        testcase_id = request.args.get('id', None)
        if testcase_id:
            for item in testcase_id:
                if item[testcase_id] == item:
                    return item

            return {}
        else:
            testcases = TestCase.query.all()
            return [str(testcase) for testcase in testcases]

    def post(self):
        testcase = TestCase(
            id = request.json.get('id'),
            name = request.json.get('name'),
            steps = json.dumps(request.json.get('steps'))
            )
        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase.query.all()
        return [str(testcase) for testcase in testcases]

    def put(self):
        pass

    def delete(self):
        # 通过id删除测试用例
        testcase_id = request.json['id']
        # testcases = TestCase.query.all()
        # testcases.remove(testcase_id)
        # for item in testcase_id:
        #     if item['id'] == testcase_id:
        #         item.remove(testcase_id)
        testcases = TestCase.query.filter_by(id = id).first()
        db.session.delete(testcases)
        return [str(testcase) for testcase in testcases]


api.add_resource(TestCaseService, '/testcase')

if __name__ == '__main__':
    app.run(debug = True)
