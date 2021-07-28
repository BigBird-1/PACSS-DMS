from urllib.parse import urlencode

import requests

from dms_cs.get_token import get_token
from dms_cs.stock_management.shipping_notify.shipping_car_data import new_shipping_car


# 带token的headers
headers = get_token()
url = "http://10.0.15.130:31099/sales/shippingNotify/saveShippingNotify"
new_data, search_params, excel_data = new_shipping_car()
new_data = urlencode(new_data).encode()
res = requests.post(url, headers=headers, data=new_data)

print(res.json())
# ---------------------------------------------------------------------------------------------------------
# 查询
url = "http://10.0.15.130:31099/sales/shippingNotify/getShippingNotifyList"
search_params = urlencode(search_params).encode()
res = requests.get(url, headers=headers, params=search_params)

print(res.json())
# ----------------------------------------------------------------------------------------------------------
# 编辑

# -----------------------------------------------------------------------------------------------------------
# 导出
url = "http://10.0.15.130:31099/sales/shippingNotify/exportExcel"
excel_data = urlencode(excel_data).encode()
res = requests.post(url, headers=headers, data=excel_data)

# print(res.json())

