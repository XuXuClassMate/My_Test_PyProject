import os
from selenium import webdriver


class base:
    def setup(self):
        browser = os.getenv('browser')
        # 切换浏览器执行需要再Terminal中执行：browser=chrome pytest name.py
        if browser == "firefox":
            self.driver = webdriver.firefox()
        elif browser == "safari":
            self.driver = webdriver.safari()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
