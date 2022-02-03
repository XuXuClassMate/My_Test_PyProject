# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : testplus.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2022/1/27 10:04 上午
import json
import random

account = ["0xAA42717e6bD0Ba9Bd4c11Dc9C4529CEa4937fd24", "0x6f68E22a3Ae1aB7E812Eaf21E168cDC4056085c1",
           "0xc082398C2942A6e988fCcAD604E6BB8bB136D70F", "0xBEf151B26d3129dD385e1B034954F4807bA06BA1"]
amount = ["6", "2", "8", "4"]
sign = ["increase", "decrease", "increase", "decrease"]


def fun(num):
    lists = []
    for i in range(num):
        x = random.randint(0, 3)
        cai = {"account": account[x],
               "amount": amount[x],
               "sign": sign[x]
               },
        lists.append(cai)
    return json.dumps(lists).replace("[", "").replace("]", "")


if __name__ == '__main__':
    print("[" + fun(500) + "]")
