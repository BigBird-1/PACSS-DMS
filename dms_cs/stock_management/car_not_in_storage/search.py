from urllib.parse import urlencode
import requests
from dms_cs.get_token import get_token
from dms_cs.stock_management.car_not_in_storage.data_params import data_params


# 带token的headers
headers = get_token()
url = "http://10.0.15.130:31099/sales/carNotInStorage/list"
search_params, excel_data = data_params()
params = urlencode(search_params).encode()
res = requests.get(url, headers=headers, params=params)

print(res.json())
# ---------------------------------------------------------------------------------
# 导出
url = "http://10.0.15.130:31099/sales/carNotInStorage/exportExcel"
data = urlencode(excel_data).encode()
res = requests.post(url, headers=headers, data=data)

print(res.status_code)
