# 当你的工资大于3000时去烧烤，否则回家
money = int(input("请输入你的工资："))

if money > 8000:
    print("把你小店给盘了！！我来当老板")

elif money > 7000:
    print("来个烤全羊🐑")

elif money > 5000:
    print("来个大烤鸭！")

elif money > 3000:
    print("来10串大腰子！！")
    print("再来一瓶雪花酒！！")

else:
    print("快回家吧。。。")

print("退出回家")
