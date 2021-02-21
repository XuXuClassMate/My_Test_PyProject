import pytest
from app_APPium_test.src.Mian import Main


class Test_ADDMenber:
    main = Main()

    def test_addmember(self):
        result = self.main.go_to_Address_book().go_to_add_member().go_to_Manual_add().add_name("张三").add_another_name(
            "not") \
            .add_iphone_num("13609394617").complete()
        res = result.get_add_Toast()
        assert res == "添加成功"

    if __name__ == '__main__':
        pytest.main(test_addmember())
