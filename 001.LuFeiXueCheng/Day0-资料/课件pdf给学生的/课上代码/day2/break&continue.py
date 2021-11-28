for floor in range(1,7):
    print(f"当前在{floor}层".center(50,'-'))
    if floor == 3 :
        print("不走三层....")
        continue  # 停止本次循环，进入下次循环
    for room in range(1,10):
        if floor == 4 and room == 4:  # ALex and black girl xxoo
            print("见鬼了.....die at young....")
            exit() # 退出程序
            #break # 结束整个循环....(仅限当前一层).
        print(f"当前房间是{floor}0{room}室.")

# 标志位....
print("hahaa, still here....")