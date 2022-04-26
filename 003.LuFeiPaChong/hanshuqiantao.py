def func1():
    print('fucn1,123')
    def func2():
        print('func2,456')
        def func3():
            print('func3,789')
        func3()
        print('func3结束')
    print('func2结束')
    func2()

# func1()


# def func():
#     def inner():
#         print('inner')
#     return inner
# res = func()
# res()


# a = 10
# def func():
#     global a
#     a = 20

# func()
# print(a)
#
#
# def func2(fu):
#     fu()
#
#
# func2(func)




# 函数返回值，
# def res():
#     def inner():
#         print('123')
#     return inner
#
# res = res()
# res()


