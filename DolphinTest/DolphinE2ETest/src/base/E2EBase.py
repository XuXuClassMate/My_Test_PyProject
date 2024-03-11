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
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def login_with_cookie(self) -> bool:
        saved_cookie = self.load_cookie()  # Load saved cookie
        if saved_cookie:
            self.page.context.add_cookies(saved_cookie)
            self.page.goto(self.getBaseUrl() + '/ui/home')  # Navigate to the homepage
            return True
        return False

    def save_cookie(self):
        cookies = self.page.context.cookies()  # Get current page's cookies
        self.log.echolog("Get current page's cookies：" + str(cookies))
        self.save_to_file(cookies)  # Save cookies to a file for future use

    @staticmethod
    def save_to_file(cookies):
        # Saving cookies to a file
        with open('cookies.txt', 'w') as f:
            f.write(str(cookies))

    @staticmethod
    def load_cookie():
        # Load saved cookies from file
        try:
            with (open('cookies.txt', 'r') as f):
                cookie_str = f.read()
                return eval(cookie_str)if cookie_str else None
        except FileNotFoundError:
            return None

    def login(self) -> bool:
        self.log.echolog("login operation")
        if not self.login_with_cookie():
            self.page.goto(self.getBaseUrl() + '/ui/login')
            self._input('[placeholder="请输入用户名"]', self.getUserName())
            self._input("[placeholder='请输入密码']", self.getPassWord())
            self.click_element('[role="button"][name="登录"]')
            if self.find_element('[role="menuitem"][name="首页"] span').is_visible():
                self.save_cookie()  # Save cookie after successful login
            else:
                self.log.echolog("Login failed. Please check your username and password.")
        return True

    def navigate_to(self, url: str):
        self.log.echolog("navigate to page: " + str(self.getBaseUrl()+ url))
        self.page.goto(self.getBaseUrl()+ url)

    def find_element(self, selector: str):
        self.log.echolog("find element by selector " + str(selector))
        return self.page.locator(selector)

    def close_browser(self):
        self.log.echolog("close browser")
        self.browser.close()

    def click_element(self, element: str):
        self.log.echolog("click element by selector ：" + str(element))
        target_element = self.page.query_selector(element)
        if target_element:
            target_element.click()
        else:
            self.log.echolog("Element not found: " + str(element) + ". Cannot click.")

    def _input(self, element: str, text: str):
        self.log.echolog("by element :" + str(element)+"， input content ："+ text)
        target_element = self.page.query_selector(element)
        if target_element:
            target_element.fill(text)
        else:
            self.log.echolog("Element not found: " + str(element) + ". Cannot input："+ text +".")