# n = 100
# while n > 0 :
#     n = int(n /2)
#     print(n)

def divide_calc(n):
    print(n)
    if n > 0 :
        divide_calc(int(n/2))
    return n
res = divide_calc(10)
print(res)
