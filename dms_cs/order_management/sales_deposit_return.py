from urllib.parse import urlencode

import requests
from dms_cs.get_token import get_token


class SalesDepositReturn(object):
    def __init__(self):
        self.headers = get_token()

    def search(self):
        url = "http://10.0.15.130:31099/sales/salesDepositReturn/list"
        params = urlencode(self.search_params()).encode()
        res = requests.get(url, headers=self.headers, params=params)
        print(res.json())

    def new(self):
        pass

    def search_params(self):
        search_data = {
            "sheetCreateDateStart": "",
            "sheetCreateDateEnd": "",
            "finishStartDate": "",
            "finishEndDate": "",
            "keyWord": ""
        }
        params = {
            "searchData": search_data,
            "limit": 10,
            "offset": 0
        }
        return params
