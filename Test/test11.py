#堆内存分配问题，按照自己的思路写了一遍

malloc_size = int(input())
used_memory =[0]*100

def malloc():
    if malloc_size>100 or malloc_size<0:
        return -1

    offset_list = []

    while True:
        try:
            offset,size = map(int, input().split())
            offset_list.append(offset+size)
            for i in range(offset, offset+size):
                used_memory[i] = 1
        except:
            break

    free_offset ={}
    zero_count =[]
    count = 0
    for used in used_memory:
        if used == 1:
            if count >0:
                zero_count.append(count)
                count =0
        else:
            count+=1

    zero_count.append(count)

    for i in range(len(zero_count)):
        idx = offset_list[i]
        free_offset[idx] = zero_count[i]

    free_offset = dict(sorted(free_offset.items()))

    first_free = next(iter(free_offset))
    diff_list ={}
    for items in free_offset:
        if free_offset[items] <malloc_size:
            pass
        else:
            diff = free_offset[items] - malloc_size
            diff_list[items] = diff

    return first_free

print(malloc())



