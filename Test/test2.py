# 小明正在规划一个大型数据中心机房，为了使得机柜上的机器都能正常满负荷工作，需要确保在每个机柜边上至少要有一个电箱。为了简化题目，
# 假设这个机房是一整排，M表示机柜，I表示间隔，请你返回这整排机柜，至少需要多少个电表箱。如果无解请返回-1。

cabinets = input()

def check_electricity(s):
    M_num = s.count('M')
    I_num = s.count('I')
    stack =[]
    #三个M至少需要两个I
    if M_num-1 > I_num:
        return -1
    if s == 'M' :
        return -1
    if M_num ==0:
        return 0
    for i in range(len(s)):
        if s[i] == 'I':
            stack.append(s[i])
            if i > 0 and s[i-1] == 'M' or s[i+1] == 'M':
                stack.pop()
            else:
                return -1

    return (I_num - len(stack))

print(check_electricity(cabinets))