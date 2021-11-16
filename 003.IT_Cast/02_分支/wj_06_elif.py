# elif 是在判断多个条件，条件不同执行的代码也不同，而逻辑运算符and or not是多个条件成立或不成立都是执行的一段代码。
holiday_name = input("输入是啥节日：")
if holiday_name == "情人节":
    print("买玫瑰，看电影")
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")
elif holiday_name == "生日":
    print("买蛋糕！")
else:
    print("每天都是节日啊。。。")
