i = 1
while i <= 9:
    x = 1
    while x <= i:
        print("%d * %d = %d" % (x, i, x * i), end="\t")
        x += 1
    print("")
    i += 1