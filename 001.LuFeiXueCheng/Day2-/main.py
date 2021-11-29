count = 0
age = 38
while count < 3:
    guess = input('请输入你猜的年龄：')
    count += 1

    if guess == age:
        print('猜的真准')
        exit()
    else:
        print('你真笨，继续猜', count)

    if count == 3:
        cmd = input('还要继续猜吗（Y/N）？').strip()
        if cmd in ['y', 'Y', 'Yes', 'YES']:
            count = 0
        else:
            exit()




# 1.计数器;也是要循环的变量。
                                     # 2.最终结果容器
                           # 3.当这个变量小于=100时
                         # 4.如果这个变量是奇数
# 5.容器结果就是所有的奇数相加的和

                         # 6.否则容器结果就是偶数相减的和

# 计算 1-2+3-4+5.。..100

sum = 0
count = 1

while count <= 100:
    if count % 2 == 1:      # 如果 是奇数
        sum += count
        print(sum)
        count += 1
