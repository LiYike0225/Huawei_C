# 现有两组服务器A和B，每组有多个算力不同的CPU，其中 A[i] 是 A 组第 i 个CPU的运算能力，B[i] 是 B组 第 i 个CPU的运算能力。
# 一组服务器的总算力是各CPU的算力之和。
# 为了让两组服务器的算力相等，允许从每组各选出一个CPU进行一次交换，
# 求两组服务器中，用于交换的CPU的算力，并且要求从A组服务器中选出的CPU，算力尽可能小。
while True:
    try:
        l1, l2 = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        #half_diff法 b-a = (sumB-sumA)/2
        #所以可以遍历listA中的a来找b，其中a要尽可能小
        half_diff = abs((sum(B) - sum(A)))//2
        ans = {}
        if sum(A)<sum(B):
            for a in A:
                if a+half_diff in B:
                    ans[a] = a + half_diff
        else:
            for a in A:
                if a-half_diff in B:
                    ans[a] = a - half_diff
        min_A = min(ans.keys())
        min_B = ans[min_A]
        print(min_A, min_B)
    except:
        break
