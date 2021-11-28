

s = "路飞" # unicode
s_utf = s.encode("utf-8")
s_gbk= s.encode("gbk")
print("utf:",s_utf)
print("gbk:",s_gbk)

print("解码:",s_gbk.decode("gbk") )# 告诉解释器，你是gbk编码

