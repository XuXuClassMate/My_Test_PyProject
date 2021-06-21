# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-06-20 15:35
IDE: PyCharm
Introduction:
"""


import requests
# 获取token

r = requests.get('http://127.0.0.1:5000/login', auth = {'magigo', '123456'})
print(r.text)

# token验证

# token = ''
# r = requests.get('http://127.0.0.1:5000/tes123', params = {'token': token})
# print(r.text)

