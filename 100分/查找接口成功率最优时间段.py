# 服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示，
# 数组中每个元素都是单位时间内失败率数值，数组中的数值为0~100的整数，
# 给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值，即平均失败率小于等于minAverageLost，
# 找出数组中最长时间段，如果未找到则直接返回NULL

min_average_lost = int(input())
arr = list(map(int, input().split()))

def calculate_average():
    n = len(arr)
    prefix_sum = [0]*(n+1)
    for i in range(1,n+1):#修改下标
        prefix_sum[i] = prefix_sum[i-1] +arr[i-1]
    ans= []
    maxlen =0
    for i in range(n):#区间（i，j-1）
        for j in range(i+1,n+1):
            interval_sum = prefix_sum[j]-prefix_sum[i]
            length = j-i
            lost = length * min_average_lost

            if interval_sum <= lost:
                if length > maxlen:
                    ans =[[i, j-1]]
                    maxlen = length
                elif length == maxlen:
                    ans.append([i, j-1])

    ans.sort(key=lambda x: x[0])

    if len(ans)==0:
        return "NULL"
    else:
        return " ".join(map(lambda x: "-".join(map(str,x)),ans))

print(calculate_average())


