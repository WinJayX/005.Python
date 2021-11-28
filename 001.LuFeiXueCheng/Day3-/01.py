msg = 'My Name is {name}, i am {age} years old'.format(name='WinJay', age=24)
msg1 = '--My Name is {0}, i am {1} years old'.format('WinJayX', 28)

# msg.format(msg, name='WinJay', age=43)
print(msg, '\n', msg1)




#  正常有两个密码本，一方一个，但是这个密码本不是一样的，而是完全相反的。。。。。

#  所以需要生成两个密码本。

import string
source = string.printable
print(source, '源字符，用于加密')

print(len(source))

output = '''HGF@?wvpol*$#"!ZkRCBxednm  ]\[JIQhLKEg_^~}|> =<;:/jiVUT&%fc   bts210.-,+rq7654Sa9{`O('Azy3NMD8u)YXWP'''

print(output, '制作密码本用于显示的')
print(len(output))

pass_book = str.maketrans(source, output)

print(pass_book)


msg = 'Hello Babylon , I Z Y Miss You So March. I Want to see you!!'

pass_test = msg.translate(pass_book)

print('加密后的字符串显示为：', pass_test)





#  解密：
# 解密方需要再生成一个密码本，这个密码本对应的是将上面的source 及 output 进行反转，位置互换

pass_book1 = str.maketrans(output, source)
print(pass_book1)
print('\n', '\n', '\n')
print('解密后的显示文字是：', pass_test.translate(pass_book1))



