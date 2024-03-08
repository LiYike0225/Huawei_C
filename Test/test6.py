# 题目描述:寿司店周年庆，正在举办优惠活动回馈新老客户。
# 寿司转盘上总共有n盈寿司，prices门是第i盘寿司的价格，如果客户选择了第:盘寿司，寿司店免费赠送客户距离第(流寿司最近的下一盘寿司j，前提是 pricest]
# <prices的]，如果没有满足条件的i，则不赠送寿司每个价格的寿司都可无限供应输入描述:输入的每一个数字代表每盘寿司的价格，每盘寿司的价格之间使用空格分隔

sushi = list(map(int, input().split()))

def idx_of_sushi(sushi):
    idx_dict = {}
    idx = 0
    for sushi in sushi:
        idx_dict[sushi] = idx
        idx += 1
    return idx_dict

def prices(sushi):
    price_list = sorted(sushi, reverse=True)
    price_sum_dict = {}
    for i in range(len(price_list)):
        sum_list = set(price_list[i:])
        price_sum = sum(sum_list)
        price_sum_dict[price_list[i]] = price_sum

    return price_sum_dict

def get_price(sushi):
    prices_sum_dict = prices(sushi)
    idx_dict = idx_of_sushi(sushi)
    result = []
    for i in idx_dict.keys():
        result.append(prices_sum_dict[i])
    return " ".join(map(str,result))

print(get_price(sushi))

#存在寿司价格一致所产生的bug

