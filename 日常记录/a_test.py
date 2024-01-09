
# import xlrd
#
#
# path = r"C:\Users\cpr264\Desktop\宝马通用事业部.xlsx"
#
# book = xlrd.open_workbook(path)
#
# table = book.sheet_by_index(0)
#
# ll = table.col_values(0)
#
# print(','.join(ll))

# import requests
#
#
# # url = "https://dms.t.hxqcgf.com/apigateway/auth/oauth/token"
# # headers = {
# #     "Authorization": "Basic c2NvOmRtcw==",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
# # }
# # params = {
# #     "entitycode": "HD340400",
# #     "username": "AG6N",
# #     "password": "LJ7LMXrU9lronyFk4qkGFw==",
# #     "isRemember": "true",
# #     "grant_type": "password"
# # }
# # res_dict = requests.get(url, headers=headers, params=params).json()
# #
# # token_type = res_dict["token_type"]
# # access_token = res_dict["access_token"]
# # # 将token放进请求头里
# # headers["Authorization"] = "{} {}".format(token_type, access_token)
# #
# # print(headers)
#
# url = "https://dms.t.hxqcgf.com/apigateway/dms-wfs/bpm/wfs/task"
# headers = {
#     "Authorization": "Bearer 70af4443-a3d7-4424-8536-4c4a0f5ec763",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
# }
#
# params = {
#             "page": 1,
#             "per_page": 15,
#             "task_name": "",
#             "task_code": "TK202005151026",
#             # "userCodeOrigin": 88880000062054
#         }
# res = requests.get(url=url, params=params, headers=headers)
#
# dd = res.json()
# print(res.json())
#
# print(dd["data"]["total"])
# -------------------------------------------------------------------------------------------------------------------------------

ss = "bearer a1d5c356-8660-41bb-9d3d-24197a265ac7"

print(ss.capitalize())






















