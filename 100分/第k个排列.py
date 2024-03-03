# 给定参数n，从1到n会有n个整数：1,2,3,…,n,这n个数字共有n!种排列。
# 按大小顺序升序列出所有排列的情况，并一一标记，
# 当n=3时,所有排列如下:
# “123” “132” “213” “231” “312” “321”
# 给定n和k，返回第k个排列

n = int(input())
k = int(input())
arr = [i+1 for i in range(n)]

fact = [0]*(n+1)
fact[1] =1
for i in range(2,n+1):
    fact[i] = fact[i-1] * i

def result(n,k,arr):
    if n == 1:
        return 1

    res = []

    while True:
        prefix = arr[(k-1)//fact[n-1]]#可以确定排序是由什么开头的
        res.append(str(prefix))

        k = k % fact[n-1]
        if k ==0:
            k = fact[n-1]
        arr = list(filter(lambda x: x != prefix,arr))
        n-=1
        if k == 1:
            res.append("".join(map(str,arr)))
            break
    return "".join(res)


print(result(n,k,arr))

