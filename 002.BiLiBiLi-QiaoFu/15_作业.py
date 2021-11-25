# ⽂能提笔安天下,
# 武能上⻢定乾坤.
# ⼼存谋略何⼈胜,
# 古今英雄唯是君.

print("⽂能提笔安天下,\n武能上⻢定乾坤.\n⼼存谋略何⼈胜,\n古今英雄唯是君.")


# ---
# 如果⼩于10, 提⽰⼩屁孩,
# 如果⼤于10, ⼩于# 20, 提⽰青春期叛逆的⼩屁孩.
# 如果⼤于20, ⼩于30.提⽰开始定性, 开始混社会的⼩屁孩⼉,
# 如果⼤于30, ⼩于40.提⽰看老⼤不⼩了, 赶紧结婚⼩屁孩⼉.
# 如果⼤于40, ⼩ 于50.提⽰家⾥有个不听话的⼩屁孩⼉.
# 如果⼤于50, ⼩于60.提⽰⾃⼰⻢上变成不听话的老屁孩⼉.
# 如果⼤于60, ⼩于70.提⽰活着还不错的老屁孩⼉.
# 如果⼤于70, ⼩于# 90.# 提⽰⼈⽣就快结束了的⼀个老屁孩⼉.
# 如果⼤于90以上.提⽰.再⻅了这个世界.

age = int(input("请输入您的年龄： "))
if age > 90:
    print("再⻅了这个世界.")
elif age > 70:
    print("⼈⽣就快结束了的⼀个老屁孩⼉.")
elif age > 60:
    print("活着还不错的老屁孩⼉..")
elif age > 50:
    print("⾃⼰⻢上变成不听话的老屁孩⼉.")
elif age > 40:
    print("家⾥有个不听话的⼩屁孩⼉.")
elif age > 30:
    print("看老⼤不⼩了, 赶紧结婚⼩屁孩⼉.")
elif age > 20:
    print("开始定性, 开始混社会的⼩屁孩⼉,.")
elif age < 0:
    print("没出生的别淘气。。。.")
else:
    print("⼩屁孩...")

# ---
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i = i +1
    print(sum)


# ---
# 下面两段代码为啥不一样？多了一个变量结果就不一样了？
count = 1
sum = count % 2
while count <= 100:
    if sum == 1:
        print(count)
    count += 1

count = 1
while count <= 100:
    if count % 2 == 1:
        print(count)
    count += 1

count = 1
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1

# ---
# 求1-2+3-4+5 ... 99的所有数的和.  提示: 使用循环, 每次循环都把上一次计算的结果累加在一个变量里.
#
# 这个逻辑没太理解。
count = 1
sum = 0
while count <= 99:
    if count % 2 == 1:
        sum += count  # sum = sum + count
    else:
        sum -= count
    count += 1
print( sum )


# ---
# 7. 计算361+362+363+…+460 = ?

count = 361
while count <= 460:
    count += 1
    print(count)

count = 361
sum = 0
while count <= 460:
    sum = sum + count
    count += 1
print(sum)


"""
---
8. 输入一年份，判断该年份是否是闰年并输出结果。
注：凡符合下面两个条件之一的年份是闰年。
（1） 能被4整除但不能被100整除。
（2） 能被400整除。
"""

num = int(input("请输入您要测试的年份：" ))

if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("您测试的年份是闰年")
else:
    print("您测试的不是闰年！！")

# JS判断闰年代码
#
# function
# isLeapYear(year)
# {
# if (((year % 4) == 0) & & ((year % 100) != 0) | | ((year % 400) == 0))
# {
# return (true);
# } else {
# return (false);}
# }

