test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
test_dic = {}
for i in test_list:
    if i not in test_dic: # 第一次遇到4
        test_dic[i] = [i,] # 创建一个key
    else: # 下次遇到4
        test_dic[i].append(i) # 追加

print(test_dic)