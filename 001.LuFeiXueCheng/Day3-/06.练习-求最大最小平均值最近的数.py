list = [2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 35, 45, 52, 54, 56, 57, 67, 74, 89]
max_num = list[0]
lim_num = list[1]
for i in list:
    if i > max_num:
        max_num = i
    if i < lim_num:
        lim_num = i

print(max_num, lim_num)

avg_n = (max_num + lim_num) / 2
print(avg_n)

number = list[0]
for n in list:
    number = n - avg_n


# 老师代码
for n in li: # 12
    if abs(avg_n - n) < abs(avg_n - closest_n ) : # 代表找到了更近的值 , 需要把最近的值 ，给到closet_n
        closest_n = n
        print("找到更近的了",closest_n)

print(closest_n)