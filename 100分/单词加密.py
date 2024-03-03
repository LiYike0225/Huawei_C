#输入句子，单词中有元音的话用‘*’代替，如果没有的话单词收尾字母互换
#输出换了之后的新句子

sentence = input().split()
list = "aeuioAEUIO"
result =''
for i in range(len(sentence)):
    word = sentence[i]
    new_word =''
    for ch in word:
        if ch in list:
            new_word += '*'
        else:
            new_word += ch
    for ch in new_word:
        if new_word.count('*')==0:
            new_word = new_word[-1]+ new_word[1:-1] + new_word[0]
    result += new_word + ' '

print(result)
