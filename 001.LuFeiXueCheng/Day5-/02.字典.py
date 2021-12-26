# 如新华字典一样，使用key values的格式使用。不用像列表一样全遍历一遍。

info = {}
print(type(info))

# Key 必须使用不可变的数据类型，如元组、数字、字符串，列表就不行。

info = {'a': 3, 'b': 7, 'WinJay': 'Name', 'age': 37}

print(info['WinJay'], info['age'])

# 字典的2种创建方式
Info = dict(name='WinJay', age=37, hometown='ShanDong')
print(Info, info)

# 增

Info['Job'] = 'Student'

print(Info)

Info['Job'] = 'Teacher'

print(50*'*', Info)




print(50* '=')
print()
for v in Info:

    print(Info[v])

print()
print(Info['age'])
