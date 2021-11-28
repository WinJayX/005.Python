

days = 11
i = 1
while days > 1:
    i = i * 2 + 2                   # +2 也可以计算出正确的结果，但+2 没有明显的条件规律
#     i = (i + 1) * 2               # 这个地方应该是剩下的先加1再乘以2 （+1 是多吃掉的那个，乘以2 得出上一天有多少个）
    print(i)
    days -= 1




count = 1                                       # 1.计数器;也是要循环的变量。
sum = 0                                         # 2.最终结果容器
while count <= 100:                             # 3.当这个变量小于=100时
    if count % 2 == 1:                          # 4.如果这个变量是奇数
        sum += count  # sum = sum + count       # 5.容器结果就是所有的奇数相加的和
    else:
        sum -= count                            # 6.否则容器结果就是偶数相减的和
    count += 1
    print(sum)
