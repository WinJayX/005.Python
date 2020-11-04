for i in range(1,10):               #从1开始取值，共取到9
#    print(f"1 x {i} = {1*i}")
    print()                         #print 参数自带换行属性，在此是为了这个外部大循环可以换行
    for j in range(1,i+1):          #从1开始取值，取到i，即是i+1
        print(f"{j} x {i} = {j * i}", end="   ") #end="",等于空，即不换行了，就是让内循环的都在一行上。
