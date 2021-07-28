from urllib.parse import urlencode
from dms_cs.get_token import get_token
from dms_cs.data_generate.brand_data import new_brand_data
import requests


# 带token的headers
headers = get_token()


# 新增品牌-保存
url = "http://10.0.15.130:31099/gms/gmsBrand/save"
# 构建请求数据
brand_data = new_brand_data()
data = urlencode(brand_data).encode()  # 暂不清楚为啥要这样编码就可以传
res = requests.post(url, headers=headers, data=data)
print(res.json())
# 列表查询
url = "http://10.0.15.130:31099/gms/gmsBrand/list"
# 准备查询条件
search_data = {
    "brandKeywords": brand_data["data"]["brandCode"]
}
# 准备查询参数
params = {
    "limit": 10,
    "offset": 0,
    "searchData": search_data,
    "useMock": "false"
}
params = urlencode(params).encode("utf-8")
res = requests.get(url, headers=headers, params=params)
print(res.content.decode())

