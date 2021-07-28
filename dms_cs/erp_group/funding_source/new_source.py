from urllib.parse import urlencode
import requests
from dms_cs.erp_group.funding_source.funding_source_data import new_funding_source_data
from dms_cs.get_token import get_token


# 带token的headers
headers = get_token()
# 点击新增
url = "http://10.0.15.130:31099/gms/gmsCapitalSource/getInfo"
params = {
    "sourceCode": "",
    "useMock": "false"
}
params = urlencode(params).encode()
res = requests.get(url, headers=headers, params=params)
if res.status_code == 200:
    funding_source_data = new_funding_source_data()
    data = urlencode(funding_source_data).encode()
    url = "http://10.0.15.130:31099/gms/gmsCapitalSource/save"
    res = requests.post(url, headers=headers, data=data)
    print(res.json())
    print(funding_source_data)

