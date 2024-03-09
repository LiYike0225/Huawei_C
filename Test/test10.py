# 给一个正整数列nums，一个跳数jump，及幸存数量 left。运算过程为:从索引为0的位置开始向后跳，中间跳过i个数字，命中索引为j+1的数字，该数被敲出，并从该点起跳，以此类推，直到幸存left个数为止。然后返回幸存数之和。
input_string = input()
nums, jump, left = eval(input_string)

def solution(nums, jump,left):
    idx = jump + 1
    while len(nums) > left:
        n = len(nums)

        if idx > n:
            idx = (idx%n)
            del nums[idx]
            idx += jump
        else:
            del nums[idx]
            idx+=jump
    return sum(nums)

print(solution(nums,jump,left))

