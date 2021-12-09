#
# list1 = [5, 2, 5, 4, 6, 56, 4, 6, 3, 5, 35, 4, 5, 2, 45, 324, 23, 5, 4, 5, 6, 54, 6, 5, 74, 7, 568, 7, 868, 9, 89, 8, 67,
#          57, 4, 4, 6, 3, 5, 24, 52, 7]
#
# print(list1.count(5))
#
# for i in list1:
#     tims_num = list1.count(i)
#     if list1.count(i) > 1:
#         print(f'List1中的{i}是重复的值,重复了{tims_num}次')
#     else:print(f'{i}是没有重复的值')
#
#     while tims_num > 1:
#         list1.remove(i)
#         tims_num -= 1
#
#
#
# list1.sort()
#
# print(list1)
# print(list1[1])

# 求一个列表是不是另一个列表的子列表

list2 = [2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 35, 45, 52, 54, 56, 57, 67, 74, 89, 324, 568, 868]
list3 = [4, 6, 7, 8, 89, 9, 67, 5, 3, 3, 2]

print('begin')

is_sub_list = True
for i in list3:
    if i not in list2:
        print('List3 不是list2的子列表')
        is_sub_list = False
        exit()  # 检测到不是，退出即可。不再做比较

if is_sub_list:print('是list2的子列表')
