
count = 0
black_girl_age = 25
while count < 3:
    guess = input("猜黑姑娘的年龄>:")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("不识别的指令,重新输入...")
        continue
    if guess > black_girl_age:
        print("猜大了，往小了试...")
    elif guess < black_girl_age:
        print("往大了试...")
    else:
        print("恭喜你猜对了， 黑姑娘送你一晚/..///")
        break
    count += 1
    if count == 3:
        cmd = input("你这么笨，是找不到对象的，还要不要试一把？(y/n)").strip()
        if cmd in ["Y","y","yes"]:
            count = 0 # 把count重置为0
        else:
            print("bye........see u...")

