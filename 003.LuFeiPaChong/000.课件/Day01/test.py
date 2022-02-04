#如何调用inner这个内部函数呢？
def outer():
    print('我是外部函数outer')
    def inner():
        print('我是内部函数inner')
    return inner #返回的是内部函数名，不加括号的！

res = outer() # outer() == inner, result == inner
# result() # inner()
res()
print('========')
print(res())