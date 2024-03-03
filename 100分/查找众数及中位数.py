# 众数是指一组数据中出现次数量多的那个数，众数可以是多个。
# 中位数是指把一组数据从小到大排列，最中间的那个数，如果这组数据的个数是奇数，那最中间那个就是中位数，如果这组数据的个数为偶数，那就把中间的两个数之和除以2，所得的结果就是中位数。
# 查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数。

old_arr = sorted(map(int,input().split()))
new_arr = []
count = {}
for i in old_arr:
    count[i] = old_arr.count(i)
max_count = max(count.values())
for k in count:
    if count[k] == max_count:
        new_arr.append(int(k))
mid =len(new_arr)//2
if len(new_arr)%2 == 0:
    print((new_arr[mid]+new_arr[mid-1])//2)
else:
    print(new_arr[mid])
