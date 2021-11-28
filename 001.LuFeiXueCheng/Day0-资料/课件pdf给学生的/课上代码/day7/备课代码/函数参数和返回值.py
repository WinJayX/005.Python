#
# def say_hi(name):
#     print(f"Hello, I'm {name},  valar morghulis")
#
#
# say_hi("Alex金角大王")
#
# names = ["Alex", "Peiqi", "BlackGirl", "Celina", "XiaoYun"]
#
# for i in names:
#     say_hi(i)


# def mobile_check(phone_num):
#     if len(phone_num) == 11:
#         if phone_num.isdigit():
#             if phone_num.startswith('1'): # 1开头
#                 return True
#
# s = '13651054609'
# if mobile_check(s): # 结果是True
#     print("合法手机号...")

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


stu_info, flag = stu_registriation_form()
print(stu_info)
print(flag)
