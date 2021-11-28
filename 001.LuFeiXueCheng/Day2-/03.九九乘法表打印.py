for i in range(1, 10):

    for n in range(1, i+1):
        print(f'{i}x{n}={i * n}', end=' ')

    print()


# 每一行都相当于是一层楼

# 一共有9层楼，先实现方形体的楼层打印

for i in range(1, 10):      # 楼层记录，共有9层。
    for n in range(1, i+1): # 房间号记录，房间号不确定
        # 规则，有几层楼就有几个房间号。那房间号的取值范围就是（1，i+1）
        print(f'{i}x{n}={i * n}', end=' ')

    print()

