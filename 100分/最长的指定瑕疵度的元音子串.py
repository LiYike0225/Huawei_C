flaw_num = int(input())
str = input().lower()
vowels = 'aeiou'
def getResult():
    idxes =[]

    for i in range(len(str)):
        if str[i] in vowels:
            idxes.append(i)

    ans = 0
    l = 0
    r = 0
    while r<len(idxes):
        diff = idxes[r] - idxes[l] -(r-l)
        if diff > flaw_num:
            l +=1
        elif diff < flaw_num:
            r +=1
        else:
            ans = max(ans, idxes[r]-idxes[l]+1)
            r +=1

    return ans

print(getResult())