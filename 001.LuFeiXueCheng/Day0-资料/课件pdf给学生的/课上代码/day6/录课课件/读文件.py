f = open("model_contacts.txt")
# data = f.read() # 读所有
# print(data)
# data = f.read(2) # 代表10个字符呢？还是字节？
# print(data)
print(f.readline())
print(f.readline())
print(f.readline())
print('--------中间--------')

f.seek(0) # 光标移到开头
print(f.readline())
#
# for line in f:
#     if "梓萱" in line:
#         print(line)

