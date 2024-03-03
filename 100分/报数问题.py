#约瑟夫环问题
#迭代公式：n是人数，m是报数：josephus(n)=(josephuse(n-1)+m)%n
def josephus(n):
    if n == 1:
        return 0
    else:
        return (3+josephus(n-1))%n

n = int(input())
print(int(josephus(n))+1)
