# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : test.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2022/1/26 3:36 下午

def fun1():
    filst = str("""{
        "account": "0xAA42717e6bD0Ba9Bd4c11Dc9C4529CEa4937fd24",
        "amount": "5",
        "sign": "increase"
    }""") + ","
    return filst


def fun2():
    filst = str("""{
        "account": "0xAA42717e6bD0Ba9Bd4c11Dc9C4529CEa4937fd24",
        "amount": "3",
        "sign": "decrease"
    }""") + ","
    return filst


def fun(num):
    nums = num//2
    for i in range(nums):
        print(fun1() + fun2())


if __name__ == '__main__':
    fun(250)
