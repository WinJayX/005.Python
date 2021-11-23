#需求：判断用户登陆。

username = input("please input your username: ")
password = input("please input your password: ")

if username == 'admin':
    if password == 'nerc':
        print("Login!")         #程序走到这里的前提是用户名与密码对了
    else:           # 只有当密码错误时才会走到这里
        print("Your password is error")
else:               #程序走到这里时只能是用户名输入错误
    print("Your username is error!")
    
