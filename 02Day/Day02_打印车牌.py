import random
import string


count = 0
while count < 3:
    # print("这个是取给定字符串中的一个字符--------------"+random.choice('dasfasdfasfas'))
    # # print("========在给定的字符串中随机打印一个字符=======")
    # count += 1
    # print("这个是取所有字母及数字中的一个字符----------"+random.choice(string.ascii_letters + string.digits))
    # # print("这个是取1--9 之间的随机数字----------" + random.randint(1, 9))
    #



    for i in range(20):
        upp = random.choice(string.ascii_uppercase)         #京后面的字母
        num = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        s = (f'京{upp}*{num}')
        print(s)
    count += 1
    number = input( "请输入您选择的车牌：" )
    if number in s:

        print( "恭喜您选中车牌" )
    # elif:
        print( "请再选一次" )
        exit( "已经没有机会了哦。。" )







