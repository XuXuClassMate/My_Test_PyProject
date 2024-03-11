# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : E2EBase.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2024/2/16 15:56

from DolphinTest.DolphinConfig import DolphinConfig
from DolphinTest.LogFile import Logs
from playwright.sync_api import sync_playwright


class E2EBase(DolphinConfig):
    def __init__(self):
        super().__init__()
        self.log = Logs("DolphinE2ETest")
        self.page = None

    def open_page(self):
        self.log.echolog(f"Opening page: {self.getBaseUrl()}")
        self.page.goto(self.getBaseUrl()+"/ui/login")

    def save_cookies(self):
        cookies = self.page.context.cookies()
        with open('cookies.txt', 'w') as f:
            f.write(str(cookies))

    def load_cookies(self):
        with open('cookies.txt', 'r') as f:
            cookies = f.read()
        self.page.context.add_cookies(cookies)

    def check_login_status(self):
        if "登录" in self.page.title():
            self.login()

    def login(self):
        print("Logging in...")
        self.page.set_title("已登录")

        self.save_cookies()