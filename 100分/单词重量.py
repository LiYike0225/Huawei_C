# 每个句子由多个单词组成，句子中的每个单词的长度都可能不一样，我们假设每个单词的长度Ni为该单词的重量，你需要做的就是给出整个句子的平均重量V。
#保留两位浮点数result = round(num, 2)
sentence = input().split()


weight = 0

for i in range(len(sentence)):
    weight += float(len(sentence[i]))

average = round(weight/len(sentence),2)
print(average)
