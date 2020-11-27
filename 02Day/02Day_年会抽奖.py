import random
import csv
big_list = list(range(1, 301))
count = 3
while count > 0:
    count -= 1

    # only_1 = random.choice(num)       #随机生成一个中奖号码
    num1 = random.sample(big_list, 3)       #随机生成三个中奖号码

    print(f"获得一等奖的三位同事为{num1}，前往泰国三日游免费手术")
    for del_num1 in num1:
        if del_num1 in big_list:
            big_list.remove(del_num1)

        else:
            print(big_list)
    print( f"=====不要着急，还有{len( big_list )}位没中奖哈。。。。" )

    num2 = random.sample(big_list, 6)
    print(f"获得二等奖的6位同事为{num2}，iPhone 手机各一部")
    for del_num2 in num2:
        if del_num2 in big_list:
            big_list.remove(del_num2)

        else:
            print(big_list)
    print( f"=====不要着急，还有{len( big_list )}位没中奖哈。。。。" )

    num3 = random.sample(big_list, 30)
    print(f"获得三等奖的30位同事为{num3}， 前往前台领取")
    for del_num3 in num3:
        if del_num3 in big_list:
            big_list.remove(del_num3)

        else:
            print(big_list)
    print( f"=====不要着急，还有{len( big_list )}位没中奖哈。。。。" )




