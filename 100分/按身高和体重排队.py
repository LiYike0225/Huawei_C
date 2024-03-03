# 某学校举行运动会，学生们按编号(1、2、3…n)进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列；对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。
n = int(input())
height =list(map(int,input().split()))
weight =list(map(int,input().split()))
def getResult(height,weight):
    student =[]
    for i in range(n):
        student.append([height[i],weight[i], i+1])
    student.sort(key=lambda x:(x[0],x[1],x[2]))
    return " ".join(map(lambda x:str(x[2]),student))

print(getResult(height,weight))
