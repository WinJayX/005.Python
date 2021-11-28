
n = 1
day = 11
while day > 1:
    n = (n + 1) * 2 # 上一天吃之前的桃子数量
    day -= 1
    print(day,n)