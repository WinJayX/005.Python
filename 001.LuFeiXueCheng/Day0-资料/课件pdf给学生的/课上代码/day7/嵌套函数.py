def stu_form():

    form = {
        "name": input("Name:").strip(),
        "age": input("Age:").strip(),
        "major": input("Major:").strip(),
        "phone": input("Phone:").strip()
    }

    print(form)
    # 下面边个子函数，是写了一个可以改form dict值 的功能
    def change_form(form_data):  # 这个函数只能在stu_form内调用
        print(form_data.keys())
        print("--------------修改信息--------------")
        while True:
            key = input("输入要改的key>:").strip()
            if not key:continue
            if key in form_data.keys():
                print(f"({key})的当前值{form_data[key]}")
                key_new_val = input("输入要改的新值:").strip()
                form_data[key] = key_new_val
                break
            else:
                print("不合法的key...")

    change_form(form) # 内部调用
    print("new form:",form)

    return form

#stu_form()
stu_form.change_form