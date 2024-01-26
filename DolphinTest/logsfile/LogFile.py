# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : Logs.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/22 19:23


import os
from datetime import datetime


class Logs(object):

    def __init__(self, dir_name: str):
        self._foldername(dir_name)
        self._foldername = datetime.now().strftime('%Y-%m-%d')
        self._logfilename = "logs-" + datetime.now().strftime('%Y-%m-%d-%H') + ".txt"

    @staticmethod
    def _foldername(dir_name):
        current_dir = os.getcwd()

        while True:
            if dir_name in os.listdir(current_dir):
                target_dir = os.path.join(current_dir, dir_name)
                os.chdir(target_dir)
                return
            else:
                new_dir = os.path.dirname(current_dir)
                if new_dir == current_dir:
                    raise FileNotFoundError(f" no search '{dir_name}' 的目录")
                else:
                    current_dir = new_dir

    def echolog(self, echocontent: str):
        os.makedirs(f"./Logs/{self._foldername}", exist_ok=True)
        with open(f'./Logs/{self._foldername}/{self._logfilename}', 'a') as f:
            logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2]
            print(logtime + " || " + echocontent + "\n")
            f.write(logtime + " || " + echocontent + "\n")
