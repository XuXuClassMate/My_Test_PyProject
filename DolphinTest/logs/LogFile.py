# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Logs.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/22 19:23


import os
from datetime import datetime


class Logs(object):
    def __init__(self):
        self._foldername = datetime.now().strftime('%Y-%m-%d')
        self._logfilename = "logs-" + datetime.now().strftime('%Y-%m-%d-%H') + ".txt"

    def echolog(self, echocontent: str):
        path = os.listdir("..")
        logs = "Logs"
        if logs not in path:
            os.mkdir("../Logs")
        path2 = os.listdir("../Logs")
        if self._foldername not in path2:
            os.mkdir(f"../Logs/{self._foldername}")
        with open(f'../Logs/{self._foldername}/{self._logfilename}', 'a') as f:
            logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2]
            print(logtime + " || " + echocontent + "\n")
            f.write(logtime + " || " + echocontent + "\n")
