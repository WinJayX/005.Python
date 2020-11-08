for i in range(10):
    if i < 10:
        # print(f"1 * {i} ={1*i}")
        print("")  # 打印换行
        for j in range(1,i+1):      # 变量j 从1 开始，到 i结束，因为i+1了。range顾头不顾尾。
            print(f"{j} * {i} = {j*i}",end="  ")


