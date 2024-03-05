# 向一个空栈中依次存入正整数，假设入栈元素 n(1<=n<=2^31-1)按顺序依次为 nx…n4、 n3、n2、 n1, 每当元素入栈时，如果 n1=n2+…+ny(y 的范围[2,x]， 1<=x<=1000)，则 n1~ny 全部元素出栈，重新入栈新元素 m(m=2*n1)。
# 如：依次向栈存入 6、 1、 2、 3, 当存入 6、 1、 2 时，栈底至栈顶依次为[6、 1、 2]；当存入 3时， 3=2+1， 3、 2、 1 全部出栈，重新入栈元素 6(6=2*3)，此时栈中有元素 6；
# 因为 6=6，所以两个 6 全部出栈，存入 12，最终栈中只剩一个元素 12

nums = list(map(int,input().split()))

def push(num,stack):
    total = num
    # 访问栈顶-1处的元素，并且逐步减一直到访问到序号为零的位置
    for i in range(len(stack)-1,-1,-1):
        total -= stack[i]
        if total == 0:
            del stack[i:]#此时是向前遍历的，所以可以理解为删除i之前的所有元素
            push(num*2, stack) #递归，将num替换为num*2
            return
        elif total < 0:
            break

    stack.append(num)#循环结束后将得到的num入栈

def result():
    stack = [nums[0]]
    for i in range(1, len(nums)):#i的范围是1-len（nums-1）
        push(nums[i],stack)

    stack.reverse()

    return " ".join(map(str,stack))

print(result())






