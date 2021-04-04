import allure
import pytest
import yaml

from test_Calculator.src.calculator import Calculator


def get_datas():
    with open('/Users/bytedance/Desktop/My/PythonProject/My_Test_Project/'
              'test_Calculator/testing/data.yml') as data_x:
        datas = yaml.safe_load(data_x)
        data = datas['datas']
        ids = datas['ids']
        return [data, ids]


datat = get_datas()


@allure.feature("测试方法")
class Testcalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    #  使用参数化
    @allure.story('测试加法')
    @pytest.mark.parametrize("a,b,expect", datat[0]['data_add'], ids=datat[1]['ids_add'])
    # 测试add函数
    def test_add(self, a, b, expect):
        try:
            with allure.step('赋值运算'):
                # 调用add函数,返回的结果保存在result里面
                result = self.calc.add(a, b)
        except Exception as e:
            # Exception 全部的错误
            print(e)
        else:
            with allure.step('结果验证'):
                # 判断result结果是否等于期望的值
                assert result == expect

    @allure.story('测试减法')
    @pytest.mark.parametrize('a,b,expect', datat[0]['data_sub'], ids=datat[1]['ids_sub'])
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    @allure.story('测试乘法')
    @pytest.mark.parametrize('a,b,expect', datat[0]['data_mul'], ids=datat[1]['ids_mul'])
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @allure.story('测试除法')
    @pytest.mark.parametrize('a,b,expect', datat[0]['data_div'], ids=datat[1]['ids_div'])
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect


if __name__ == '__main__':
    pytest.main('test_cal.py', '-v')

"""
---生成报告---
pytest test_cal.py --alluredir=./retule/5

---查看测试报告----
allure serve ./result/5
"""
