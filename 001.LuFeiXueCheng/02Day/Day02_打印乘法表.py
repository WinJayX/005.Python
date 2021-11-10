for i in range(1,10):               #从1开始取值，共取到9
#    print(f"1 x {i} = {1*i}")
    print()                         #print 参数自带换行属性，在此是为了这个外部大循环可以换行
    for j in range(1,i+1):          #从1开始取值，取到i，即是i+1
        print(f"{j} x {i} = {j * i}", end="   ") #end="",等于空，即不换行了，就是让内循环的都在一行上。

print("")
print(500*'=')


for i in range(10):
    if i < 10:
        # print(f"1 * {i} ={1*i}")
        print("")  # 打印换行
        for j in range(1,i+1):      # 变量j 从1 开始，到 i结束，因为i+1了。range顾头不顾尾。
            print(f"{j} * {i} = {j*i}", end="  ")

