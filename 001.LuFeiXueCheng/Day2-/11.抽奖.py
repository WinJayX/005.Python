import random

# 生成300个员工代码
worker_list = list(range(1, 301))
# worker_list1 = [range(300)]
# # # 抽奖次数为3
count = 0
amount = [30, 6, 3]                                          # 设定中奖的数量
while count < 3:
    print(input(f'现在开始抽{3-count}等奖： '))                 # 这个思路很不错呢，而且借用count变量进行复用
    lucky = random.sample(worker_list, amount[count])        # 还有这个count
    print('中奖名单为：', lucky)                               #

    # 将中奖名单取出来，然后从员工名单中删除。
    for i in lucky:
        worker_list.remove(i)
    # worker_list.remove(lucky)
    count += 1
