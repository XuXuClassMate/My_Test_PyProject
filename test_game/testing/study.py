# -*- coding: utf-8 -*- 
"""
Project: My_Test_Project
Creator: bytedance
Create time: 2021-07-08 09:59
IDE: PyCharm
Introduction:
"""
from __future__ import division
from math import sqrt

print(sqrt(9))

print("this's  windows computer")


# result = 9
# for i in range(0, 10, 2):
#     x = result - i
#     print(x)

# result = 9
# x = 0
# while x < 10:
#     a = result - x
#     x = x+2
#     print(a)


def sum(x, y):
    result = 0
    for b in range(x, y + 1):
        result = result + b
        if b == y:
            print(result)


sum(1, 49)
