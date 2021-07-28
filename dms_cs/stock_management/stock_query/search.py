from urllib.parse import urlencode
import requests
from dms_cs.get_token import get_token
from dms_cs.stock_management.stock_query.data_params import data_params


# 带token的headers
headers = get_token()
url = "http://10.0.15.130:31099/sales/stockQuery/getStockList"
search_params, excel_data= data_params()
params = urlencode(search_params).encode()
res = requests.get(url, headers=headers, params=params)
a = res.elapsed.microseconds/1000
print(res.json())
print(a)
# ---------------------------------------------------------------------------------
# 导出
url = "http://10.0.15.130:31099/sales/stockQuery/exportExcel"
data = urlencode(excel_data).encode()
res = requests.post(url, headers=headers, data=data)

print(res.status_code)


