# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : StackLearning.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2022/1/18 9:37 上午

from pythonds.basic.stark import Stack


def ParChecker(SymbolString):
    s = Stack
    balanced = True
    index = 0
    while index < len(SymbolString) and balanced:
        Symbol = SymbolString[index]
        if Symbol == "(":
            s.push(Symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(ParChecker('((()))'))

print(ParChecker('(()'))
