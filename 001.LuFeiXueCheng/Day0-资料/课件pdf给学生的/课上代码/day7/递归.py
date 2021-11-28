
#
# n = 100
# while n > 0:
#     n = int(n/2)
#     print(n)
#
# # 自己调用自己

def calc(n):
    n = int(n/2)
    print(n)
    if n >0:
        calc(n) # 调用自己
    print(n)
    return n

res = calc(100)
print(res)
