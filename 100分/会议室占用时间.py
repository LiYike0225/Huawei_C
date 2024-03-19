# 输入描述
# 第一行输入一个整数 n，表示会议数量
# 之后输入n行，每行两个整数，以空格分隔，分别表示会议开始时间，会议结束时间
# 输出描述
# 输出多行，每个两个整数，以空格分隔，分别表示会议室占用时间段开始和结束

def merge(time):
    time.sort(key=lambda x: x[0])

    ans =[]
    pre = time[0]
    for i in range(1, len(time)):
        cur = time[i]
        if cur[0] <= pre[1]:
            pre[1] = max(pre[1], cur[1])
        else:
            ans.append(pre)
            pre = cur
    ans.append(pre)
    return ans

n = int(input())
room_time = []
for i in range(n):
    room_time.append(list(map(int, input().split())))

for start, end in merge(room_time):
    print(f"{start} {end}")

