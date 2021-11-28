red_balls = []
blue_balls = []

li = [
    [6, 33, "红球", red_balls],
    [1, 16, "蓝球", blue_balls]
]
for item in li:
    print(f"开始选择{item[2]}".center(50, '-'))
    count = 0
    while count < item[0]:
        choice = input(f"选择第{count + 1}个{item[2]}>>:").strip()
        if not choice.isdigit():
            print("不合法的选择...")
            continue
        choice = int(choice)
        if 0 < choice < item[1] and choice not in item[3]:  # 合法的球
            item[3].append(choice)  # 动态的往每个球色的列表里加球...
            count += 1
print(red_balls)
print(blue_balls)
