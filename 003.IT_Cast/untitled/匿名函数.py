def my_func(f,age):
    return f(age)
print(my_func(lambda x: 2*x*x,5))


my_func(lambda x:2*x*x,5)



def polynomia(x):
    return x**2 + 5*x +4
print(polynomia(-4))

y = -4**2
z = -4*-4
print(y,z)# 这个好奇怪啊。。。为毛-4**2 与-4*-4的结果不一样？不应该都是负负得正为16吗？

print((lambda x:x**2 +5*x +4)(-4))

double = lambda x:x*2
print(double(9))



fast = lambda x:x**4 - 5*x
print(fast(2))




triple = lambda x: x*3
add = lambda x,y: x+y

print(add(triple(3),4))
print(y)



#-64 -20 -80


