# 需求 ：抽奖小程序
# 有300人。
import random
worker_list = list(range(1, 301))
# print(worker_list)

# 抽奖3 次 第一次 3等奖  30 人   # 第二次 2等奖 6人    # 第三次 1 等奖 3人
amount = [30, 6, 3]
count = 0

while count < 3:
    print(input(f'现在开始抽取{3 - count}等奖，共计{amount[count]}名，按回车键开始抽奖！'))
    luck = random.sample(worker_list, amount[count])
    print('中奖的号码是：', luck)

    for i in luck:
        worker_list.remove(i)
        # print('现在删除中奖的号码',i , end='')

    count += 1
    print()