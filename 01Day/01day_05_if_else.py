# salary = int(input("填上你的收入吧："))
#
# if salary <= 10000:
#     print("工资太少了，人又丑，咋找对像啊。。。")
# elif 10001 <= salary <= 20000:
#     print("还湊合吧。能够生活的")
# elif 20001 <= salary <= 50000:
#     print("大佬，带我")
# else:
#     print("写上吧！！")

#猜年龄

black_girle_age = 26
guss = int(input("输入你猜的年龄吧："))
if black_girle_age > guss:
    print("猜小了。。。")
elif black_girle_age < guss:
    print("猜大了。。。")
else:
    print("猜对了。。")


#心态

salary = int(input("再来工资吧："))
if salary <= 1000:
    print("老板，我是你爹")
elif 1001 <= salary <= 2000:
    print("老板，wqnmlgbdb")
elif salary <= 5000:                #这种写法稍好些，但是需要从大向小匹配，因为程序是从上而下读取的
    print("老板，你脑子有坑吧。。。")
elif 5001 <= salary <= 20000:
    print("刚刚够")
elif 20001 <= salary <= 50000:
    print("996 都不叫事儿。。。")
elif 50001 <= salary <= 100000:
    print("公司是我家")

