# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-16 11:06
IDE: PyCharm
Introduction:
"""

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
from terrace.backend.src.testcase.main import TestCase

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)


class AddTestCaseFileService(Resource, TestCase):
    def post(self):
        testcase = TestCase(
            id = request.json.get('id'),
            name = request.json.get('name'),
            data = request.json.get('file'),
            remark = json.dumps(request.json.get('remark'))
            )
        db.session.add(testcase)
        db.session.commit()

        testcases = TestCase.query.all()
        return [str(testcase) for testcase in testcases]


api.add_resource(AddTestCaseFileService, '/testCase/file')

if __name__ == '__main__':
    app.run(debug = True)
