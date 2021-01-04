"""
1、case顺序：加-除-减-乘
2、fixture方法在case前打印【开始计算】，结束后打印【计算结束】
3、fixture方法存在在conftest.py，设置scope=module
4、控制case只执行顺序为：加-减-乘-除
5、结合allure生成本地测试报告
"""
import allure
import pytest
import yaml
from test_Calculator.src.calculator import Calculator


@allure.story('获取数据')
def get_data():
    with allure.step('解析data.yaml文件'):
        with open('data.yml') as data_x:
            datas = yaml.safe_load(data_x)
            data_data = datas['datas']
            data_name = datas['ids']
            return [data_data, data_name]


data = get_data()

get_cal = Calculator()


class Test_Calculator:
    @pytest.mark.run(order=0)
    @pytest.mark.usefixtures("prints")
    @pytest.mark.parametrize("a, b, result", data[0]['data_add'], ids=data[1]['ids_add'])
    def test_add(self, a, b, result):
        assert get_cal.add(a, b) == result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, result", data[0]['data_div'], ids=data[1]['ids_div'])
    def test_div(self, a, b, result):
        assert get_cal.div(a, b) == result

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, result", data[0]['data_sub'], ids=data[1]['ids_sub'])
    def test_sub(self, a, b, result):
        assert get_cal.sub(a, b) == result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, result", data[0]['data_mul'], ids=data[1]['ids_mul'])
    def test_mul(self, a, b, result):
        assert get_cal.mul(a, b) == result


if __name__ == '__main__':
    pytest.main('test_cal_plus.py', '-vs')

