import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.DataFrame({'数据序号': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],  '厂商编号': ['001', '001', '001', '002', '002', '002', '003', '003', '003', '004', '004', '004'], '产品类型': ['AAA', 'BBB', 'CCC', 'AAA', 'BBB', 'CCC', 'AAA', 'BBB', 'CCC', 'AAA', 'BBB', 'CCC'], 'A属性值': [40, 70, 60, 75, 90, 82, 73, 99, 125, 105, 137, 120], 'B属性值': [24, 36, 52, 32, 49, 68, 77, 90, 74, 88, 98, 99], 'C属性值': [30, 36, 55, 46, 68, 77, 72, 89, 99, 90, 115, 101]})
print(df1)

# 设置背景风格
# sns.set()
# sns.set_style("darkgrid")  # 灰色背景
# sns.set_style("whitegrid")
# sns.set_style("dark")
# sns.set_style("white")
# sns.set_style("ticks")

# 使用matplotlib设置字体-黑体
# plt.rcParams['font.sans-serif'] = ['SimHei']

# 边框   sns.despine()方法
# 移除顶部和右部边框，只保留左边框和下边框
# sns.despine()
# 使两个坐标轴相隔一段距离（以10长度为例）
# sns.despine(offet=10,trim=True)
# 移除左边框
# sns.despine(left=True)
# 移除指定边框 （以只保留底部边框为例）
# sns.despine(fig=None, ax=None, top=True, right=True, left=True, bottom=False, offset=None, trim=False)

# 绘制散点图
# 使用seaborn库 绘制散点图，可以使用replot()方法，也可以使用scatter()方法。
# replot方法的参数kind默认是’scatter’，表示绘制散点图。
# hue参数表示 在该一维度上，用颜色区分
# ①对A属性值和数据序号绘制散点图，红色散点，灰色网格，保留左、下边框
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['SimHei']
# sns.relplot(x='数据序号', y='A属性值', data=df1, color='red')
# plt.show()
# ②对A属性值和数据序号绘制散点图，散点根据产品类型的不同显示不同的颜色，
# 白色网格，左、下边框：
# sns.set_style('whitegrid')
# plt.rcParams['font.sans-serif'] = ['SimHei']
# sns.relplot(x='数据序号', y='A属性值', data=df1, hue='产品类型')
# plt.show()
# ③将A属性、B属性、C属性三个字段的值用不同的样式绘制在同一张图上（绘制散点图），x轴数据是[0,2,4,6,8…]
# ticks风格（四个方向的框线都要），字体使用楷体
# sns.set_style('ticks')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# df2 = df1.copy()
# df2.index = list(range(0, len(df2)*2, 2))
# dfs = [df2['A属性值'], df2['B属性值'], df2['C属性值']]
# sns.scatterplot(data=dfs)
# plt.show()

# 绘制 折线图
# 使用seaborn库绘制折线图， 可以使用replot()方法，也可以使用lineplot()方法。
# sns.replot()默认绘制的是散点图，绘制折线图只需吧参数kind改为"line"。
# ①需求：绘制A属性值与数据序号的折线图，灰色网格，全局字体为楷体；并调整标题、两轴标签 的字体大小，以及坐标系与画布边缘的距离（设置该距离是因为字体没有显示完全）
# sns.set(rc={'font.sans-serif': 'STKAITI'})
# sns.relplot(x='数据序号', y='A属性值', data=df1, color='purple', kind='line')
# plt.title('绘制折线图', fontsize=18)
# plt.xlabel('num', fontsize=18)
# plt.ylabel('A属性值', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()
# ②需求：绘制不同产品类型的A属性折线（三条线一张图），whitegrid风格，字体楷体。
# sns.set_style('whitegrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# sns.relplot(x='数据序号', y='A属性值', data=df1, hue='产品类型', kind='line')
# plt.title('绘制折线图', fontsize=18)
# plt.xlabel('num', fontsize=18)
# plt.ylabel('A属性值', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()
# ③需求：将A属性、B属性、C属性三个字段的值用不同的样式绘制在同一张图上（绘制折线图），x轴数据是[0,2,4,6,8…]
# darkgrid风格（四个方向的框线都要），字体使用楷体，并加入x轴标签，y轴标签和标题。边缘距离合适。
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# df2 = df1.copy()
# df2.index = list(range(0, len(df2)*2, 2))
# dfs = [df2['A属性值'], df2['B属性值'], df2['C属性值']]
# sns.relplot(data=dfs, kind='line')
# plt.title('绘制折线图', fontsize=18)
# plt.xlabel('num', fontsize=18)
# plt.ylabel('A属性值', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()
# ③多重子图
# 横向多重子图 col
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# sns.relplot(data=df1, x='A属性值', y='B属性值', kind='line', col='厂商编号')
# plt.subplots_adjust(left=0.05, right=0.95, bottom=0.1, top=0.9)
# plt.show()
# 纵向多重子图 row
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# sns.relplot(data=df1, x='A属性值', y='B属性值', kind='line', row='厂商编号')
# plt.subplots_adjust(left=0.05, right=0.95, bottom=0.1, top=0.9)
# plt.show()
# 使用lineplot()方法绘制折线图，其他细节基本同上，示例代码如下
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# sns.lineplot(data=df1, x='数据序号', y='A属性值', color='purple')
# plt.xlabel('num', fontsize=18)
# plt.ylabel('A属性值', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()

# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# df2 = df1.copy()
# df2.index = list(range(0, len(df2)*2, 2))
# dfs = [df2['A属性值'], df2['B属性值'], df2['C属性值']]
# sns.lineplot(data=dfs)
# plt.title('绘制折线图', fontsize=18)
# plt.xlabel('num', fontsize=18)
# plt.ylabel('A属性值', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()

# 绘制直方图使用的是sns.displot()方法
# bins=6 表示 分成六个区间绘图
# rug=True 表示在x轴上显示观测的小细条
# kde=True表示显示核密度曲线
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# sns.displot(bins=6, rug=True, kde=True, data=df1[['C属性值']])
# plt.title('直方图', fontsize=18)
# plt.xlabel('C属性值', fontsize=18)
# plt.ylabel('数量', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()
# 随机生成300个正态分布数据，并绘制直方图，显示核密度曲线
# sns.set_style('darkgrid')
# plt.rcParams['font.sans-serif'] = ['STKAITI']
# np.random.seed(13)
# Y = np.random.randn(300)
# sns.displot(Y, bins=9, rug=True, kde=True)
# plt.title('直方图', fontsize=18)
# plt.xlabel('C属性值', fontsize=18)
# plt.ylabel('数量', fontsize=16)
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)
# plt.show()
# 绘制条形图使用的是barplot()方法
# 以产品类型 字段数据作为x轴数据，A属性值数据作为y轴数据。按照厂商编号字段的不同进行分类。
# 具体如下：
sns.set_style('darkgrid')
plt.rcParams['font.sans-serif'] = ['STKAITI']
sns.barplot(x="产品类型", y="A属性值", hue="厂商编号", data=df1)
plt.title("条形图", fontsize=18)
plt.xlabel("产品类型", fontsize=18)
plt.ylabel("数量", fontsize=16)
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
plt.show()



