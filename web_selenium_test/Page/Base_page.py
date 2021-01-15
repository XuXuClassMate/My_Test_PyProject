import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, Basedriver: WebDriver = None):
        if Basedriver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self._add_cookie_login()
        else:
            self.driver = Basedriver
        # 更新cookie
        self._get_cookie_login()

    def _add_cookie_login(self):
        # # 登录企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 读取cookie
        try:
            with open('/Users/bytedance/Desktop/我的/PythonProject/My_Test_Project/web_selenium_test/cookie.json',
                      'r') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # 页面刷新
            self.driver.refresh()
            # 登陆成功，到达首页
            self.driver.find_element_by_css_selector('#menu_index')
        except:
            # cookie失效等待60秒，人工扫码时间为60秒
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_css_selector('#menu_index')

    def _get_cookie_login(self):
        # 获取页面cookie
        cookie = self.driver.get_cookies()
        # 写入/更新cookie
        with open('/Users/bytedance/Desktop/我的/PythonProject/My_Test_Project/web_selenium_test/cookie.json', 'w') as f:
            json.dump(cookie, f)

    def find(self, by, locater):
        return self.driver.find_element(by, locater)

    def quit(self):
        self.driver.quit()
