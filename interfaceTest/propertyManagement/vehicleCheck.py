from common.configHttp import http_r
from interfaceTest.constants import car_inventory_urls
from common import Log


log = Log.logger


class CarInventory(object):
    def __init__(self):
        pass

    @staticmethod
    def new():
        res = http_r.run_main('post', url=car_inventory_urls["新增盘点单"], name="新增盘点单")

        inventory_no = res["data"]["inventoryNo"]

        log.info("新增盘点单-新建成功-单号: {}".format(inventory_no))

        return inventory_no

    @staticmethod
    def difference_inventory(inventory_no):
        params = {"inventoryNo": inventory_no}

        res = http_r.run_main('get', url=car_inventory_urls["差异情况说明-查看"], data=params, name="差异情况说明-查看")
        losses_list = res["data"]["lossesList"]
        y_t = {}
        for i in losses_list:
            y_t[str(i["itemId"])] = "盘点差异说明-测试"

        data = {
           "vehInventoryExplainJson": {"id": {"inventoryNo": inventory_no}, "cerReceiptExplain": "1",
                                       "shippingAmountExplain": "1", "shippingCountExplain": "1", "toolkitExplain": "1",
                                       "factoryShippingAmount": 0,  "factoryShippingCount": 0,
                                       "financialKeyExplain": "1", "salesKeyExplain": "1"},
           "paramsMap": y_t
        }

        res = http_r.run_main('post', url=car_inventory_urls["差异情况说明-保存"], data=data, name="差异情况说明-保存")

        print(res)


car_inventory = CarInventory()

if __name__ == '__main__':
    num = car_inventory.new()
    car_inventory.difference_inventory("")


