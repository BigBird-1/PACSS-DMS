import pytest
import os
import allure


@allure.feature("这是测试类")
class TestA(object):

    def setup(self):
        print("执行测试用例前会先执行此方法")

    def teardown(self):
        print('执行完测试用例后会执行此方法')

    @classmethod
    def setup_class(cls):
        print("执行测试套件前会先执行此方法")

    @classmethod
    def teardown_class(cls):
        print('执行完测试套件后会执行此方法')

    @staticmethod
    def fun(num):
        return num+1

    @allure.description("这是测试用例描述")
    def test_a(self):
        assert self.fun(5) > 7

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_b(self):
        assert 3 == 5

    @pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
    def test_c(self):
        assert 8 > 7

    def test_d(self):
        assert 9 < 10

    # @allure.step
    # def simple_step(self, step_param1):
    #     assert step_param1 > 3000

    @pytest.mark.parametrize('param1', [4399, 2012])
    def test_parameter(self, param1):
        assert param1 > 3000
        # self.simple_step(param1)

    @pytest.mark.parametrize("params1", ['aa', 'BBB'])
    @pytest.mark.parametrize("params2", ['AAA', 'BBB'])
    def test_params(self, params1, params2):
        print("1: {} 2: {}".format(params1, params2))
        assert params1 == params2


if __name__ == '__main__':
    # pytest.main(['--alluredir', './result', 'test_class.py'])
    os.system("pytest -s test_class.py --alluredir=result/json_report")
    os.system('allure generate result/json_report -o result2/html/ --clean')

