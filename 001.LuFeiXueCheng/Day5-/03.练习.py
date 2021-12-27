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



