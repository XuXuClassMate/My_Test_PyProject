from selenium.webdriver.common.by import By

from web_selenium_test.Page.Base_page import BasePage
from web_selenium_test.Page.newsletter_page import NewsLetterPage


class MainPage(BasePage):
    def goto_section(self):
        # 点击通讯录页面
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        self.driver.refresh()
        return NewsLetterPage(self.driver)

