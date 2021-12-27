test_list = [4, 2, 6, 4, 6, 8, 2, 5, 6, 7, 9, 3, 9, 5]

test_dic = {}

for i in test_list:
    if i not in test_dic:
        test_dic[i] = [i, ]
        # print(test_dic[i])
    else:
        test_dic[i].append(i)   # 当i在字典中时（Key）， 同是，这个V也是个列表，即i = [6, 6] 意思就是i.append(i)
print(test_dic)


dist1 = {}

for i in range(100):
    if i not in dist1:
        dist1[i] = i
print(dist1)


dist2 = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
for k, v in dist2.items():
    if v > 5:
        print(k, end=',')



# 把题2中value是偶数的统⼀改成-1
dist3 = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
print(dist3.values())

for k in dist3:
    print(k, dist3[k])      # 循环字典的key, 并打印出key值，与v值（dist3[k]就是获取这个key对应的values值啊。。）

for k in dist3:
    if dist3[k] % 2 == 0:
        dist3[k] = -1
print(dist3)




string = 'Python is great and Java is also great'
output = []
list = string.split(' ')        # 字符串变列表。
# print(list)

for items in list:
    if items not in output:
        output.append(items)
print(" ".join(output))




dic7 = {'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1,2, 5]}

list7 = []
for k in dic7:
    for n in dic7[k]:
        if n not in list7:
            list7.append(n)
list7.sort()
print(list7)







