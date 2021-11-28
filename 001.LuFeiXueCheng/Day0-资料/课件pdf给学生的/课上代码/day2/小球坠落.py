
height = 100
distance = 0
count = 0
while count < 10 :
    distance += height # 纪录坠落时经过的长度
    height = height / 2 # 反弹回的高度
    distance += height # 纪录反弹回经过的长度
    count += 1
    print(count, distance, height)