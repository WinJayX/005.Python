def change_data(my_name,hobbies):
    my_name = "Alex"   # 修改只在函数内生效
    hobbies.append("大保健")  # 在函数内往外部列表添加值
    hobbies[1] = "XiaoYun"   # 修改列表元素
    print("in func:",my_name,hobbies)


my_name = "金角大王" # 不可变类型
my_hobbies = ["Money","BlackGirl"] # 可变类型
change_data(my_name,my_hobbies)

print(my_name,my_hobbies)