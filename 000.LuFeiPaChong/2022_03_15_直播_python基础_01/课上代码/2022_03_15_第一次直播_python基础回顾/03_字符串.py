# s1 = "周杰伦的妹妹"
# s2 = '周杰伦的媳妇'
# s3 = """周杰伦的小舅子"""
# s4 = '''孙同学的小弟弟'''

# 索引和切片 []
# 字符串: 把字符按照固定的顺序连成串
# 索引： 字符的位置,从0开始数
# 编程的世界里。 基本上都是从0开始的。
# c = s1[3]
# print(c)
# c2 = s2[2]
# print(c2)  # Index(索引)Error(错误): string index out of range

# # 切片(面包切片) 从字符串中切出来一小段字符串
# s = s1[1:4]  # 前面能取到， 后面取不到, 前闭后开区间[)
# print(s)

# c11 = s2[1:]  # 从1开始, 取到最后
# print(c11)
#
# lst = ["表头xxxxx", "数据1", "数据2"]
# new_list = lst[1:]

# \n 换行
# \r 回车
# \t 制表符
#    空格
# 上面这一坨都是空白符

# s = "\n\t    \n\t    哈哈哈哈哈呵呵呵哒 \n\r      \t\t\t\t\t"
# print(s)
# 去掉左右两端的空白符
# s1 = s.strip()
# print(s1)
# print(s)
# # 字符串不会在原来的基础上进行更改. 会返回新结果. 新结果才是你要得
# # 下面的代码是一个反例!!!!!
# s.strip()
# print(s)
# # 死刑, 立即执行!



# s = "12,ffff,333"  # 三个本应分开的数据. 现在在一个字符串里面
# # 切开 获取到， 10， 英雄本色， 1000万
# lst = s.split(",")  # 记住, split()的结果是列表.
# # num = lst[0]
# # name = lst[1]
# # money = lst[2]
# # 可以直接将列表中的数据. 提取成n个变量
# num, name, money = lst  # 解包, 必须一一对应. 否则报错.
# print(num)
# print(lst)

# lst = ["张三丰", "张无忌", "张翠山"]
# a1, a2, a3 = lst


# s = " \r      我      \n\n爱   黎       明    "
# # replace() 替换掉字符串中的特殊内容
# s1 = s.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
# print(s1)


# lst = ["\r\n          ", "\r\n          ", "黎明", "\r\n  爱", "我"]  # 练习题.结果:黎明爱我
# # 把列表拼接起来成一个字符串
# #  拼接符
# s = ''''''.join(lst)
# print(s)


# name = "周杰伦"
# s = f"我喜欢的歌手是{name}"
# print(s)

# i = 10
# s = f"我考试考了{i + 90}分"
# print(s)



name = '张五丰'
s = f'我喜欢的人是{name}'
print(s)