# 练习： 列表去重
# 练习：找到列表中第2⼤的值
# 练习：统计列表中每个值 出现的次数 ？
# 练习：判断⼀个列表是不是另⼀个列表的⼦列表
# 练习 ： 求出列表中，离最⼤值 和最⼩值 的平均 值 最接近的值
# import random

list1 = [5, 2, 5, 4, 6, 56, 4, 6, 3, 5, 35, 4, 5, 2, 45, 324, 23, 5, 4, 5, 6, 54, 6, 5, 74, 7, 568, 7, 868, 9, 89, 8, 67,
         57, 4, 4, 6, 3, 5, 24, 52, 7]

print(5 in list1)
print(list1.count(5))
print(list1.index(568))
print(len(list1))

for i in list1:
    count_num = list1.count(i)                  # 获得出现的count.次数
    print(i, '这个值出现了', count_num, '次')          # 统计列表中每个值 出现的次数 ？
        # count_num += 1
    while count_num > 1:
        # print('这是', i)
        # print(i in list1)
        list1.remove(i)
        count_num -= 1
        # else:
        #     False
print('列表去重后的结果是：', list1)                        # 去重后的列表元素

# 求第二大值，先排序，再取值。
list1.sort(reverse=True)
print('列表排序后的结果是：', list1)
print('第二大值是：', list1[1])







