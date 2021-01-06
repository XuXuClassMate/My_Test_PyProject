import json
from time import sleep
import test_cofig


class Test_weixin(test_cofig.base):
    def test_login(self):
        # 登录企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 读取cookie
        try:
            with open('cookie.json', 'r') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # 页面刷新
            self.driver.refresh()
            # 登陆成功，点击客户关系tab
            self.driver.find_element_by_css_selector('#menu_customer > span').click()
        except:
            # cookie失效等待60秒，人工扫码时间为60秒
            self.driver.implicitly_wait(60)
            self.driver.find_element_by_css_selector('#menu_customer > span').click()
        # 获取页面cookie
        cookie = self.driver.get_cookies()
        # 写入/更新cookie
        with open('cookie.json', 'w') as f:
            json.dump(cookie, f)

        sleep(5)
