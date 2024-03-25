# 2012伦敦奥运会即将到来，大家都非常关注奖牌榜的情况，现在我们假设奖牌榜的排名规则如下:
#
# 首先gold medal数量多的排在前面
# 其次silver medal数量多的排在前面
# 然后bronze medal数量多的排在前面
# 若以上三个条件仍无法区分名次，则以国家名称的字典顺序排定。
# 我们假设国家名称不超过二十个字符，各类奖牌数不超过100，且大于0.
#
n = int(input())
countries =[]

for i in range(n):
    name, gold, silver, bronze = input().split()
    countries.append([int(gold), int(silver), int(bronze), name])

    countries.sort(key=lambda x: (-x[0],-x[1],-x[2],x[3]))

for c in countries:
    print(c[3])