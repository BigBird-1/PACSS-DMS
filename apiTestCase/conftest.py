import pytest
import requests


@pytest.fixture(scope="session")
def get_token():
    headers = {
        "Authorization": "Basic c2NvOmRtcw==",
        # "Authorization": "Bearer f47351dc-7804-4511-91d9-18e675be47ac",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    }
    params = {
        "username": "AFQZ",
        "password": "Dxv+ilzJncHFspBFjLvxzw==",
        "entitycode": "HD340400",
        "isRemember": "true",
        "grant_type": "password"
    }
    url = "https://dms.t.hxqcgf.com/apigateway/auth/oauth/token"
    res = requests.get(url, headers=headers, params=params).json()
    token_type = res["token_type"]
    access_token = res["access_token"]
    # 将token放进请求头里
    token = "{} {}".format(token_type, access_token)

    headers["Authorization"] = "{} {}".format(token_type, access_token)

    return token
