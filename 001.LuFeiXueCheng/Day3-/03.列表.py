str = 'Hello there, My name is WinJay, What are you doing now?'

str_list = list(str)
print(str.split())

print(str_list)

# [0:9:1]       从左边取 前9个，步长为1，
pian = str_list[:9:3]

# [0:9:3]       从左边取 前9个，步长为3
pian = str_list[:9:3]

# [::-1]      列表反转，步长为1。
pian = str_list[::-1]


# [:0:-1]      列表反转，步长为1。
pian = str_list[:0:-1]      # 虽然这个地方写的是到0结束，但这个语法是顾头不顾尾，所以列表的0位字符是不打印出来的。


# [-1:9:-1]      列表反转，步长为1。
pian = str_list[-1::-8]        # [-1:9:-1]与[:9:-1]  都可以，但如果输入0的话"[0:9:-1]"，因为是反转步长，会就0标位向左走，但是已经没有了，就会返回空列表。




print(pian)
