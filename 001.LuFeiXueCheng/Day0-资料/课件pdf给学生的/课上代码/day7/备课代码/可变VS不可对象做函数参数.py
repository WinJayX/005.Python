


def change_data(name,hobbies):
    name = "Alex"   # 修改只在函数内生效
    hobbies.append("大保健")  # 在函数内往外部列表添加值
    hobbies[1] = "XiaoYun"   # 修改列表元素
    print("in func:",name,hobbies)


my_name = "金大王"
my_hobbies = ["Money","BlackGirl"]
change_data(my_name,my_hobbies)
print(my_name,my_hobbies)


