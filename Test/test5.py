nums = list(map(int, input().split()))
left_product_dict ={}
right_product_dict ={}

def left_product(nums):
    prod = [1]*(len(nums))
    prod[1] = nums[0]
    for i in range(1,len(nums)):
        prod[i] = prod[i-1] * nums[i-1]
        left_product_dict[i] =prod[i]
    return left_product_dict

def right_product(nums):
    nums = nums[::-1]
    prod = [1]*(len(nums))
    prod[1] = nums[0]
    for i in range(1,len(nums)):
        prod[i] = prod[i-1] * nums[i-1]
        right_product_dict[i] =prod[i]
    return right_product_dict

def find_common_value(left_product_dict, right_product_dict):
    common_keys = []
    for i in left_product_dict.keys():
        if left_product_dict[i] in right_product_dict.values():
            common_keys.append(i)
    common_keys.sort()
    return common_keys[0]

print(find_common_value(left_product(nums), right_product(nums)))