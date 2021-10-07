import pytest
import requests
import allure


@allure.feature('购车建议书模块用例集')
class TestOrder(object):

    @pytest.fixture()
    def first(self):
        print("测试用例执行前执行")

    def test_save(self):
        assert 3 > 4

    @allure.description('登录token状态码验证')
    def test_query(self, get_token):
        url = "https://dms.t.hxqcgf.com/apigateway/report/salesOrderFeignUtils/searchDepositList"
        headers = {"Authorization": get_token}
        params = {"limit": 20, "offset": 0, "searchData": {}}
        res = requests.get(url, params=params, headers=headers).json()
        assert res["code"] == 200

    def test_submit(self):
        assert 3 < 4
