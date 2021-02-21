from appium.webdriver.common.mobileby import MobileBy
from app_APPium_test.src.BasePage import BasePage


class Manual_add(BasePage):
    def add_name(self, add_name):
        name = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText')
        name.send_keys(add_name)
        return self

    def add_num(self, add_num):
        num = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"帐号")]/../android.widget.EditText')
        num.send_keys(add_num)
        return self

    def add_another_name(self, add_another_name):
        another_name = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"别名")]/../android.widget.EditText')
        another_name.send_keys(add_another_name)
        return self

    def add_iphone_num(self, add_iphone_num):
        iphone_num = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]')
        iphone_num.send_keys(add_iphone_num)
        return self

    def complete(self):
        from app_APPium_test.src.Add_Member import Add_Member
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                               'true).instance(0)).scrollIntoView(new UiSelector('
                                                               ').text("保存").instance(0));').click()
        return Add_Member(self.driver)
