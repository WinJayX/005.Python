staff_list = {
    "alex": [23, "CEO", 66000],
    "黑姑娘": [24, "行政", 4000],
    "xiao_yun":[22,"Student",2000],

}

names = {
    "xiao_yun":[25,"前端开发",12000],
    "Celina":[23,"UE", 9999]
}

staff_list.update(names) # 把names的每个k,v赋值给staff_list, 相当于如下操作
# for k in names:
#     staff_list[k] = names[k]

print(staff_list)


