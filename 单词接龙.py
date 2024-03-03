# 单词接龙的规则是：
# 可用于接龙的单词首字母必须要前一个单词的尾字母相同；
# 当存在多个首字母相同的单词时，取长度最长的单词，如果长度也相等，则取字典序最小的单词；已经参与接龙的单词不能重复使用。
# 现给定一组全部由小写字母组成单词数组，并指定其中的一个单词作为起始单词，进行单词接龙，
# # 请输出最长的单词串，单词串是单词拼接而成，中间没有空格。
idx = int(input())
n = int(input())
words = [input() for _ in range(n)]

def getresult():
    chain = [words.pop(idx)]
    prefix ={}

    for word in words:#按首字母分类创建索引
        ch = word[0]
        if prefix.get(ch) is None:
            prefix[ch]=[]
        prefix[ch].append(word)

    for ch in prefix.keys():
        prefix[ch].sort(key = lambda x:(-len(x),[ord(i) for i in x]))
    while True:
        tail = chain[-1][-1]
        if prefix.get(tail):
            chain.append(prefix[tail].pop(0))#加上新词把旧词弹出

        else:
            break

    return "".join(chain)

print(getresult())