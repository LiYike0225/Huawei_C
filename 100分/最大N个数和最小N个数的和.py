# # 给定一个数组，编写一个函数来计算它的最大N个数与最小N个数的和。你需要对数组进行去重。
# 数组中数字范围[0, 1000]
# 最大N个数与最小N个数不能有重叠，如有重叠，输入非法返回-1
# 输入非法返回-1

m = int(input())
arr = list(map(int, input().split()))
n = int(input())

arr.sort()

def getResult():

    if arr[-n] == arr[n]:
        return -1
    else:

        return sum(arr[:n])+sum(arr[-n:])

print(getResult())