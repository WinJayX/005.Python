
def get_square(n):
    """求平方"""
    return n*n

li = [9,11,2,3,4,8,19,12,30]
li2 = []
for i in li:
    val = get_square(i)
    li2.append(val)
print(li2)

def add_one(n):
  return n+1
li = [9,11,2,3,4,8,19,12,30]
print(list(map(add_one, li))) # 给列表里每个值+1
print(list(map(lambda n:n+1, li))) # 给列表里每个值+1