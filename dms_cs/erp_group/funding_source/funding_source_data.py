from dms_cs.data_generate.random_name import make_name
import random
import string


def new_funding_source_data():
    # 资金来源代码1-4位大写字母，数字随机组合
    # 随机生成1到4位包含大写字母数字的代码
    i = random.randint(1, 4)
    funding_source_code = ''.join(random.sample(string.ascii_uppercase + string.digits, i))
    # 随机2-4位资金来源名称
    source_name = make_name() + "测试"
    # 优先顺序1-8位数
    sort_order = str(random.randint(1, 99999999))
    data = {
            "data": {"sourceCode": funding_source_code,
                     "sourceName": source_name,
                     "sortOrder": sort_order,
                     "id":{"sourceCode": funding_source_code}},
            "useMock": "false",
            "isNew": "1"
    }
    return data

