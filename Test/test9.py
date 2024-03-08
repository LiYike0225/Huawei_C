# 给定一个字符串s，最多只能进行一次变换返回变换后能得到的最小字符串(按照字典序进行比较)。
#交换宇符串中任意两个不同位置的字符

s = input()

def smallest_str(s):
    s = list(s)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            swap = s[i+1]
            s[i+1] = s[0]
            s[0] =swap
            return "".join(map(str,s))
        else:
            continue
    return "".join(map(str,s))


print(smallest_str(s))