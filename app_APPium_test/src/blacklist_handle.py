from selenium.webdriver.common.by import By


def balck_handle(fun):
    balck_list = [(By.XPATH, "//*[@class='classes']")]

    def run(*args, **kwargs):
        self = args[0]

        # 捕获异常（元素没找到）
        try:
            result = fun(*args, **kwargs)
            return result
        except Exception as e:
            # 遍历黑名单（弹窗）
            for black in balck_list:
                # 如果发现黑名单中的元素存在
                eles = self.driver.find_elements(*black)
                # 对黑名单进行处理
                if len(eles) > 0:
                    # 通过点击的方式，关闭弹窗
                    eles[0].click()
                    # 再次查找元素
                    return fun(*args, **kwargs)
            raise e

    return run
