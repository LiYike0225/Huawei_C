# 题目描述
# 现有一字符串仅由 ‘(‘，’)’，'{‘，’}’，'[‘，’]’六种括号组成。
# 若字符串满足以下条件之一，则为无效字符串：
# ①任一类型的左右括号数量不相等；
# ②存在未按正确顺序（先左后右）闭合的括号。
# 输出括号的最大嵌套深度，若字符串无效则输出0。
# 0≤字符串长度≤100000
# 输入描述
# 一个只包括 ‘(‘，’)’，'{‘，’}’，'[‘，’]’的字符串
# 输出描述
# 一个整数，最大的括号深度

str = input()

def getResult():
    map = {"}":"{", ")":"(","]":"["}

    stack = []

    max_depth = 0

    for i in range(len(str)):
        ch = str[i]
        if len(stack) >0 and map.get(ch) is not None and map[ch] == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
            max_depth = max(max_depth, len(stack))
    if len(stack)>0:
        return 0

    return max_depth

print(getResult())


