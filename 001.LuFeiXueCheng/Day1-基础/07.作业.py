# 作业一：猜年龄

age = int(21)
guess = int(input('请输入您猜的年龄是：  '))

# if guess.isdigit():
#     print('请输入数字哟。。。')
#     exit()


if guess < age:
    print('嘻嘻，哥哥猜的有点小了，请往大了猜一下！！')
elif guess > age:
    print('人家哪有那么大，讨厌了啦。。。')
else:
    print('哟哟哟，哥哥阅妹无数嘛。。。')



# --------------------------
# 作业二：读取用户输入的工资，根据数据打印出对老板说的话。

money = int(input('小伙，这月发了多少啊:  '))

# Q: 如何判断money 接收到的是int类型的数据？

if money <= 0:
    print('请输入正确的工资啊。。。')

elif money <= 1000:
    print('老板，我是你爹。。')
elif money <= 2000:
    print('老板，WQNMLGBXXXXX')
elif money <= 5000:
    print('老板，你脑子瓦特了。。。。')
elif money <= 10000:
    print('老板，你说有的问题，但是我就不说话。。。。')
elif money <= 50000:
    print('老板，996就像呼吸一样自然')
elif money <= 100000:
    print('老板，公司是我家')

else:
    print('你是老板吧。。。')
