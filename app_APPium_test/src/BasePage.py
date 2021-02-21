from appium import webdriver
from appium.webdriver.webdriver import WebDriver

phone_info = {
    "platformName": "android",
    "platformVersion": "8.1",
    "deviceName": "S4F6R19C18016391",
    "appPackage": "com.tencent.wework",
    "appActivity": ".launch.LaunchSplashActivity t9",
    "noReset": "true",
    "dontStopAppOnReset": "true",
    "skipDeviceInitialization": "true",
    "resetKeyBoard": "true",
    "waitFoeIdleTimeout": 0
}


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", phone_info)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
