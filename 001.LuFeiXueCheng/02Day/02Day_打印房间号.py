#嵌套循环

for i in range(1,6):
    if i == 3:
        continue        #结束本次循环。
    print(f"------第{i}层--------")

    for j in range(1,9):
        if i == 4 and j == 4:
            break       #结束当前循环。外面的大循环还会继续。
        print(f"==L{i}-{i}0{j}室==")
