# 数轴×有两个点的序列 A={A1， A2, …, Am}和 B={B1, B2, ..., Bn}， Ai 和 Bj 均为正整数， A、 B 已经从小到大排好序，
# A、 B 均肯定不为空，
# 给定一个距离 R（正整数），列出同时满足如下条件的所有（Ai， Bj）数对
# Ai <= Bj
# Ai,Bj 距离小于等于 R，但如果 Ai 找不到 R 范围内的 Bj，则列出距它最近的 1 个 Bj，当然此种情况仍然要满足 1，

import re

#输入获取
tmp = re.compile(r"A=\{(.+)},B=\{(.+)},R=(.+)").search(input())
#正则表达式 r"A=\{(.+)},B=\{(.+)},R=(.+)" 匹配的是形如 "A={...},B={...},R=..." 的字符串格式
#.+ 表示匹配任意字符（除换行符外）至少一次
#提取匹配的数据并用map转换成一个整数列表
A = list(map(int,tmp.group(1).split(",")))
B = list(map(int,tmp.group(2).split(",")))
R = int(tmp.group(3))

def getResult():
    ans = []

    for a in A:
        count = 0 #count是指b是第一个满足条件的b
        for b in B:
            if b<a:
                continue #表示该数对不满足条件，跳过

            if b - a <= R or count == 0: #若ab之间距离小于r或是第一个b
                ans.append(f"({a},{b})")#格式化字符串，允许字符串中插入变量的值
                count += 1
            else:
                break
    return "".join(ans) #使用空字符串 "" 作为分隔符，将 ans 中的所有字符串连接起来

print(getResult())