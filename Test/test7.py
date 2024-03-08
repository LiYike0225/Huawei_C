# 字符串s首尾相连成一个环形，请你在环中找出0'字符出现了偶数次最长子字符串的长度。
s = input()

def circular_string(s):
    count = s.count('o')-1
    substr = []
    ans =[]
    right = len(s)
    left = 0
    n=len(s)*2
    while right < n:
        substr.append(s[left:right])
        left +=1
        right += 1
    for sub in substr:
        if sub.count('o') == count:
            ans.append(sub)
    ans = sorted(ans,key=lambda x:(len(x)),reverse=True)
    ans_str = ans[0]
    for ch in s:
        if ch != 'o':
            ans_str += ch
        else:
            break
    return len(ans_str)


def get_len(s):
    count = s.count('o')
    if count%2 == 0:
        return len(s)
    else:
        return circular_string(s)

print(get_len(s))