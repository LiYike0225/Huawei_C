# 题目描述
# 给你一个字符串 s，首尾相连成一个环形，请你在环中找出 'o' 字符出现了偶数次最长子字符串的长度。
# 输入描述
# 输入是一个小写字母组成的字符串
# 输出描述
# 输出是一个整数

str = input()

def loop_string(str):
    n = str.count("o")
    loop_str = str*2 #looxdolxloopdolx
    right = len(str)+1
    ans = []
    for left in range(len(str)):
        if loop_str[left:right].count("o") == n-1:
            for right in range(right, len(loop_str)):
                if loop_str[left:right].count("o") == n-1:
                    ans.append(loop_str[left:right])
    ans.sort(reverse=True)
    return len(ans[0])

def getResult():
    n = str.count("o")
    if n % 2 == 0:
        return len(str)
    else:
        return loop_string(str)

print(getResult())