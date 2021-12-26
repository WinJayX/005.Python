names  = ()
print(type(names))

names = ('WinJay', 'Xiu', 'Qing', 'Lin', ['Lan', 'Gui', 'Chen', 'Xuan'])
# 元组里面嵌套列表，这个列表是独立存在的，所以里面的值可修改，跟外面的元组是独立的内存地址。ID

print(id(names), id(names[4]))

for i in names:
    print(i)

# 元组的特点：只能查、删；不可新增、修改，只要符合对应的业务场景，都可以使用。

# 使用方式跟列表无区别。