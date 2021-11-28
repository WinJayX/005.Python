def stu_form():

    form = {
        "name": input("Name:").strip(),
        "age": input("Age:").strip(),
        "major": input("Major:").strip(),
        "phone": input("Phone:").strip()
    }

    print(form)

    def change_form(form_data):
        print(form_data.keys())
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

    change_form(form)
    print("new form:",form)

    return form

stu_form()

