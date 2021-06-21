# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-17 21:52
IDE: PyCharm
Introduction:
"""
from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    jenkins = Jenkins(
        'http://localhost:8080/',
        username = "admin",
        # 需要用户管理添加token
        password = "11b08f5bb2929885569dbc97d6232cd310"
        )
    print(jenkins.keys())
    print(jenkins.version)
    print(jenkins.jobs.keys())
    print(jenkins.views.keys())
    jenkins.jobs.build("0412newjob")
