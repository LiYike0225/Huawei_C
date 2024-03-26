# 请在一个字符串中找出连续最长的数字串，并返回这个数字串。
#
# 如果存在长度相同的连续数字串，返回最后一个。
#
# 如果没有符合条件的字符串，返回空字符串””。

str = input()

def isSign(ch):
    return ch == "-" or ch == "+"

def isDot(ch):
    return ch == "."

def isValidSign(SignIdx):
    nxtIdx = SignIdx + 1
    return nxtIdx < len(str) and str[nxtIdx].isdigit()

def isValidDot(DotIdx):
    prevIdx = DotIdx - 1
    nxtIdx = DotIdx + 1
    return nxtIdx < len(str) and str[prevIdx].isdigit() and str[nxtIdx].isdigit()

def getAns(l, r, ans):
    return str[l:r] if l<len(str) and r-l>=len(ans) else ans

def findStartIdx(i):
    while i <len(str):
        ch = str[i]
        if ch.isdigit() or (isSign(ch) and isValidSign(i)):
            break

        i += 1
    return i

def getResult():
    ans = ""

    dotIdx = -1
    l = findStartIdx(0)
    r = l+1

    while r<len(str):
        ch = str[r]

        if ch.isdigit():
            r +=1
        elif isSign(ch):
            ans = getAns(r, l, ans)

            if isValidSign(r):
                l = r

            else:
                l = findStartIdx(r+1)

            r = l + 1
            dotIdx =-1
        elif isDot(ch):
            ans = getAns(l, r, ans)

            if isValidDot(r):
                if dotIdx != -1:
                    l = dotIdx +1
                dotIdx = r
                r+=1
            else:
                l = findStartIdx(r+1)
                r = l+1
                dotIdx = -1
        else:
            ans =getAns(l, r, ans)
            l = findStartIdx(r+1)
            r = l+1
            dotIdx = -1

    return getAns(l,r,ans)

print(getResult())






