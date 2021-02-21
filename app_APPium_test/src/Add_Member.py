from appium.webdriver.common.mobileby import MobileBy

from app_APPium_test.src.BasePage import BasePage
from app_APPium_test.src.Manual_add import Manual_add


class Add_Member(BasePage):
    def go_to_Manual_add(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return Manual_add(self.driver)

    def get_add_Toast(self):
        ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return ele
