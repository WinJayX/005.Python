for floor in range(1, 7):
    print(f'当前是在第{floor}层'.center(50, '-'))

    if floor == 3:
        continue        # 停止当前循环，进入下次循环。
    for room in range(1, 10):
        if room == 4 and floor == 4:
            # break       # 结束整个循环（仅限当前的循环）
            exit()    # 退出程序，结束所有循环。
        print(f'当前是在{floor}0{room}室内')


        
