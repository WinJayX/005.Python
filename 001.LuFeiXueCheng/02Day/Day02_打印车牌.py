import random
import string


count = 3
while count > 0:
    count -= 1
    # print("这个是取给定字符串中的一个字符--------------"+random.choice('dasfasdfasfas'))
    # # print("========在给定的字符串中随机打印一个字符=======")
    # count += 1
    # print("这个是取所有字母及数字中的一个字符----------"+random.choice(string.ascii_letters + string.digits))
    # # print("这个是取1--9 之间的随机数字----------" + random.randint(1, 9))
    #
    car_nums = []       #定义这个是为了方便用户输入的值做in 判断所用
    for i in range(20):
        upp = random.choice(string.ascii_uppercase)         # 生成京后面的第一个字母
        num = "".join(random.sample(string.ascii_uppercase + string.digits, 5))     #“”.join 是将所有的字符进行拼接。
        c_num = f"京{upp}*{num}"
        car_nums.append(c_num)
        print(i+1, c_num)           #这个地方不是打印每次的列表car_nums值，而是打印最后一次列表的值c_num

    number = input("请输入您选择的车牌：").strip()   #str.strip()去掉两边的空格及回车
    if number in car_nums:
        exit("恭喜您选中车牌")
    else :
        print(f"未选中， 还有{count}次机会")  #由于这里打印了剩余次数，所以上面的count 用递减来计数了。
    # else:
    #     exit( "已经没有机会了哦。。" )
    #     # break







