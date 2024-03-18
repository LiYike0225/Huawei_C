# 给定一个从小到大的有序整数序列（存在正整数和负整数）数组 nums ，请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为最小值，并返回这个绝对值。
# 每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

import sys
nums = list(map(int,input().split()))

def absolute(a,b):
    return abs(a+b)

minV = sys.maxsize

ans = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        a = nums[i]
        b = nums[j]
        ans.append(absolute(a,b))

print(min(ans))

