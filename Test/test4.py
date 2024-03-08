# 有N条线段，长度分别为a[1]-a[N]。现要求你计算这N条线段最多可以组合成几个直角三角形，每条线段只能使用一次，每个三角形包含三条线段。输入描述:第一行输入一个正整数T(1<=T<=100)，表示有T组测试数据。对于每组测试数据，接下来有T行，每行第一个正整数N，表示线段个数(3<=N<20)，接着是N个正整数，表示每条线段长度(0<a[i]<100)。
# 输出描述:对于每组测试数据输出一行，每行包括一个整数，表示最多能组合的直角三角形个数。

n = int(input())
for i in range(n):
    nums = list(map(int, input().split()))
line_num = nums[0]
nums = nums[1:]

def is_triangle(a, b, c):
    a,b,c = sorted([a,b,c])
    return a**2 + b**2 == c**2 and a !=0 and b!=0 and c!=0

def count(nums):
    result = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):#一直出现index out Of range的问题

                if is_triangle(nums[i], nums[j], nums[k]):
                    result.append((nums[i], nums[j], nums[k]))
                    nums[i],nums[j],nums[k] = 0, 0, 0

    return len(result)

print(count(nums))




