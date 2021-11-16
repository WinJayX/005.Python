def test1():
    print("===========这是test1函数===========")


def test2():
    print("+++++++++++这是test2函数+++++++++++")
    test1()     # 调用test1函数

# test2()


def FenGeXian(char, num):
    """

    :param char:
    :param num:
    """
    print(char * num)
FenGeXian("&", 20)




def wuhang(char, num):
    """打印多行分隔线

    :param char: 分隔线使用的字符
    :param num: 分隔线打印的次数
    """
    i = 0
    while i < 1:
        FenGeXian(char, num)
        i += 1
wuhang("^", 60)


list = [86, 98, 6, 4, 3, 2345, 6, 98, 6, 678, 45]
# list.sort()
list.append(34)
list.remove(4)
print(list.index(678))
list.clear()
# list.sort(reverse=True)
# list.reverse()
print(list)

# x = list.count(6)
print(len(list))
#






