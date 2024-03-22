# 给定一个数组，里面有 6 个整数，求这个数组能够表示的最大 24 进制的时间是多少，输出这个时间，无法表示输出 invalid
# 输入描述
# 输入为一个整数数组，数组内有六个整数。
#
# 输入整数数组长度为 6，不需要考虑其它长度，元素值为 0 或者正整数，6 个数字每个数字只能使用一次。
#输出为一个 24 进制格式的时间，或者字符串”invalid“。

import re

arr = eval(input())

p = re.compile("(([01][0-9])|([2][0-3]))([0-5][0-9])([0-5][0-9])")

def dfs(arr, used, path, res):
    if len(path) == len(arr):
        tmp = "".join(map(str,path))
        if p.search(tmp):
            res.append(path[:])
        return

    for i in range(len(arr)):
        if not used[i]:
            path.append(arr[i])
            used[i] = True
            dfs(arr, used, path, res)
            used[i]= False
            path.pop()

def getResult():
    res = []
    dfs(arr, [False]*len(arr), [], res)

    if len(res) == 0:
        return "invalid"

    res.sort()
    t = res[-1]

    return f"{t[0]}{t[1]}:{t[2]}{t[3]}:{t[4]}{t[5]}"

print(getResult())