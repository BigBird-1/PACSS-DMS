import pytest
import requests


class TestOrder2(object):

    @pytest.fixture()
    def first(self):
        print("测试用例执行前执行")

    def test_save(self):
        assert 5 > 4

    # def test_query(self, get_token):
    #     url = "https://dms.t.hxqcgf.com/apigateway/report/salesOrderFeignUtils/searchDepositList"
    #     headers = {"Authorization": get_token}
    #     params = {"limit": 20, "offset": 0, "searchData": {}}
    #     res = requests.get(url, params=params, headers=headers).json()
    #     assert res["code"] == 200

    def test_submit(self):
        assert 3 < 4

    def test_delete(self):
        assert 7 > 6

