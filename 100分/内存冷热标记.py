# 输入描述
# 第一行输入为 N，表示访存序列的记录条数，0 < N ≤ 10000。
# 第二行为访存序列，空格分隔的 N 个内存页框号，页面号范围 0 ~ 65535，同一个页框号可能重复出现，出现的次数即为对应框号的频次。
# 第三行为热内存的频次阈值 T，正整数范围 1 ≤ T ≤ 10000。
# 输出描述
# 第一行输出标记为热内存的内存页个数，如果没有被标记的热内存页，则输出 0 。
# 如果第一行 > 0，则接下来按照访问频次降序输出内存页框号，一行一个，频次一样的页框号，页框号小的排前面。

n = int(input())
seq = list(map(int, input().split()))
max_time = int(input())

count ={}
for i in seq:
    if count.get(i) is None:
        count[i] = 1
    else:
        count[i] += 1

ans = []
pages = 0
for key in count.keys():
    if count[key] >= max_time:
        pages +=1
        ans.append(key)

ans.sort()

if len(ans) == 0:
    print(pages)
else:
    print(len(ans))
    for i in ans:
        print(i)


