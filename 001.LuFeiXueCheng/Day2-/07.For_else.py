# for/while....else

for i in range(10):
    print(i)
    if i >= 5:
        break

else:
    print()
    print('----------这里的else是程序正常结束----------')



print('--------------------')

count = 0
while count < 11:
    print(count)
    count += 1
    if count == 5:
        break

else:                   # 循环正常退出他就执行，不正常退出他就不执行
    print('----------也是正常退出----------')



print('--------------------')

# 质数重做

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            # print(i, '是质数')
            break
    else:
        print(i, '是质数')

