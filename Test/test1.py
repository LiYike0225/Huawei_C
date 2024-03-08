# 题目描述:对于任意两个正整数A和B，定义他们之间的差异值和相似值:
# 差异值:A、B转换成二进制后，对于二进制的每一位，对应位置的bit值不相同则为1，否则为0。
# 相似值:A、B转换成二进制后，对于二进制的每一位，对应位置的bit值都为1则为1，否则为0。
# 现在有n个正整数 A0到A(n-1)，问有多少对(i,j)(0<=i<j<n)，Ai和 Aj的差异值大于相似值。假设A=5,B=3;则A的二进制表示101;B的二进制表示011;则A与B的差异值二进制为110;相似值二进制为 001;A与B的差异值十进制等于6，相似值十进制等于1，满足条件。输入描述:输入:一个n接下来n个正整数
# 数据范围:1<=n<=10^5,1<=A[i]<2^30输出描述:输出:满足差异值大于相似值的对数

n = int(input())
nums = list(map(int,input().split()))

def diff_similarilty(a,b):
    diff = 0
    similarity = 0
    while a>0 or b>0:
        bit_a = a & 1
        bit_b = b & 1
        if bit_a != bit_b:
            diff +=1
        if bit_a == bit_b ==1:
            similarity += 1
        a >>= 1
        b >>= 1
    return diff, similarity

def count_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, n):
            diff, similarity = diff_similarilty(nums[i],nums[j])
            if diff > similarity:
                count += 1
    return count

print(count_pairs(nums))


