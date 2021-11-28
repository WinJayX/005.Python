
red_balls = []
blue_balls = []

count = 0
while count < 6:
    choice = input(f"输入第{count+1}个红球>:").strip()
    if not choice.isdigit(): #
        print("不合法")
        continue
    choice = int(choice)
    if 0 < choice <= 33 and choice not in red_balls:
        red_balls.append(choice)
        count += 1

count = 0
while count < 1:
    choice = input(f"输入第{count+1}个blue球>:").strip()
    if not choice.isdigit(): #
        print("不合法")
        continue
    choice = int(choice)
    if 0 < choice <= 16 and choice not in blue_balls:
        blue_balls.append(choice)
        count += 1


print(red_balls,blue_balls)






