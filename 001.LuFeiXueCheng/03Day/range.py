# i = range(10)
# print(i)
# print(type(i))
# print(list(i))
#
#
# a = ['#', '4', '@', 'eva', 'rain', '狗蛋', '⾦金金⻆角⼤大王', '银⻆角⼤大王', '⿊黑姑娘']
# print(a[5])
# print(a[2:4])
# print(a[-3:])
# print("--------")
# print(a.sort())
# print(a)
# print("+" * 50)
# print(a.reverse())
# print(a)
# print(a.index("rain"))
# print("----------")
# for i in enumerate(a):
#     print(i[0], i[1])
#
#

x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))