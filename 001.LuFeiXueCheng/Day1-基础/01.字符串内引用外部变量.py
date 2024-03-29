# 两种方式

# - 第一种 %           基本不用
# %s      string    str
# %d      digit     int
# %f      float     f
name = '大头'
age = 26
hobbie = 'Linux'

info = '''------%s Info -------
name : %s
age : %s--%d--%f        
Hobbie : %s
''' % (name, name, age, age, age, hobbie)
# age传递了三次age信息，第一次类型为字符串(str)，第二次类型是数字(int)，第三次类型是浮点数(f)。

print(info)


# -------------------

# - 第二种 f       强烈使用

name = "WinJay"
age = 28
hobbie = 'girl'

info = f'''--------{name} Info -------
name : {name}
age : {age}
Hobbie : {hobbie}
'''
print(info)
