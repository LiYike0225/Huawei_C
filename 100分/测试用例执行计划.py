# 某个产品当前迭代周期内有 N 个特性（F1,F2,......FN）需要进行覆盖测试，每个特性都被评估了对应的优先级，特性使用其 ID 作为下标进行标识
# 设计了 M 个测试用例（T1,T2,......,TM），每个测试用例对应一个覆盖特性的集合，测试用例使用其 ID 作为下标进行标识，测试用例的优先级定义为其覆盖的特性的优先级之和。
# 在开展测试之前，需要制定测试用例的执行顺序，规则为：优先级大的用例先执行，如果存在优先级相同的用例，用例 ID 小的先执行。
n, m = map(int,input().split())

features = [0]*(n+1)#创建一个列表 初始值为0，（n+1）可以使特性的编号从1开始
for i in range(1,n+1):
    features[i] = int(input())
case =[]
for i in range(1,m+1):
    priority = sum(map(lambda x: features[int(x)], input().split()))
    case.append([priority,i])

case.sort(key=lambda x: (-x[0],x[1]))

for priority,index in case:
    print(index)
