# 某个产品的RESTful API集合部署在服务器集群的多个节点上，近期对客户端访问日志进行了采集，需要统计各个API的访问频次，根据热点信息在服务器节点之间做负载均衡，现在需要实现热点信息统计查询功能。
# RESTful API是由多个层级构成，层级之间使用 / 连接，如 /A/B/C/D 这个地址，A属于第一级，B属于第二级，C属于第三级，D属于第四级。
# 现在负载均衡模块需要知道给定层级上某个名字出现的频次，未出现过用0表示，实现这个功能。
#第一个input是日志条数 第二个是分级api，第三个是层级和对应层级中查询的关键字
n = int(input()) #查询日志条数
cnts =[]
for i in range(n):
    url = input().split("/")

    for level in range(len(url)):
        urlComponent  = url[level]
        #如果不存在对应层级
        if level >= len(cnts):
            #创建对应层级
            cnts.append({})
        #获取对应层级
        cnts[level][urlComponent] = cnts[level].get(urlComponent,0) + 1

#输入要查询的层级和关键字
tar_level, tar_urlComponent = input().split()

if int(tar_level)>=len(cnts):
    print(0)
else:
    print(cnts[int(tar_level)].get(tar_urlComponent,0))



