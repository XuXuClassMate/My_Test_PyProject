from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        phone_info = {
            "platformName": "android",
            "platformVersion": "8.1",
            "deviceName": "S4F6R19C18016391",
            "noReset": True,
            'browserName': 'Browser',
            "skipDeviceInitialization": "true",
            "resetKeyBoard": "true",
            "waitFoeIdleTimeout": 0,
            "chromedriverExecutable": "/Users/bytedance/Desktop/My/APPium/android-webview/chromedriver"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", phone_info)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    balck_list = [(By.XPATH, "//*[@class='classes']")]
    def find(self, locator):
        # 捕获异常（元素没找到）
        try:
            result = self.driver.find_element(*locator)
            return result
        except Exception as e:
            # 遍历黑名单（弹窗）
            for black in balck_list:
                # 如果发现黑名单中的元素存在
                eles = self.driver.find_elements(*black)
                # 对黑名单进行处理
                if len(eles) > 0:
                    # 通过点击的方式，关闭弹窗
                    eles[0].click()
                    # 再次查找元素
                    return self.find(locator)
            raise e

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        # 下面的操作和selenium保持一致
        sleep(5)
        search_locator = (By.ID, 'index-kw')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()

