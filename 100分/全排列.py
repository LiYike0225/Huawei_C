# 给定一个只包含大写英文字母的字符串S，要求你给出对S重新排列的所有不相同的排列数。
# 如：S为ABA，则不同的排列有ABA、AAB、BAA三种

s = input()

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def get_result():
    total = fact(len(s))
    count = {}
    for i in s:
        if count.get(i) is None:
            count[i] =1
        else:
            count[i] += 1

    for i in count.keys():
        n = count[i]
        if n >1:
            total /= fact(n)

    return int(total)

print(get_result())