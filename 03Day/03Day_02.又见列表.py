names = ["WinJayX", "WuWenhao", "PengJiangbing", "YangRongfeng", "ZhaoTianRan"]
ages = [31, 23, 43, 32, 29, 27, 17, 35]


############ 2.2 列表增加元素操作 ############
print(names)
names.insert(2, "Nieqifan")
print(names)
names.append("LianJiangwei")                # append 一次只能接受一个值
print(names)
print(len( names ))
names.reverse()                             # reverse() 不接受参数，列表反转
print(names)
# 列表扩展

names.extend(ages)
print(names)

# 列表嵌套及取值
names.insert(3, ages)
print(names)
print(names[3][5])


############ 2.3 列表删除 ############
# del:直接放索引值(必须是int 类型的索引值，不支持删除值)删除指定值
del names[-1]
# del names["WuWenHao"]       # output:TypeError: list indices must be integers or slices, not str
print(names)

# pop:直接放索引值(必须是int 类型的索引值，不支持删除值)删除指定值,默认删除最后一位
names.pop(-3)
print(names)
# remove:这个与上面不同，这是删除value值，而不是根据索引值删元素。
# names.remove(-1)              # output:ValueError: list.remove(x): x not in list
names.remove("ZhaoTianRan")
print(names)


############ 2.4 列表的修改操作 ############
names[3] = "杨九郎"
print(names)
names[-1] = "周九良"
print(names)


############ 2.5 列表的查询操作 ############
print(names.index("WinJayX"))       # index 返回的是索引值
print(names.index("周九良"))
print(len(names))                   # 13  是13 个元素
# 在不知道一个元素在列表哪个位置的情况下，如何修改：
print("杨九郎" in names)             # 1.先判断这个元素是否在列表中
print(names.index("LianJiangwei"))  # 2.使用index方法获取索引值
names[0] = "烧饼"                    # 3.进行重新赋值修改
print(names)                        # 修改完成


############ 2.6 列表的切片操作 ############
print(names[1:5])                  # 顾头不顾尾
print(names[-4:])
print(names[-4:-1])                # 顾头不顾尾,所以不取最后一位
print(names[-4:])
print(names)
# 步长
print(names[::])                   #默认是1，即1 个1 个的取值
print(names[::2])                  #设置步长为2，即跳过1个取值
print(names[::3])                  #设置步长为3，即跳过2个取值

print("=" * 50)


############ 2.7 列表的排序、反转操作 ############
ages.sort()                       # 排序
print(ages)
ages.reverse()                    # 反转
print(ages)


############ 2.8 列表的循环操作 ############

for i in ages:
    print(i)

print("=" * 50)
print(names)
for i in enumerate(names):      # 枚举，返回的i是一个个元组()，与列表相似.
    print(i)                    # output :(0, '烧饼')、(1, 'YangRongfeng')
    print(i[0], i[1])           # 取元组的索引与元素--(共两个)


