result = int(input('请输入您的成绩，以便进行判断：'))

if result > 90 and result < 100:
    print('恭喜您，获得 A.')
elif result >80 and result < 89:
    print('还不错，获得 B')
elif result >60 and result < 79:
    print('已Pass，获得 C')
elif result >40 and result < 59:
    print('需要努力啦，获得 D')
elif result >0 and result < 39:
    print('加倍努力哦，获得 E')
else:
    print('请输入0--100之间的正确数字，谢谢！')
