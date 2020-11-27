#字符串特性：0.有序 1.取值、取索引 2.切片--属于列表的一个特性--s[3:6]从第3 个位置开始切，一直切到第6 个位置，也是顾头不顾尾，实际切到5. 3.不可变--不能进行修改字符串里面的内容。。
str = "Hello whart are doing now?"
name = "WinJayX"
num = "34243324234"

print(str.count("a"))                   # count 统计某个字符出现的次数
print(str.upper())                      # upper 将字符串全部转换成大写
print( len( str ) )                     # len 统计字符串有多少个字符
print(str.find("l"))                    # find查找第一个找到的字符的位置，返回索引值
print(str[6])                           # [n]     取第6个索引位置的字符串内容
print(str[3:7])                         # [n:n]   切片，从第3个索引位置切到到7个索引位置，顾头不顾尾。
print(str[-3:])                         # [-n:]   切片，倒着切，取后末尾的值  忽略即取到最后一位
print(str[-3:-1])                       # [-n:-n] 切片，倒着切，取后末尾的值  还是顾头不顾尾 写是-1位，即忽略了最后一位了
print(str.endswith("now?"))             # endswith   判断是否是以某个值结尾   返回布尔值
print(str.startswith("Hell"))           # startswith 判断是否是以某个值开始   返回布尔值
print(name.center(50, "-"))             # center 将字符串居中，并以指定数量的指定符号占位。###！！！注意先写数字再填符号
print(num.isdigit());    print(name.isdigit())  # isdigit 判断字符串是不是整数，返回布尔值
print("/".join(str+name+num))           # join 将一个字符串中的每个字符都用指定的符号拼接，如果指定符号为空，则可以拼接字符串
print("".join(str+name+num))            # join 如果指定符号为空，则可以拼接字符串。。
print(str.replace("now", "tomorrow"), end=""); print(str)   # replace 替换字符串中的某个值但并不是修改，后面的str仍是原来的值

#  Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
print(str.split())                      # split 默认以空格为分隔符，包含\n也当成分隔符 # split
print(str.split("o"))                   # split 以“o”为分隔符，返回的数组中的单词就不包含分隔符了
print(str.split("o", 2))                # split 有指定分隔的字符串数，为n+1 个

print(str.strip("?"))                   # strip 删除字符串头及尾部指定的字符，默认为空格


