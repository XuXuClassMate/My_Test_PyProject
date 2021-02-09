from selenium.webdriver.common.by import By
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

        # 修改部门名称
    def update_section(self, new_name):
        # 点击设置
        self.find(By.CSS_SELECTOR, 'ul ul li').click()
        self.find(By.CSS_SELECTOR, 'ul ul li span').click()
        # 点击修改名称
        self.find(By.XPATH, '//a[@rel="1"]').click()
        # 重新命名
        v1 = self.find(By.XPATH, '//input[@class="qui_inputText ww_inputText js_rename_input"and @name="name"]')
        v1.clear()
        v1.send_keys(new_name)
        # 点击确认
        self.find(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        # 页面刷新
        self.driver.refresh()
        return self

    def delete_section(self):
        self.find(By.CSS_SELECTOR, 'ul ul li').click()
        self.find(By.CSS_SELECTOR, 'ul ul li span').click()
        # 点击删除
        # self.find(By.XPATH, '/html/body/ul/li[7]/a').click()
        self.find(By.XPATH, '//a[@rel="3"]').click()
        self.find(By.XPATH, '//a[@d_ck="submit"]').click()
        return self

    def get_section_list(self):
        # 获取部门的文本信息
        return self.get_list(By.CSS_SELECTOR, '.jstree-container-ul a')
