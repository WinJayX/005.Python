count = 1
while count <= 10:
    count += 1
    print(f"死循环{count}次")

#死循环。。。
# count = 1
# while True:
#     count += 1
#     print(f"死循环{count}次")

count = 0
while count <= 2:
    count += 1
    age = 26
    guss = int(input("请输入你猜的年龄："))

    if age < guss:
        print("人家没那么大了啦。。。")
    elif age > guss:
        print("嘻嘻，人家没那么小啦。。。")
    else:
        print("你猜对啦。。。。")       # 不要用 exit 了，要不然后面的代码就不执行了，这个是整个程序都退出了。 用break结束循环，后面的还可以执行
        break

print("===============后面的代码===============")
