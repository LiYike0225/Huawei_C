# 部门在进行需求开发时需要进行人力安排。
# 当前部门需要完成 N 个需求，需求用 requirements 表述，requirements[i] 表示第 i 个需求的工作量大小，单位：人月。
# 这部分需求需要在 M 个月内完成开发，进行人力安排后每个月人力时固定的。
# 目前要求每个月最多有2个需求开发，并且每个月需要完成的需求不能超过部门人力。
# 请帮助部门评估在满足需求开发进度的情况下，每个月需要的最小人力是多少？
import math
M = int(input())
N = sorted(map(int, input().split()))
#二分法可以参考悟空那题，只不过最大量变成了最小的两个工作量相加
def check(M,N):
    min_requirement = int(N[-1])
    max_requirement = int(N[0] + N[1])#每个月至多有两个项目开发
    ans = max_requirement
    while min_requirement <= max_requirement:
        mid = (max_requirement + min_requirement) >>1
        cost = 0
        for n in N:
            cost += math.ceil(n/mid)
        if cost >= M:
            min_requirement =mid +1
        else:
            max_requirement = mid -1
            ans = mid
    return ans

print(check(M,N))


