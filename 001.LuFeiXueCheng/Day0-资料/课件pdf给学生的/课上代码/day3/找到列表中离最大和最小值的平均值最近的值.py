li = [8, 3, 12,1, 2, 34, 54, 12, 34, 11,50.1,51, 12,14, 9, 1, 10,15, 17, 18, 99, 1, 3, 5, 10]

max_n = li[0]
min_n = li[1]

for i in li:
    if i > max_n:max_n = i
    if i < min_n:min_n = i

avg_n = (max_n + min_n) / 2

print(max_n,min_n,avg_n)
closest_n = li[0] # 假设

for n in li: # 12
    if abs(avg_n - n) < abs(avg_n - closest_n ) : # 代表找到了更近的值 , 需要把最近的值 ，给到closet_n
        closest_n = n
        print("找到更近的了",closest_n)

print(closest_n)









# l2 = [5,32,12]
#
# is_sub_list = True
# for i in l2:
#     if i not in li:
#         is_sub_list = False
#         print("不是子列表....")
#
# if is_sub_list: # true
#     print("是子列表")
