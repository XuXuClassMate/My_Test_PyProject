from time import sleep
import pytest
import test_cofig


class Test_12306(test_cofig.base):
    def test_login(self):
        self.driver.get('https://www.12306.cn/index/')
        # 定位出发地，输入：北京西
        sleep(1)
        self.driver.execute_script("a=document.getElementById('fromStationText');a.value='北京西'")
        # self.driver.find_element_by_css_selector("#citem_2").click()
        fromStationText = self.driver.find_element_by_css_selector('#fromStationText').get_attribute('value')
        print(f"\n 出发地输入内容：{fromStationText}")
        if fromStationText == "北京西":
            print("出发地：北京\n 输入正常")
        else:
            print("出发地：北京\n 输入异常")
        sleep(1)
        print(self.driver.find_element_by_css_selector('#fromStationText').text)
        sleep(3)
        # 定位到达地，输入：兰州
        self.driver.execute_script("a=document.getElementById('toStationText');a.value='兰州'")
        # self.driver.find_element_by_css_selector("#citem_1").click()
        toStationText = self.driver.find_element_by_css_selector('#toStationText').get_attribute('value')
        print(f"出发到达地输入内容：{toStationText}")
        if toStationText == "兰州":
            print("到达地：兰州\n 输入正常")
        else:
            print("到达地：兰州\n 输入异常")
        # 输入出发时间
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-1-20'")
        self.driver.find_element_by_css_selector("#search_one").click()
        sleep(1)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        sleep(3)
        seat = self.driver.find_element_by_css_selector("#YW_2400000Z550O").get_attribute('value')
        print(f'硬卧二等座车票情况：{seat}')
        if seat == "有":
            self.driver.find_element_by_css_selector("#ticket_2400000Z550O_01_06 > td.no-br > a").click()
            self.driver.implicitly_wait(60)
        else:
            print("硬卧二等座车票已售完")
        sleep(5)


if __name__ == '__main__':
    pytest.main(['test_se.py', '-sq'])
