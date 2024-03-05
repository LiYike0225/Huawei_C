# 有一个总空间为100字节的堆，现要从中新申请一块内存，内存分配原则为：优先紧接着前一块已使用内存，分配空间足够且最接近申请大小的空闲内存。

class Memory:
    def __init__(self, offset, size):
        self.offset = offset  # 内存块起始位置
        self.size = size  # 内存块大小


# 输入获取
malloc_size = int(input())  # 要申请的内存大小

used_memory = []  # 已占用的内存
while True:
    try:
        offset, size = map(int, input().split())
        used_memory.append(Memory(offset, size))
    except:
        break


# 算法入口
def getResult():
    # 申请的内存大小非法，则返回-1
    if malloc_size <= 0 or malloc_size > 100:
        return -1

    # 记录最优的申请内存起始位置
    malloc_offset = -1
    # 记录最接近申请内存的空闲内存块大小
    min_malloc_size = 100

    # 对占用的内存按照起始位置升序
    used_memory.sort(key=lambda x: x.offset)

    # 记录（相对于已占用内存的前面一个）空闲内存块的起始位置
    free_offset = 0

    for used in used_memory:
        # 如果占用的内存起始位置 小于 前面一个空闲内存块起始位置，则存在占用内存区域重叠
        # 如果占用的内存起始位置 大于 99，则非法
        if used.offset < free_offset or used.offset > 99:
            return -1

        # 如果占用的内存的大小少于0，则非法
        # 如果占用的内存的大小超过该内存起始位置往后所能申请到的最大内存大小，则无效
        if used.size <= 0 or used.size > 100 - used.offset:
            return -1

        # 空闲内存块地址范围是：free_offset ~ memory.offset - 1
        if used.offset > free_offset:
            # 空闲内存块大小
            free_memory_size = used.offset - free_offset

            # 如果该空闲内存块大小足够，且最接近申请的内存大小
            if malloc_size <= free_memory_size < min_malloc_size:
                malloc_offset = free_offset
                min_malloc_size = free_memory_size

        # 更新：空闲内存的起始位置 = （当前占用内存的结束位置 + 1） = （当前占用内存的起始位置 + 占用大小）
        free_offset = used.offset + used.size

    # 收尾
    last_free_memory_size = 100 - free_offset
    if malloc_size <= last_free_memory_size < min_malloc_size:
        malloc_offset = free_offset

    return malloc_offset


# 算法调用
print(getResult())





