# (1+(2+3)*(3+(8+0))+1-2)这是一个简单的数学表达式,今天不是计算它的值,而是比较它的括号匹配是否正确。
# 前面这个式子可以简化为(()(()))这样的括号我们认为它是匹配正确的,
# 而((())这样的我们就说他是错误的。注意括号里面的表达式可能是错的,也可能有多个空格，对于这些我们是不用去管的，
# 我们只关心括号是否使用正确。

s = input()

def check_brackets(s):
    stack =[]
    count =0
    for c in s:
        if c != '(' and c != ')':
            continue
        elif c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return -1
            else:
                stack.pop()
                count += 1
    if len(stack) > 0:#若遍历字符串之后还存在（，则输出-1
        return -1
    else:
        return count

print(check_brackets(s))


