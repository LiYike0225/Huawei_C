# 总共有 n 个人在机房，每个人有一个标号（1<=标号<=n），他们分成了多个团队，需要你根据收到的 m 条消息判定指定的两个人是否在一个团队中，具体的：
# 消息构成为 a b c，整数 a、b 分别代表两个人的标号，整数 c 代表指令
# c == 0 代表 a 和 b 在一个团队内
# c == 1 代表需要判定 a 和 b 的关系，如果 a 和 b 是一个团队，输出一行’we are a team’,如果不是，输出一行’we are not a team’
# c 为其他值，或当前行 a 或 b 超出 1~n 的范围，输出‘da pian zi’

n,m = map(int,input().split())
msgs=[list(map(int,input().split())) for i in range(m)]
#查找一个元素所在的集合可以用并查集来实现
class UnionFindSet:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        #每个节点的父节点是自己
    def find(self,x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        return x
#合并x,y集合，通过判断x,y的父节点是否是一个来判断x，y是否在一个集合里
    def union(self,x,y):
        x_fa = self.find(x)
        y_fa = self.find(y)
        if x_fa != y_fa:
            self.fa[y_fa] =x_fa

def getResult():
    #如果第一行的m，n超过范围，输出NULL
    if n<1 or n >= 100000 or m<1 or m >= 100000:
        print("NULL")
        return

    ufs = UnionFindSet(n+1)#n+1是因为并查集从1开始更可读

    for a,b,c in msgs:
        if a<1 or a>n or b<1 or b>n:
            print("da pian zi")
            continue
        if c==0:
            ufs.union(a,b)
        elif c==1:
            if ufs.find(a)==ufs.find(b):
                print("we are a team")
            else:
                print("we are not a team")
        else:
            print("da pian zi")

getResult()



