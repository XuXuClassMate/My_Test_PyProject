from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

phone_info = {
    "platformName": "android",
    "platformVersion": "8.1",
    "deviceName": "S4F6R19C18016391",
    "appPackage": "com.tencent.wework",
    "appActivity": ".launch.LaunchSplashActivity t9",
    "noReset": "true",
    # "dontStopAppOnReset": "true",
    "skipDeviceInitialization": "true",
    "resetKeyBoard": "true",
    "waitFoeIdleTimeout": 0
}


class Test_wework:
    def setup(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", phone_info)
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_wework_Clockin(self):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/en5' and @text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                        '0)).scrollIntoView(new UiSelector().text("打卡").instance('
                                                        '0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        ele = self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/pu').text
        print(ele)
        assert ele == "外出打卡成功"

    def test_wework_jointeam(self):
        add_name = "袁不婷"
        add_num = "1008611"
        add_another_name = "沙雕"
        add_iphone_num = "13160018191"
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                               'true).instance(0)).scrollIntoView(new UiSelector('
                                                               ').text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="完整输入"]').click()
        name = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText')
        name.send_keys(add_name)
        num = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"帐号")]/../android.widget.EditText')
        num.send_keys(add_num)
        another_name = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"别名")]/../android.widget.EditText')
        another_name.send_keys(add_another_name)
        iphone_num = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]')
        iphone_num.send_keys(add_iphone_num)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                               'true).instance(0)).scrollIntoView(new UiSelector('
                                                               ').text("保存").instance(0));').click()
        ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ele
