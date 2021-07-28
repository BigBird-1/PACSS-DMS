from decimal import Decimal
from dms_cs.data_generate.random_name import make_name
import random
import string


def new_brand_data():
    # 随机生成1到30位包含大写字母数字的品牌代码
    i = random.randint(1, 30)
    brand_code = ''.join(random.sample(string.ascii_uppercase + string.digits, i))
    # 随机2-4位汉字品牌名称
    brand_name = make_name()
    # 积分系数0-3之间并保留两位小数
    coefficient = Decimal(round(random.uniform(0, 3), 2)).quantize(Decimal('0.00'))
    data = {
            "data": {"brandCode": '',  # 品牌代码*
                     "brandName": brand_name,  # 品牌名称*
                     "coefficient": str(coefficient),  # 积分系数*
                     "isSale": 12781001 or 12781002,  # 是否销售可用
                     "isAfterSale": 12781001 or 12781002,  # 是否售后可用
                     "id": {"brandCode": ''},
                     "vendorCode": "CSBM-CS2020",  # 厂家编码
                     "vendorName": "厂家名称-测试名称2020",  # 厂商名称
                     "enableStdLabour": 12781001 or 12781002,  # 开启工时标准化
                     "facRepairType": "厂家维修类型-测试类型2020"},  # 厂家维修类型
            "useMock": "false",
            "isNew": "1"
    }
    return data

