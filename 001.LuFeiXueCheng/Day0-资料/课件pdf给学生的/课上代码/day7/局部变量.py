def change_name():
    # global name
    name = "Alex" # 局部变量，只在函数内部生效
    print("in func:", name)
    print(globals())
    print(locals())
name = "金角大王"  # 全局变量， 整个代码文件全局生效

change_name()
print("global var:",name)