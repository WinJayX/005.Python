'''
特性
1. key-value结构
2. key必须为不不可变数据类型（字符串串、数字）、必须唯⼀
3. 可存放任意多个value、可修改、可以不不唯⼀
4. ⽆无序, ordered_dict
5. 查询速度快，且不不受dict的⼤大⼩小影响，⾄至于为何快？我们学完hash再解释。
'''

info = {
    "name": "WinJayX",
    "name": "杨九郎",                  #key:value 组合，key 必须唯一，如相同会覆盖。
    "age": 32,
    "hometown": "Shandong",
}
print(info["name"], info["age"])



deyunshe = {
    "郭德钢": ["CEO", 54, 100000],
    "于谦": ["CEO",59,100000],
    "栾云平": ["副总", 36, 90000],
    "高峰": ["副总", 39, 90001],
    "侯震": ["候爷", 42, 89999],
    "烧饼": ["儿徒", 32, 79999]
}
deyunshe["孙越"] = ["胖子", 38, 88888]          # 新增键值对信息
deyunshe["云鹏"] = ["一哥", 36, 88889]          # 新增键值对信息
print(deyunshe)

print(deyunshe["于谦"][1])    # 根据key 查询value 的值，value 可以是数组，就按数组取值的方法去取。
print(deyunshe.pop("侯震"))   #删除指定的key，默认返回删除的value值，如果key 不存在即报错。
print(deyunshe)
del deyunshe["烧饼"]          #删除指定的key，不返回任何信息，如果key 不存在即报错。
print(deyunshe)


deyunshe["高峰"] = ["总教习", 38, 190000]        # 修改，直接重新赋值即可
print(deyunshe)

# 查操作
print(deyunshe["高峰"])                         # 返回字典中key对应的值，若key不存在字典中，则报错；
print(deyunshe.get("栾1云平"));print(deyunshe.get("栾云平"))      # 返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）
print(deyunshe.keys())                         # 返回一个列表，其中包含了字典所有的KEY
print(deyunshe.values())                       # 返回一个列表，其中包含了字典所有的VALUE
print(deyunshe.items())                       # 返回一个列表，其中包含了字典所有的VALUE


######=====循环=====######
list = deyunshe.items()                   # 返回一个列表，其中包含了字典所有的VALUE
# 方法1
for i in deyunshe.items() :
    # print(i)
    print(i[0], i[1])                     # 与列表枚举的打印有点儿不一样，列表是取的索引值，字典没有索引，因为无序啊，所以只能取key

print("=" * 50)


# 方法2
for k, v in deyunshe.items() :
    print(k, v)                           # 等同于for i in list: print(i[0], i[1])

print("=" * 50)


# 方法3
for k in deyunshe:
    print(k, deyunshe[k])
