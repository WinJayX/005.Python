count = 0
while count < 3:
    count += 1
    print('pool', count)


count = 0
age = 38
while count < 3:
    guess = input('请输入你猜的年龄：').strip()
    count += 1
    if guess.isdigit():
        guess = int(guess)
    else:
        print('----------不识别的输入，请输入正常的年龄----------')
        continue


    if guess < age:
        print('嘻嘻，人家比这个大呢，你猜小了。。。')
    elif guess > age:
        print('讨厌了啦，人家哪有那么大，猜大了。。。')
    else:
        print('哥哥猜的真准。。。。')
        break

#   完成三次后询问

    if count == 3:
        cmd = input('还想再次猜一轮吗： ').strip()
        if cmd in ['y', 'Y', 'Yes', 'YES','YEs']:
            count = 0
        else:
            print('Bye...le nin lai....')
            exit()



