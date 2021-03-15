from appium.webdriver.common.mobileby import MobileBy
from app_APPium_test.src.Add_Member import Add_Member
from app_APPium_test.src.BasePage import BasePage


class Address_book(BasePage):
    def go_to_add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
        #                                                        'true).instance(0)).scrollIntoView(new UiSelector('
        #                                                        ').text("添加成员").instance(0));').click()
        self.click(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                 'true).instance(0)).scrollIntoView(new UiSelector('
                                                 ').text("添加成员").instance(0));')
        return Add_Member(self.driver)
