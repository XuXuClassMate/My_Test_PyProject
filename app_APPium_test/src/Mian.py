from appium.webdriver.common.mobileby import MobileBy
from app_APPium_test.src.Address_book import Address_book
from app_APPium_test.src.BasePage import BasePage


class Main(BasePage):
    def go_to_Address_book(self):  # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return Address_book(self.driver)
