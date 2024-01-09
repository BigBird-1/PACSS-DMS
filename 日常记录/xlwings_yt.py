import xlwings as xw


app = xw.App(visible=False, add_book=False)

print(xw.apps.keys())
# 连接到工作簿
wb = app.books.open(r"F:\PACSS-DMS\日常记录\flow_file\复制审核流用.xls")
# wb = xw.Book(r"F:\PACSS-DMS\日常记录\flow_file\复制审核流用.xls")
# 打开工作表  索引或者表名
sheet1 = wb.sheets[0]
# sheet1 = wb.sheets['Sheet1']

# 获取sheet1工作表里的行数，列数
n_rows = sheet1.used_range.last_cell.row
n_cols = sheet1.used_range.last_cell.column
print(n_rows, n_cols)
# 读取第x行数据
value = sheet1.range("A1").expand("right").value
print(value)
# 在Range内读取/写入值非常简单：
# 存储单个数据
# sheet1.range('A3').value = '重大事项'
# 存储单行数据
# sheet1.range('A4').value = ['id', '姓名', '年龄']
# 存储多行数据
# sheet1.range('A5').value = [['1', '2', '3'], ['4', '5', '6']]
# print(sheet1.range('A3').value)
# 保存
# wb.save()

a_list = []

for i in range(2, n_rows+1):
    a_dict = {}
    for j in range(1, n_cols+1):
        # 获取i行j列的数据
        v = sheet1.range(i, j).value
        print(i, j, v)

        a_dict[value[j-1]] = v

    a_list.append(a_dict)


print(a_list)

# 关闭
wb.close()
# 退出Excel
app.quit()






