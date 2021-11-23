# input

name = input("Your name is :  ").strip()
age = int(input('Your age is :  '))


Hobbie = input('You Hobbie is : ')

info = f'''
--------{name} Info---------
Name: {name}
Age:  {age}， wow still young , in {30 - age} years you will be 30 years olds.
Hobbie: {Hobbie}
-----------END INFO-----------
'''
print(info.strip())

# strip() 函数，这个测试失败，没有去除空格


