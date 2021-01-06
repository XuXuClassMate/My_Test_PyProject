import json
from time import sleep

from selenium import webdriver


class Test_weixin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        try:
            with open('cookie.json', 'r') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.driver.find_element_by_css_selector('#menu_customer > span').click()
        except:
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_css_selector('#menu_customer > span').click()
        cookie = self.driver.get_cookies()
        with open('cookie.json', 'w') as f:
            json.dump(cookie, f)

        sleep(5)





