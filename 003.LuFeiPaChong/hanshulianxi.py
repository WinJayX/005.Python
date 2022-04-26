
def ma(ren, level):


    print('1.你瞅啥？',ren)
    print('2.严正交涉',ren)
    if level < 10:
        print('快点儿滚吧。。。')
    else:
        print('3.开始骂功')
        print('4.骂死你吖')
    print('5.骂完收工')

#ma('张三',13)


# 四则运算

def yunsuan(a, opt, b):

    if opt == '+':
        return (a + b)
    elif opt == '-':
        return (a - b)
    elif opt == '*':
        return (a * b)
    elif opt == '/':
        return (a / b)
    else:
        print('运算错误。。。这是四则运算')

result = yunsuan(388, '+', 176)
print(result * 2)


# yunsuan(388, '-', 176)
# yunsuan(388, '*', 176)
# yunsuan(388, '/', 176)
# yunsuan(388, '&', 176)




# 参数排序

### 位置参数  > *args > 默认参数 > **kwargs

def test(a, b, *args, c='haha', **kwargs):
    print(a,b,args, c,kwargs)

# test(3.3,4,2,66,5,5,3,42,2,2,54,5,34,53,65,3,c='hehe',d=4,e=6,t=9)




