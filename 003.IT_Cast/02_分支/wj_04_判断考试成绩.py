python_score = input("请输入您的python成绩：")
c_score = input("请输入您的C成绩：")

total = int(python_score) + int(c_score)

if int(python_score) >= 60 or int(c_score) >= 60:
    print("成绩合格，您的总成绩为%.2f" % total)
else:
    print("成绩不合格，您的总成绩才为%.2f" % total)