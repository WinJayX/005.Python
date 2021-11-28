f = open("model_contacts.txt", "r+")

# 1. 先把文件内容加载到内存
# 2. 替换要改的部分
# 3. 清空原文件内容
# 4.把新内容写回去

data = f.read()
# 备份
back_file = open("model_contacts.txt.bak","w")
back_file.write(data)
back_file.close()

data_new = data.replace("刘翠花TracyLiu","伍小仪",)
f.seek(0)
f.truncate() # 清空原文件
f.write(data_new)
f.close()

import os
os.remove("model_contacts.txt.bak")

