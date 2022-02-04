b = [1, 43, 343, 1, 5, 8, 3, 5, 6]

to_set = set(b)
print(to_set)
to_list = list(set(b))

print(to_list)



to_set.add('WinJayX')

print(to_set)


for i in to_set:
    print(i)

if 98 not in to_set:
    print(98)

print(to_set.remove(43))

print(to_set)

print(to_set.pop())
print(to_set)
print(to_set.discard(5))
print(to_set)
