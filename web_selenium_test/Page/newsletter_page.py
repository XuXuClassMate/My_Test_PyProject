from selenium.webdriver.common.by import By
import re

from web_selenium_test.Page.Base_page import BasePage


class NewsLetterPage(BasePage):
    def add_member(self):
        pass

    def add_section(self, test_name):
        # 点击添加部门
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        # 添加部门，开始命名
        self.find(By.XPATH, '//input[@name="name"]').send_keys(test_name)
        # 选择部门
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.qui_dialog_body [id="1688854046128733_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        self.driver.refresh()
        return self

    def get_list(self):
        """
        获取通讯录页面的信息
        :return:
        """
        section = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-container-ul a')
        section_name = []
        for name in section:
            section_name.append(name.text)

        return section_name
