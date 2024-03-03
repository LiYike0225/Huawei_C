# 五张牌，每张牌由牌大小和花色组成，牌大小2~10、J、Q、K、A，牌花色为红桃、黑桃、梅花、方块四种花色之一。
# 判断牌型:
# 牌型1，同花顺：同一花色的顺子，如红桃2红桃3红桃4红桃5红桃6。
# 牌型2，四条：四张相同数字 + 单张，如红桃A黑桃A梅花A方块A + 黑桃K。
# 牌型3，葫芦：三张相同数字 + 一对，如红桃5黑桃5梅花5 + 方块9梅花9。
# 牌型4，同花：同一花色，如方块3方块7方块10方块J方块Q。
# 牌型5，顺子：花色不一样的顺子，如红桃2黑桃3红桃4红桃5方块6。
# 牌型6，三条：三张相同+两张单

# 输入由5行组成，每行为一张牌大小和花色，牌大小为2~10、J、Q、K、A，花色分别用字符H、S、C、D表示红桃、黑桃、梅花、方块。

#判断顺序：同花顺->四条->葫芦->三条

arr =[input().split() for _ in range(int(5))]
nums = []
colors = []
for num, color in arr:
    nums.append(num)
    colors.append(color)


#首先处理jqka
def cards(num):
    if num == "J":
        return 11
    elif num == "Q":
        return 12
    elif num == "K":
        return 13
    elif num == "A":
        return 14
    else:
        return int(num)

nums.sort(key=lambda num: cards(num))

def countNums(nums,part_count, max_same_num_count):
    count = {}
    for num in nums:#数相同的数字有多少个
        if count.get(num) is None:
            count[num] = 0
        count[num] += 1

    #例如：三条有三个部分，对应的len(count.key())数量应该为3
    if len(count.keys()) != part_count:
        return False
    max_same_num_count = max(count.values())
    return max_same_num_count

def is_santiao(nums):
    return countNums(nums,3,3)

def is_sitiao(nums):
    return countNums(nums, 2,4)

def is_hulu(nums):
    return countNums(nums,2,3)

def is_tonghua(colors):
    if len(set(colors)) ==1:
        return True
    else:
        return False

def is_shunzi(nums):

    if "".join(nums) == "234A":
        return True

    for i in range(1,len(nums)):
        if cards(nums[i-1])+1 != cards(nums[i]):
            return False
    return True

def result():

    if is_shunzi(nums) and is_tonghua(colors):
        return 1

    elif is_sitiao(nums):
        return 2

    elif is_hulu(nums):
        return 3

    elif is_tonghua(colors):
        return 4

    elif is_shunzi(nums):

        return 5

    elif is_santiao(nums):
        return 6

    else:
        return 0

print(result())
