
blue_list = []
red_list = []
ball_limit = [[6,32,"red",red_list],[1,16,"blue",blue_list]]
for item in ball_limit:
    print(f"开始选{item[2]}")
    count = 0
    while count < item[0]:
        choice = input(f">>:选{item[2]}-第{count+1}个").strip()
        if not choice.isdigit():continue
        choice = int(choice)
        if choice > 0 and choice <=32:
            item[3].append(choice)
            count += 1
        else:
            print("输入的球不合法...")

print(blue_list)
print(red_list)


