# 特定大小的停车场，数组cars[]表示，其中1表示有车，0表示没车。
# 车辆大小不一，小车占一个车位（长度1），货车占两个车位（长度2），卡车占三个车位（长度3）。
# 统计停车场最少可以停多少辆车，返回具体的数目

#replace方法的用法
cars = input().replace(",","")
cars = cars.replace("111","x").replace("11","x").replace("1","x")

print(cars.count("x"))