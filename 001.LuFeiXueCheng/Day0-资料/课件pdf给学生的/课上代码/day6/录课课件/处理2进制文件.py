# f = open("../qrcode.png",'rb')
# print(f.read())
#
# 字节类型
# f = open("2进制写文件.txt",'wb',) # 只能以2进制形式写...
# s = "我是Alex大吊环王" # unicode 要编码成utf-8后才能存
# s_gbk = s.encode("gbk")
# print("gbk:",s_gbk)
# f.write(s_gbk)
# #f.write(s.encode("utf-8")) # 编码后，数据变成字节类型
#
#
f = open("2进制写文件.txt",'rb')
data = f.read()
print(data.decode("gbk"))