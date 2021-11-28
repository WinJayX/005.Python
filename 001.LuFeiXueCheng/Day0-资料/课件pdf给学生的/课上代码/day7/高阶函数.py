
def get_abs(n):
    if n < 0 :
        n = int(str(n).strip("-"))
    return n


def add_num(x,y,func):
    return func(x) * func(y)

n = add_num(3,-9,get_abs)
print(n)