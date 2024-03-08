# 给定一个字符串s，s包含以空格分隔的若干个单词，请对s进行如下处理后输出
# 1.单词内部调整:对每个单词字母重新按字典序排序;2.单词间顺序调整:
# 1)统计每个单词出现的次数，并按次数降序排列
# 2)次数相同时，按单词长度升序排列
# 3)次数和单词长度均相同时，按字典序升序排列请输出处理后的字符串，每个单词以一个空格分隔。
# 输入描述:一行字符串，每个字符取值范围:[a-zA-Z0-9]以及空格，字符串长度范围:[,1000]

s = input().split()
words = [''.join(sorted(word))for word in s]
word_count ={}

def getresult():
    for word in words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], len(x[0]), x[0]))
    ans =[]
    for i, j in sorted_word_count:
        [ans.append(i) for _ in range(j)]

    return " ".join(map(str,ans))

print(getresult())


