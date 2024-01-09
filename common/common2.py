from math import radians, cos, sin, asin, sqrt
from geopy.distance import geodesic


# 公式计算两点间距离（m）

def geodistance(lng1, lat1, lng2, lat2):
    # lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance / 1000, 3)
    return distance

    # 返回 446.721 千米

# 调用geopy包中的方法
print(geodesic((22.537046, 114.058992), (30.472123, 114.338239)).m)  # 计算两个坐标直线距离
print(geodesic((22.537046, 114.058992), (30.472123, 114.338239)).km)  # 计算两个坐标直线距离
# 返回 447.2497993542003 千米

# 南昌：华东交通大学（120.12802999999997,30.28708）
# 杭州：浙江工商大学（115.86572000000001,28.7427）
# 用百度地图测量结果：447.02km

print(geodistance(114.058992, 22.537046, 114.338239, 30.472123))
