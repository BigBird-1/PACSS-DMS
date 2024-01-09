# -*- coding:utf-8 -*
# @FileName:   getData.py
# @Author:     刘峰
# @CreateTime: 2022/7/23 17:29

"""
    读取文件，并返回读取的数据
"""
import yaml, openpyxl

# 读取yaml文件的数据
def getYaml(file):
    f = open(file, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return data

# 读取Excel文件的数据
def getExcel(file):
    excel = openpyxl.load_workbook(file)
    sheet1 = excel['Sheet1']

    list1 = []
    i = 0
    keys = []
    values = []
    for line in sheet1.rows:
        if i == 0:
            keys = line
            i += 1
        else:
            if line[0].value != None:
                values.append(line)
                i += 1

    for i in range(len(values)):
        dict = {}
        for j in range(len(keys)):
            if keys[j].value != None:
                dict[keys[j].value] = values[i][j].value
        list1.append(dict)
    return list1


if __name__ == '__main__':
    # list = getExcel(r'../data/erp售后业务系统/新增车主.xlsx')
    # print(list)

    ya = getYaml(r'../data/erp售后业务系统/新增车主.yaml')
    print(ya)