# 6.1 算术运算符 '+， -， *， /， %， //, **'

# % 取模 or 取余数
for i in range(20):
    if i % 2 == 0:
        print(str(i) + ' is 偶数')
    else:
        print(str(i) + '  is 奇数')
        print(i)


# // 取商 or 取除法公式中的整数
print(97 // 3)      # 值为32

# ** 幂乘

print( 3 ** 5)      # 243 = 3*3*3*3*3

print(9 ** 8)


# 6.2 比较运算符 '==， <， >， !=， >=， <='
# return True or False.

a = 3
b = 5
print(a == 5)
print(a >= b)
print(a <= b)




# 6.3 赋值运算符 '+=， -='
a = 3
b = 5
a += 1      # a = a + 1
print(a)

a += b      # a = a + b
print(a)


a -= 1      # a = a - 1
print(a)


print(a)
print(b)
a -= b      # a = a - b
print(a)


# 6.4 逻辑运算符 'and， or， not'
# 三个运算符的优先级排列：
# 1. and
# 2. or
# 3. not

# 一段公式中有多个 and or not == 时 and 是优先计算的。
# 多段or 时，只要有一个条件满足时，即返回True.

# 取反 Not
# 返回bool值

a = 3
b = 5

print(a > b)
print( not a > b)       #not 取反

# 6.5 in not in 成员运算 判断一条数据里面包含有哪些信息。
names = 'lili, xiaowang, xiaoli, xiaozhang, xiaoliu'
print('lili' in names)
print('lili' not in names)
