
li = [8, 3, 12,1, 2, 34, 54, 12, 34, 11, 12,14, 9, 1, 10,15, 17, 18, 99, 1, 3, 5, 10]

for n in range(2):
    for index in range(len(li)-1):
        # 让当前索引值index, 跟index+1进行比较
        i = li[index] # 拿到当前索引的值 8

        if i > li[index+1] : # 8>3 , 得换
            li[index] = li[index+1]  # 把3换到8的位置
            li[index+1] = i # 把原来临时存的8，放到3的位置
    print(li)





# max_n = li[0]
# second_n = li[0]
# for i in li:
#     if i > max_n:
#         max_n = i
#
# print(max_n)