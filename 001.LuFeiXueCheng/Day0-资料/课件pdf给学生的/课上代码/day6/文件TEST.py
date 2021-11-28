import random
import string

names = ["alex",'jack','rain','black_girl','peiqi']

f = open("password.txt", 'w')  # 创建一个文件对象，存为变量f
for i in names:
    passwd = random.sample(string.ascii_letters + string.digits, 8)
    line = f"{i}:{''.join(passwd)}\n"
    f.write(line)
f.close()