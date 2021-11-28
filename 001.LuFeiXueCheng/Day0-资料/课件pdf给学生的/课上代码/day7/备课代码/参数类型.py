# def stu_form(name, age, major, phone):
#     info = f'''
#     Name : {name},
#     Age  : {age},
#     Major: {major},
#     Phone: {phone}
#     '''
#     print(info)
#
#
# # stu_form(major="Computer Science", name="Alex", phone=13334, age=22)
# stu_form( "BlackGirl",  major="Accounting", age=24, phone='1445533' )
#
# # stu_form("Alex", 22, "IT")

#
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
#
# # stu_form("Alex", 22, "IT")



def stu_form(name, age, major, phone, nationality='CN',*args,**kwargs):
    info = f'''
    Name : {name},
    Age  : {age},
    Major: {major},
    Phone: {phone},
    Nation: {nationality}
    '''
    print(info)
    print("不定长列表参数:",args,kwargs)


info = {'hometown':"河南",'university':"北大青鸟"}
hobbies = ["Alex",'Movies',"LiveHouse"]

stu_form("XiaoYun",23,"Finance",13332,"Thailand",'Alex','Movies',*hobbies,**info)


