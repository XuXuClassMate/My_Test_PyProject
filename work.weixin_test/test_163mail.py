from time import sleep

import test_cofig


class Test_mailbox(test_cofig.base):
    def test_login(self):
        self.driver.get('https://mail.163.com/')
        # self.driver.find_element_by_css_selector('#switchNormalCtrl').click()
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath('//input[@data-placeholder="邮箱帐号或手机号码"]').send_keys('13609394618')
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('97461853Yxp')
        print(self.driver.find_element_by_css_selector('#dologin').text)
        sleep(5)


