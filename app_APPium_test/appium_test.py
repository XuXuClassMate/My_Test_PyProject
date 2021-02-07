from time import sleep

from appium import webdriver
phone_info = {
    "platformName": "android",
    "platformVersion": "8.1",
    "deviceName": "S4F6R19C18016391",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", phone_info)
# driver.implicitly_wait(10)
# driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
# el1 = driver.find_element_by_id('com.xueqiu.android:id/search_input_text')
# el1.send_keys('阿里巴巴')
# el2 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
#                                    '.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
#                                    '.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android'
#                                    '.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget'
#                                    '.RecyclerView/android.widget.RelativeLayout['
#                                    '3]/android.widget.LinearLayout/android.widget.TextView[1]')
# el2.click()
# sleep(5)
driver.quit()
