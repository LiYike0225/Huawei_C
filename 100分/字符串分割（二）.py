# 给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。
# 对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；
# 反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。

k = int(input())
s = input()

ans =""

def convert_case(sub):
    upper_count = sum(1 for ch in sub if ch.isupper())
    lower_count = sum(1 for ch in sub if ch.islower())

    if lower_count > upper_count:
        return sub.lower()
    elif upper_count > lower_count:
        return sub.upper()
    else:
        return sub

def getResult():
    ans =[]
    arr = s.split("-")
    ans.append(convert_case(arr[0]))
    new_str = "".join(arr[1:])
    for i in range(0,len(new_str),k):
        substr = new_str[i:i+k]
        ans.append(convert_case(substr))


    return "-".join(ans)

print(getResult())


