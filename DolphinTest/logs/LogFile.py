# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : LogFile.py
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/1/22 19:23


import os
from datetime import datetime


class LogFile(object):
    dir_name = None
    target_dir = None

    def __init__(self, directory_name: str):
        self._logpath(directory_name)
        self._foldername = datetime.now().strftime('%Y-%m-%d')
        self._logfilename = "logs-" + datetime.now().strftime('%Y-%m-%d-%H') + ".log"

    @staticmethod
    def _logpath(directory_name):
        LogFile.dir_name = directory_name
        current_dir = os.getcwd()
        while True:
            if directory_name in os.listdir(current_dir):
                LogFile.target_dir = os.path.join(current_dir, directory_name)
                os.chdir(LogFile.target_dir)
                return
            else:
                new_dir = os.path.dirname(current_dir)
                if new_dir == current_dir:
                    raise FileNotFoundError(f"no search '{directory_name}' 的目录")
                else:
                    current_dir = new_dir

    def echolog(self, echocontent: str):
        os.makedirs(f"./Logs/{self._foldername}", exist_ok=True)
        with open(f'./Logs/{self._foldername}/{self._logfilename}', 'a') as f:
            logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2]
            print(logtime + " || " + echocontent + "\n")
            f.write(logtime + " || " + echocontent + "\n")
