# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : BinarySearch.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2022/1/18 8:57 上午


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]

listb = [1, 5, 3, 7, 4, 2, 9, 6]

x = int(input("请输入查找的数据："))


def select(alist):
    for i in alist:
        if i == x:
            print(f"select:你查找的数据在列表中的下标是{i}")


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
        print(f"ages：找到你数据的元素了{alist[mid + 1]}个元素")
    else:
        print("ages：没找到")


def bubb(alist):
    n = len(alist) - 1
    for j in range(0, n):
        for i in range(0, n - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


if __name__ == '__main__':
    print(select(lista))
    print(ages(lista))
    print(bubb(listb))
