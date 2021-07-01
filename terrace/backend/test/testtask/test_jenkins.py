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
        password = "11ec796312b80c8841f4eef5394b74af26"
        )
    print('-----')
    print(jenkins.keys())
    print(jenkins.version)
    print(jenkins.jobs.keys())
    print(jenkins.views.keys())
    # jenkins.jobs.build('http:/10.78.16.251:8080/0412newjob')
    # print(jenkins.jobs['http:/10.78.16.251:8080/0412newjob'])
    print(jenkins.views['all'])
    print(jenkins.items())
