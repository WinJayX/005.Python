# # def stu_form(name, age, major, phone):
# #     info = f'''
# #     Name : {name},
# #     Age  : {age},
# #     Major: {major},
# #     Phone: {phone}
# #     '''
# #     print(info)
# #
# # stu_form(22,"jack","IT",133)
#
# def stu_form(name, age, major, phone):
#     info = f'''
#     Name : {name},
#     Age  : {age},
#     Major: {major},
#     Phone: {phone}
#     '''
#     print(info)
# # stu_form(major="Computer Science", name="Alex", 13334, 22)
# stu_form("Alex", 22, phone="134455455", major="Computer Science",)
#
# # 你不能把位置参数， 写到关键字参数后边。 。。 为什么？
# # 位置 参数 > 关键字参数


# def stu_form(name, age, major, phone, nationality='CN'):
#     info = f'''
#     Name : {name},
#     Age  : {age},
#     Major: {major},
#     Phone: {phone},
#     Nation: {nationality}
#     '''
#     print(info)
#
#
# stu_form( "BlackGirl",  major="Accounting", age=24, phone='1445533',nationality='JP')
# stu_form( "Alex",  major="IT", age=25, phone='1334444')


# def stu_form(name, age, major, phone, nationality='CN', *args, **kwargs):
# def stu_form(name, age, major, phone, nationality='CN', **kwargs):
#     info = f'''
#     Name : {name},
#     Age  : {age},
#     Major: {major},
#     Phone: {phone},
#     Nation: {nationality}
#     '''
#     print(info)
#     # print("不定长列表参数:", args)
#     print("不定长列表参数dict:", kwargs)
#
#
# stu_form("XiaoYun", 23, "Finance",  hometown="河南",university="北大qingniao", phone="3333",nationality="US")  # 多写了最后2个参数


def stu_form(name, age, major, phone, nationality='CN', *args,**kwargs):
    info = f'''
    Name : {name},
    Age  : {age},
    Major: {major},
    Phone: {phone},
    Nation: {nationality}
    '''
    print(info)
    print("argss:",args)
    print("kwargs:",kwargs)

# stu_form("XiaoYun", 23, "Finance", '3333',2,3,4)

my_info = ["Alex",23,"HR",13344,"US","BlackGirl"]

my_dic = {
    "name":"Alex",
    "age":22,
    "major": "IT",
    "phone":2222222,
    "hobbie":"blackgirl"
}

stu_form(*my_info)
stu_form(**my_dic)
# django