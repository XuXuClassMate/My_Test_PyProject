import os
from datetime import datetime


class LogFile(object):
    def __init__(self):
        # foldername >> 文件夹名称
        self._foldername = datetime.now().strftime('%Y-%m-%d')
        # logfilename >> 文件名称
        self._logfilename = "logs-" + datetime.now().strftime('%Y-%m-%d-%H') + ".txt"

    def echolog(self, echocontent: str):  # echocontent: str
        # 获取父级目录
        path = os.listdir("..")
        logs = "Logs"
        if logs not in path:
            # 创建Logs文件夹
            os.mkdir("../Logs")
        path2 = os.listdir("../Logs")
        if self._foldername not in path2:
            # 创建文件logfilename >> 文件名称
            os.mkdir(f"../Logs/{self._foldername}")
        # 创建日志文件及日志打印
        with open(f'../Logs/{self._foldername}/{self._logfilename}', 'a') as f:
            # logtime >> 文件中的时间
            logtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S  %f')[:-2]
            f.write(logtime + " || " + echocontent + "\n")
