import pytest


@pytest.fixture(scope='module')
def prints():
    print('\n【开始计算】')
    yield
    print('\n【计算结束】')


