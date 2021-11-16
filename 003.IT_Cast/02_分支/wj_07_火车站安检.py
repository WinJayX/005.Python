has_ticket = True
knife_length = 33

if has_ticket:
    print("车票检查通过，准备开始安检！")
    if knife_length > 20:
        print("大刀太长了啊。。。不能上车")
        print("您的刀有%d公分长啊，不允许上车" % knife_length)
    elif knife_length > 10:
        print("属于危险品，请交由乘务员处理！")
    else:
        print("安检已经通过，祝你旅途高兴")
    # 车票检查通过，准备开始安检！
    # 车票检查通过，准备开始安检！
    # 车票检查通过，准备开始安检！

else:
    print("请先去买票")