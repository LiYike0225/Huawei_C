# 华为商城举办了一个促销活动，如果某顾客是某一秒内最早时刻下单的顾客（可能是多个人），则可以获取免单。
# 请你编程计算有多少顾客可以获取免单。

n = int(input())
book_time = [input() for _ in range(n)]

def result():
    book_time.sort(reverse=True)
    stack =[book_time.pop()]
    while len(book_time)>0:
        time = book_time.pop()
        top = stack[-1]
        if top == time or top[:19] != time[:19]:
            stack.append(time)

    return len(stack)

print(result())