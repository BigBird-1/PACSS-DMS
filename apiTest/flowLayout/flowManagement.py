import time
from common.configHttp import http_r
from apiTest.initialization import initial
from apiTest.constants import oa_urls
from common import Log


class FlowManagement(object):
    def __init__(self):
        pass

    def query(self):
        pass

    def copy(self):
        params = {
            "task_code": "TK202203031001",
            "task_version": 14,
            "userCodeOrigin": 88880000060506
        }

        res = http_r.run_main('get', url=oa_urls["流程复制"], data=params, name="流程复制")
        print(res)


flow_management = FlowManagement()

if __name__ == '__main__':
    flow_management.copy()




























