# 有一种简易压缩算法：针对全部由小写英文字母组成的字符串，将其中连续超过两个相同字母的部分压缩为连续个数加该字母，其他部分保持原样不变。
# 例如：字符串“aaabbccccd”经过压缩成为字符串“3abb4cd”。
# 请您编写解压函数，根据输入的字符串，判断其是否为合法压缩过的字符串，
# 若输入合法则输出解压缩后的字符串，否则输出字符串“!error”来报告错误。

import re

str = input()

def zip(src):
    src += "-"

    ans = []
    stack =[]
    repeat =0 #用于记录字符出现的次数
    for c in src:
        if len(stack) == 0:
            stack.append(c)
            repeat += 1
            continue

        top = stack[-1]
        if top == c:
            repeat +=1
            continue

        if repeat>2:
            ans.append(f"{repeat}{top}")
        else:
            ans.append("".join([top] * repeat))

        stack.clear()
        stack.append(c)
        repeat =1

    return "".join(ans)

def getResult():
    back_s = str
    if re.search(r"[^a-z0-9]", back_s) is not None:
        return "!error"

    reg = re.compile(r"(\d+)([a-z])?")

    while True:
        match = reg.match(back_s)

        if match is None:
            break

        src = match.group()
        repeat_times = int(match.group(1))

        if repeat_times <=2:
            return "!error"

        repeat_content = match.group(2)

        if repeat_content is None:
            return "!error"

        tar = "".join([repeat_content]*repeat_times)
        back_s = back_s.replace(src,tar,1)

    if zip(back_s) != str:
        return "!error"
    else:
        return back_s


getResult()
print(getResult())