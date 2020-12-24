import pytest
import yaml

from src.test_Calculator.src.calculator import Calculator


def get_datas():
    with open('/Users/bytedance/Desktop/我的/PythonProject/My_Test_Project/src/test_Calculator/data.yml') as data_x:
        datas = yaml.safe_load(data_x)
        data = datas['datas']
        ids = datas['ids']
        return [data, ids]


datat = get_datas()


class Testcalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect", datat[0]['data_add'], ids=datat[1]['ids_add'])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', datat[0]['data_sub'], ids=datat[1]['ids_sub'])
    def test_sub(self, a, b, expect):
        assert self.calc.sub(a, b) == expect

    @pytest.mark.parametrize('a,b,expect', datat[0]['data_mul'], ids=datat[1]['ids_mul'])
    def test_mul(self, a, b, expect):
        assert self.calc.mul(a, b) == expect

    @pytest.mark.parametrize('a,b,expect', datat[0]['data_div'], ids=datat[1]['ids_div'])
    def test_div(self, a, b, expect):
        assert self.calc.div(a, b) == expect


if __name__ == '__main__':
    pytest.main('sv')
