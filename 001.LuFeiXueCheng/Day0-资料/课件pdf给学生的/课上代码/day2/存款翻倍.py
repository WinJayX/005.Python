# base = 10000
# interest = 0.0325
# how_many ?
# end condtion = 20000

base = 10000 # 本金
interest = 0.0325 # 利息
year = 0
while base <= 20000:
    year += 1
    base = base + (base * interest)
    print(year,base)