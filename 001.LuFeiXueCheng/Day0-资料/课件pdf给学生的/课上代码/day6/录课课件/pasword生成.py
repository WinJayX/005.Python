
import random
import string

names = ["alex",'jack','rain','black_girl','peiqi']
f = open("password.txt", 'w')  # 创建一个文件对象，存为变量f

pass_str = string.punctuation + string.digits + string.ascii_letters
for i in names:
    passwd = "".join(random.sample(pass_str,8))
    f.write(f"{i}:{passwd}\n")
f.close()
