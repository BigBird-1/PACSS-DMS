import pandas as pd
import numpy as np


# Series数据结构
# 1.创建Series数组
# s1 = pd.Series([1, 2, 3, 4, 5])
# print('s1: {}'.format(s1))
# 2.设置index参数
s2 = pd.Series([1, 2, 3, 4, 5], index=['第一', '第二', '第三', '第四', '第五'])
print('s2: {}'.format(s2))
# 3.Series的索引和切片
print('s2索引: {}'.format(s2.index))
print('s2数值: {}'.format(s2.values))
# 根据索引修改数值
s2["第二"] = 10
print("s2中 第二 对应的数值：{}".format(s2['第二']))
# Series还可以索引多个数值
print("s2中 第二第四第五 对应的数值：{}".format(s2[['第二', '第四', '第五']]))
# 注意：这里的切片与Python中的切片是不一样的，Series的切片末端元素是包含在内的，所以末端元素仍然可以被输出
print("s2中 第二到第五 对应的数值：{}".format(s2['第二':'第五']))
# 4.字典类型创建Series
s3 = pd.Series({'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5})
print('s3: {}'.format(s3))
s4 = pd.Series(s3, index=['first', 'second', 'fourth', 'third', 'fifth', 'tenth'])
print('s4: {}'.format(s4))
# in not in
print('ss' in s3)
print('ss' not in s3)
# 判断缺失值
print(s4.isnull())
print(s4.notnull())
# 算术运算
print(s3 + s4)
print("---------------------------------------------------------------------------------------------------------------")
# DataFrame数据结构
# 创建DataFrame
df_dic = {"color": ["red", "yellow", "blue", "purple", "pink"], "size": ["medium", "small", "big", "medium", "small"], "taste": ["sweet", "sour", "salty", "sweet", "spicy"]}
df = pd.DataFrame(df_dic)
print(df)
# 指定顺序
df1 = pd.DataFrame(df_dic, columns=['taste', 'size', 'color'])
print(df1)
df2 = pd.DataFrame(df_dic, columns=['taste', 'size', 'color', 'yang'])
print(df2)
# 获取数值    注意：数组元素之间都没有逗号
print(df1.values)
print(df1.color)
print(df1['color'])
# DataFrame的表头可以设置列索引名称的标题和行索引名称的标题，需要使用name函数进行设置。
df1.index.name = 'sample'
df1.columns.name = 'feature'
print(df1)
# 获取第三行数据
print(df1.loc[3])

df1['category'] = np.arange(5)
print(df1)

df1['jack'] = pd.Series([2, 4, 6], index=[0, 2, 4])
print(df1)

# 数学与统计计算
df5 = pd.DataFrame([[1, 4, 7, 7], [2, 5, 8, 8], [3, 6, 9, 9], [9, 5, 4, 8]], index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three', 'four'])
print(df5)
# 按列求和
print(df5.sum())
# 按行求和    设定axis = 1将进行行求和。不设定默认列求和
print(df5.sum(axis=1))
print('从上到下累计求和： {}'.format(df5.cumsum()))
print('从左往右累计求和： {}'.format(df5.cumsum(axis=1)))

print(df5.mean())        # 列均值
print(df5.median())     # 列中位数
print(df5.count())        # 列非缺失值数量
print(df5.max())          # 列最大最小值
print(df5.min())
print(df5.describe())    # 列汇总统计
print(df5.var())       # 方差
print(df5.std())       # 标准差
print(df5.skew())   # 偏度
print(df5.kurt())     # 峰度
print(df5.diff)         # 一阶差分
print(df5.cummax())   # 累计最大值、累计最小值
print(df5.cummin())
print(df5.cumsum())   # 累计和、累计积
print(df5.cumprod())
print(df5.cov())         # 协方差、相关系数
print(df5.corr())











