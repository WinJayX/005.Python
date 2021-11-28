# 存款多少儿才能翻倍？
    # 1万本金，利息0.0325/年，问连本带利多少年能翻倍。

base = 10000
interest = 0.0325

# # how_many_years = ?
years = 0       # count 计数器
while base <= 20000:
    base += base * interest
    years += 1
    print(f'这个数器是{years} 年,存款总共是{base}')




# 使用for循环的前提条件是你可以已知结束的条件，但上述题中没有结束的年限，这个是求证的，所以使用while循环。

for i in range(1, 1000):
    base = base + base * interest
    print(base)
    if base >= 20000.065:
        print(i, f'是{i}年。。')
        break

# ---
#
high = 100
count = 1
result = 0      #初始长度
while count <= 10:
    result = result + high
    count += 1
    high = high / 2

    print(result)



# 参考老师作业

# count = 0       # 计数器
# height = 100    # 初始高度。
# result = 0      # 记录球滚动的距离长度
# while count < 10:
#     result += height         # 第一次的滚动长度 等于初始高度（但是第二次的话是第一次的长度+第二次的长度，所以x = x + 第二次的）
#     height = height / 2
#     result += height
#
#     count += 1
#     print(result)