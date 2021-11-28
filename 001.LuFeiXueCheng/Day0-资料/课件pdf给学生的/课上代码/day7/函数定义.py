#
# def say_hi(name):
#     """
#     打印消息
#     :param name:
#     :return:
#     """
#     print(f"Hello, {name}, valar morhultis...")
#
#
#
# print(say_hi("Alex"))
# say_hi("Alex2")
# say_hi("Alex3")
# say_hi("Alex")


def mobile_check(phone_num):
    if len(phone_num) == 11:
        if phone_num.isdigit():
            if phone_num.startswith('1'):  # 1开头
                return True, phone_num


s = '13651054609'
print(mobile_check(s))

# if mobile_check(s): # 结果是True
#     print("合法手机号...")
#
