def stu_registriation_form():
    form = {
        "name": input("Name:").strip(),
        "age": input("Age:").strip(),
        "phone": input("Phone:").strip()
    }

    info_pass_flag = True  # 如果字段全填了，就是True
    for k, v in form.items():
        if len(v) == 0:  # 没写东西
            info_pass_flag = False
            break

    return form, info_pass_flag


stu_info, flag = stu_registriation_form() # 接收2个值
print(stu_info)
print(flag)
if not flag: # false
    print("表单填写有误...")
else:
    print("欢迎成为路飞学城的学员....")