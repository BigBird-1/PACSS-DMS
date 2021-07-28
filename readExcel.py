import os
import getpathInfo  # 自己定义的内部类，该类返回项目的绝对路径
from xlrd import open_workbook
from openpyxl import load_workbook
from common import Log


# 拿到该项目所在的绝对路径
path = getpathInfo.get_path()
log = Log.logger


class ReadExcel(object):

    @staticmethod
    def read_xls(xls_path, sheet_name):
        r_list = []
        try:
            file = open_workbook(xls_path)  # 打开用例Excel
            sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
            # 获取这个sheet内容行数, 列数
            n_rows = sheet.nrows
            n_cols = sheet.ncols
            for i in range(n_rows):  # 根据行数做循环
                if sheet.row_values(i)[0] != u'num':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                    r_list.append(sheet.row_values(i))
        except Exception as e:
            log.info(str(e))
        # # 获取第一行所有内容,如果括号中1就是第二行
        # keys = sheet.row_values(0)
        # # 读取单店编号/账号/密码 并保存
        # for i in range(1, nrows):
        #     eup_dict = {}
        #     for j in range(ncols):
        #         # 获取单元格数据
        #         c_cell = sheet.cell_value(i, j)
        #         # 将一行数据添加到字典中
        #         eup_dict[keys[j]] = c_cell
        #     # 将字典添加到列表中
        #     cls.append(eup_dict)

        return r_list

    @staticmethod
    def write_xls(xls_path, sheet_name, data, result, num):
        try:
            wb = load_workbook(xls_path)
            sheet = wb.get_sheet_by_name(sheet_name)  # 获得打开Excel的sheet
            sheet['D{}'.format(num)] = str(data)
            sheet['F{}'.format(num)] = result
            wb.save(xls_path)
        except Exception as e:
            log.info(str(e))

    def run_main(self, xls_name, sheet_name, data=None, result=None, num=None):
        r_list = None
        xls_path = os.path.join(path, "testFile", 'case', xls_name)  # 测试用例的路径
        if data:
            self.write_xls(xls_path, sheet_name, data, result, num)
        else:
            r_list = self.read_xls(xls_path, sheet_name)

        return r_list




