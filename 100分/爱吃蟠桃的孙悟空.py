# 孙悟空爱吃蟠桃，有一天趁着蟠桃园守卫不在来偷吃。已知蟠桃园有 N 棵桃树，每颗树上都有桃子，守卫将在 H 小时后回来。
# 孙悟空可以决定他吃蟠桃的速度K（个/小时），每个小时选一颗桃树，并从树上吃掉 K 个，如果树上的桃子少于 K 个，则全部吃掉，并且这一小时剩余的时间里不再吃桃。
# 孙悟空喜欢慢慢吃，但又想在守卫回来前吃完桃子。
# 请返回孙悟空可以在 H 小时内吃掉所有桃子的最小速度 K（K为整数）。如果以任何速度都吃不完所有桃子，则返回0。
import math
peach_list = list(map(int, input().split()))
H = int(input())
#分情况讨论
#若桃树棵数N大于H，则无解，应该输出0；若N等于H，N应该等于最大的桃子数；
def check(speed):
    cost =0
    for p in peach_list:
        cost +=math.ceil(p/speed)
        if cost >H:
            return False

    return True

if len(peach_list) > H:
    print("0")
elif len(peach_list) == H:
    print(max(peach_list))
#若N小于H，ie四棵树五个小时，求最小的K,用二分法
else:
    peach_list.sort()
    left=1#K是整数，最小值为1
    right = peach_list[-1]
    ans= max(peach_list)
    while left <= right:
        mid = (right + left) >>1 #向下取整
        if check(mid):
            ans = mid
            right = mid -1
        else:
            left = mid+1
    print(ans)





