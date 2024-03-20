n = int(input())
gems = [int(input()) for _ in range(n)]
v = int(input())

def get_result():
    ans = 0
    start = 0
    end =0

    window_sum = 0
    while end<n:
        window_sum += gems[end]

        if window_sum <=v:
            end+=1
        else:
            ans = max(ans,end-start)

            flag = False

            while start < end:
                window_sum -= gems[start]
                start +=1
                if window_sum <=v:
                    end+=1
                    flag = True
                    break

            if flag:
                continue

            end+=1
            start+=1
            window_sum = 0

    if window_sum <=v:
        ans = max(ans,end-start)

    return ans

print(get_result())