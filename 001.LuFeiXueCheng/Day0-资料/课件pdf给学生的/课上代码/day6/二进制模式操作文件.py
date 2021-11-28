#
# f = open('qrcode.png','rb')
# for line in f:
#     print(line)
# #


f = open("file_gbk.txt", mode="wb")
s = "路飞学城"
f.write(s.encode("utf-8"))

s = "路飞学城"
s_utf8 = s.encode("utf-8")  # 编码成utf-8
s_gbk = s.encode("gbk")  # 编码成gbk
print("utf8:", s_utf8)
print("gbk :", s_gbk)

print("由gbk解码回unicode:", s_gbk.decode("gbk")) # 必须告诉解释器，文本当前编码是什么，才能按相应的编码转回来
