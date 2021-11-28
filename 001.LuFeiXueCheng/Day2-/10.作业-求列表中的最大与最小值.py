list = [4, 19, 54, 23, 39, 12, 1, 7, 18, 76, 53, 99]

max_n = list[0]
limit_n = list[0]
for i in list:
    if i > max_n:
        max_n = i
    if i < limit_n:
        limit_n = i
print('最大的值是：', max_n)
print('最小的值是：', limit_n)


# 寻找列表里的数据组合是什么
list1 = [4, 19, 54, 23, 39, 12, 1, 7, 18, 76, 53, 99]
list2 = [2, 7, 13, 87, 9, 3, 6, 7]

for i in list1:
    for j in list2:
        if i + j == 10:
            print('两个列表中可以相加得十的组合是：', [i, j])