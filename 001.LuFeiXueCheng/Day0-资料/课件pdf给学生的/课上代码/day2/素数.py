
# 1 2 3 4 5 6 7 8 9
for i in range(2,101): # i =9
    is_prime_num = True # 假设i是素数...
    for j in range(2,i): # 拿2-8之前所有数，跟9相除， 如果能被9整除，代表9不是素数
        if i % j == 0 : # 能整除,代表 i 不是素数.
            is_prime_num = False # 证伪
        # else: # 不能被整除./ 代表9是素数?
        #     print(i,"is prime num")
    if is_prime_num == True:
        print(i,"是素数...")