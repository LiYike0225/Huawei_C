# 给定一个字符串s，最多只能进行一次变换，返回变换后能得到的最小字符串（按照字典序进行比较）。
#
# 变换规则：交换字符串中任意两个不同位置的字符。

str = input()
minStr = "".join(sorted(str))

def getResult(str):
    if str == minStr:
        return str

    s_arr = list(str)
    min_arr = list(minStr)

    for i in range(len(str)):
        if str[i] != minStr[i]:
            tmp = str[i]
            s_arr[i] = min_arr[i]
            swap_index = str.rindex(minStr[i])
            s_arr[swap_index] = tmp
            break
    return "".join(s_arr)
print(getResult(str))

