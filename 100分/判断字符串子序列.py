# 给定字符串 target和 source，判断 target是否为 source 的子序列。
# 你可以认为target和 source 中仅包含英文小写字母。
# 字符串 source 可能会很长（长度~=500,000），而 target是个短字符串（长度<=100)。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
# （例如，”abc”是”aebycd”的一个子序列，而”ayb”不是）。
# 请找出最后一个子序列的起始位置。

target = input()
source = input()

def getResult():
    cursor = len(target) -1
    for i in range(len(source)-1, -1, -1):
        if source[i] == target[cursor]:
            cursor -= 1
            if cursor < 0:
                return i

    return -1

print(getResult())


