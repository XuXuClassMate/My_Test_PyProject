# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : E2EBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/16 15:56

from DolphinTest.DolphinConfig import DolphinConfig
from DolphinTest.LogFile import Logs


class E2EBase(DolphinConfig):
    def __init__(self):
        super().__init__()
        self.log = Logs("DolphinE2ETest")
