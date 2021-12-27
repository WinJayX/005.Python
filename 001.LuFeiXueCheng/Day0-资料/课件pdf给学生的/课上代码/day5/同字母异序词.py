
arr = ['cat', 'dog', 'tac', 'god', 'act']

dic = {
    #('a','c','t') :[]
}

for i in arr:
    to_key = list(i) # 变成列表
    print(to_key)
    to_key.sort()
    to_key = tuple(to_key) # 变成一个元组，这样可当成key
    if to_key not in dic: # 之前没有，创建一个
        dic[to_key] = [ i ]
    else:# 已在
        dic[to_key].append(i)

print(list(dic.values()))

