# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : BinarySearch.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2022/1/18 8:57 上午


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]

x = int(input("请输入查找的数据："))


def ages(alist):
    start = 0
    end = len(alist) - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == x:
            break
        elif alist[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    if start <= end:
        print(f"找到你数据的元素了{alist[mid] + 1}")
    else:
        print("没找到")


if __name__ == '__main__':
    ages(lista)
