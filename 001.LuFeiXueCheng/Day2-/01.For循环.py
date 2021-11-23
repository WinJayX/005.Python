# For 循环
for i in range(10):
    print(i + 1)


# 打印0-100的奇偶数

for i in range(100):
    if i % 2 == 0:
        print(i)        # 打印偶数

for i in range(100):
    if i % 2 != 0:
        print(i)        # 打印奇数

for i in range(100):
    if i >= 50:         # 打印50以上的奇数
        if i % 2 != 0:
            print(i)


for i in range(100, 50, -1):        # 倒着取值 ，取偶数     # 顾头不顾尾
    if i >= 50:
        if i % 2 == 0:
            print(i)



# 嵌套循环
# 一橦6层的楼房，每层有9个房间，打印每个房间号。
for floor in range(1, 7):
    for room in range(1, 10):
        print(floor, 0, room)

# 老师代码

for floor in range(1, 7):
    print(f'当前是在第{floor}层'.center(50, '-'))
    for room in range(1, 10):
        print(f'当前是在{floor}0{room}室内')
print(40 * '-')


# While 循环

