# wrapper1
def wrapper1(func):
    def inner(*args, **kwargs):
        print('this way wrapper1 in')
        result = func(*args, **kwargs)
        print('This way wrapper1 out')
        return result
    return inner



# 目标函数
@wrapper1
def target():
    print('this is target function')

target()

