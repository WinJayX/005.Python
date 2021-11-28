#
# for i in range(2, 101):         # 1.假如i=9
#     is_prime_num = True         # 9.设置一个标志位✅；如果后面判断跟我这个预期标志不符，那我就把后面的标志位给改掉，再到最后面判断是否是改过了。
#     for j in range(2, i):       # 2.拿2-9之间的所有数与i(9)整除运算。如果前面的有任何一个数能被9整除，就代表9不是素数
#         if i % j == 0:          # 3.能整除，就不是素数，假如已经走到3了，发现可以整除了，那就没必要继续循环计算了，因为他已经是False了。
#             is_prime_num = False        # 证伪，如果上面被整除了，就改变这个值。只要走到这个循环里面就是被整除了
#             # print(f'{i}is not zhishu')
#             # break
#             # 4.判定一个数不是素数的话是好处理的，只要循环中有一个被整除了即可判定不是素数。
#             # 5.但是判定一个数是素数的话，就得将取值区间的所有数都整除运算一下，只有所有的数都不能被整除，才可判定是素数。！！！
#
#         # else:                             # 不能被整除。
#         #     print(f'{i} is  zhishu')
#
#                                             # 6.多次循环之后共同汇聚出来的结果，使用标志位来操作。
#     if is_prime_num:
#         print(i, 是一个素数')














# ---

for i in range(2, 101):
    is_prime_num = True
    for j in range(2, i):           # 这个没有太理解。
        if i % j == 0:
            is_prime_num = False

    if is_prime_num:
        print(i, 'is prime number...')

