import random, requests
import string
from decimal import Decimal

# a = "100000.27"
# b = round(random.uniform(0, 1), 2)
# print(b)
# print(str(b))
# print(str(round(random.uniform(0, 1), 2)))
#
# c = float(a)/(1 + b)
# print(c)
# print(Decimal(c).quantize(Decimal('0.00')))
# print(type(Decimal(c).quantize(Decimal('0.00'))))
# b = 660000.50
# print(Decimal(b).quantize(Decimal('0.00')))
# print(str(Decimal(b).quantize(Decimal('0.00'))))
# print(str(Decimal(round(random.uniform(0, 1), 2)).quantize(Decimal('0.00'))))
# purchase_price = Decimal(660000).quantize(Decimal('0.00'))
# tax = Decimal(round(random.uniform(0, 1), 2)).quantize(Decimal('0.00'))
# no_tax_vehicle_cost = Decimal(purchase_price/(1 + tax)).quantize(Decimal('0.00'))
# tax_amount = Decimal(purchase_price - purchase_price/(1+tax)).quantize(Decimal('0.00'))
# print(purchase_price, tax, no_tax_vehicle_cost, tax_amount)
# --------------------------------------------------------------------------
# 导入time模块
# import time
# # 优化格式化化版本
# print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
# print(type(time.strftime('%Y-%m-%d',time.localtime(time.time()))))
# -------------------------------------------------------------------------------
# with open("./1.png", "w", encoding='utf-8') as f:
#
#     f.write(res.content.decode())
# --------------------------------------------------------------------------------------
# vin = ''.join(random.sample(string.ascii_uppercase + string.digits, 17))
# print(string.ascii_uppercase)
# print(string.digits)
# print(random.sample(string.ascii_uppercase + string.digits, 17))
# print(vin)
# print(''.join(['S', 'K', 'T', '5', 'G', '8', 'C', 'E', '3', '7', '2', '6', 'J', 'Z', 'V', 'D', 'Q']))
# -------------------------------------------------------------------------------
# a = "asfsafsdfdsf"
# print(type("a".join(a)))
# print("a".join(a))
# ------------------------------------------------------------------------
# import hashlib
# test = '123456'#待加密信息
# m = hashlib.md5()#创建md5对象
# # 注意最好不要直接写m.update(test),若出现中文会报错，为了保证不报错最好加上编码格式
# m.update(test.encode())
# result = m.digest()
# print('加密前:', test)
# print('加密后:', result)
# import base64
#
# a = base64.b16encode(result)
# print(a.decode())  # b'aGVsbG8gd29ybGQ='


def md5(str1):
    import hashlib
    import base64
    print(str1)
    m = hashlib.md5()
    m.update(str1.encode())

    md5str = m.digest()

    b64str = base64.b64encode(md5str)
    return b64str


print(md5("123456"))

# import hashlib, base64
#
# str2 = "SFSGZ6DoiQ5HcN0uXJBU1g=="
#
# b = base64.b64decode(str2)




