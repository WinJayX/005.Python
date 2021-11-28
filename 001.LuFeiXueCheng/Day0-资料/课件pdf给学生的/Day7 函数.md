## Day 7 函数

## 一、什么是函数？作用是什么？

### 1.1 引子

现在老板让你写一个监控程序，24小时全年无休的监控你们公司网站服务器的系统状况，当cpu＼memory＼disk等指标的使用量超过阀值时即发邮件报警，你掏空了所有的知识量，写出了以下代码

```python
while True：
    if cpu利用率 > 90%: #发送邮件报警
        连接邮箱服务器
        发送邮件
        关闭连接
    if 硬盘使用空间 > 90%: #发送邮件报警
        连接邮箱服务器
        发送邮件
        关闭连接
    if 内存占用 > 80%:  #发送邮件报警
        连接邮箱服务器
        发送邮件
        关闭连接
```



仅发邮件一项功能，就得至少写这么多代码：

```python
import smtplib
from email.mime.text import MIMEText # 邮件正文
from email.header import Header  # 邮件头

# 登录

smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
smtp_obj.login("nami@luffycity.com", "xxxxddddd")

# 设置邮件内容

msg = MIMEText("Hello, 小哥哥，约么？800上门，新到学生妹...", "plain", "utf-8")
msg["From"] = Header("来自娜美的问候2020","utf-8") # 发送者
msg["To"] = Header("有缘人","utf-8") # 接收者
msg["Subject"] = Header("娜美的信2021","utf-8") # 主题

# 发邮件

smtp_obj.sendmail("nami@luffycity.com", ["alex@luffycity.com"],msg.as_string())
```



上面的代码实现了功能，但即使是邻居老王也看出了端倪，老王亲切的摸了下你家儿子的脸蛋，说，你这个重复代码太多了，每次报警都要重写一段发邮件的代码，太low了，这样干存在2个问题：

1. 代码重复过多，一个劲的copy and paste不符合高端程序员的气质
2. 如果日后需要修改发邮件的这段代码，比如加入群发功能 ， 或微信通知功能，那你就需要在所有用到这段代码的地方都修改一遍

你觉得老王说的对，你也不想写重复代码，但又不知道怎么搞，老王好像看出了你的心思，笑着说，其实很简单，**只需要把重复的代码提取出来，放在一个公共的地方，起个名字，以后谁想用这段代码，就通过这个名字调用就行了**，如下

```python
def 发送邮件(内容):
    #发送邮件提醒
    连接邮箱服务器
    发送邮件
    关闭连接
while True：
    if cpu利用率 > 90%:
        发送邮件('CPU报警')
    if 硬盘使用空间 > 90%:
        发送邮件('硬盘报警')
    if 内存占用 > 80%:
        发送邮件('内存报警')
```

你看着老王写的代码，气势恢宏、磅礴大气，代码里透露着一股内敛的傲气，心想，老王这个人真是不一般，突然对他的背景更感兴趣了，问老王，这些花式玩法你都是怎么知道的？ 老王亲了一口你儿子，捋了捋不存在的胡子，淡淡的讲，“老夫，年少时，师从京西沙河淫魔银角大王 ”， 你一听“银角大王”这几个字，不由的娇躯一震，心想，真nb,怪不得代码写的这么6, 这“银角大王”当年在江湖上可是数得着的响当当的名字，只可惜后期纵欲过度，卒于公元2021年， 真是可惜了，只留下其哥哥孤守当年兄弟俩一起打下来的江山。 此时你看着的老王离开的身影，感觉你儿子跟他越来越像了。。

### 1.2 函数是什么？

函数一词来源于数学，但编程中的「函数」概念，与数学中的函数是有很大不同的，具体区别，我们后面会讲，编程中的函数在英文中也有很多不同的叫法。在BASIC中叫做subroutine(子过程或子程序)，在Pascal中叫做procedure(过程)和function，在C中只有function，在Java里面叫做method。

**定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可**

**特性:**

1. 减少重复代码
2. 使程序变的可扩展
3. 使程序变得易维护

### 1.3 语法定义

```python
def sayhi(): # 函数名
    print("Hello, I'm nobody,  valar morghulis")
sayhi() # 调用函数
```

#### 参数和返回值

带参数

```python
def sayhi(name): # 函数名
    print(f"Hello, I'm {name},  valar morghulis")


names = ["Alex", "Peiqi","BlackGirl","Celina", "XiaoYun"]

for i in names:
    sayhi(i)
```

形参和实参

![image-20210523170726916](/Users/alex/Documents/路飞学城/B站内容营销/2021 PY大课/课件/Day6 函数.assets/image-20210523170726916.png)

**形参变量**： 只有在函数被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只在函数内部有效。函数调用结束返回后则不能再使用该形参变量

**实参**：可以是常量、变量、表达式、函数等，无论实参是何种类型的量，在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参，因此应预先给实参赋值



#### 返回值

当你想要得到函数的执行结果时，就可用`return`语法把数据返回给函数外部

```python
def mobile_check(phone_num):
    if len(phone_num) == 11:
        if phone_num.isdigit():
            if phone_num.startswith('1'): # 1开头
                return True

s = '13651054609'
if mobile_check(s): # 结果是True
    print("合法手机号...")
```

特点：

1. 默认返回值就None, 
2. 可返回任意数据类型
3. 可返回多个值 

```python
def stu_registriation_form():
    form = {
        "name": input("Name:").strip(),
        "age": input("Age:").strip(),
        "phone": input("Phone:").strip()
    }

    info_pass_flag = True  # 如果字段全填了，就是True
    for k, v in form.items():
        if len(v) == 0:  # 没写东西
            info_pass_flag = False
            break

    return form, info_pass_flag


stu_info, flag = stu_registriation_form() # 接收2个值 
print(stu_info)
print(flag)
```



## 二、 函数参数

### 2.1 传值类型

可以把任意值做为参数传递给函数，这些值可整体分为2种，可变类型、不可类型，2种值传给函数，在函数里修改时，产生的效果不同

##### 不可变类型做参数

在函数内修改外部传进来的不可变类型时， 会在函数内部生成一个该参数的copy , 并不会影响原来函数外部的值 

##### 可变类型做参数

可变类型，如列表、dict, 传到函数内部，其实只是传递了该列表\dict的整体内存地址，函数内部可直接修改函数外部的这个list or dict . 

```python
def change_data(name,hobbies):
    name = "Alex"   # 修改只在函数内生效
    hobbies.append("大保健")  # 在函数内往外部列表添加值 
    hobbies[1] = "XiaoYun"   # 修改列表元素
    print("in func:",name,hobbies)


my_name = "金角大王" # 不可变类型
my_hobbies = ["Money","BlackGirl"] # 可变类型
change_data(my_name,my_hobbies)
print(my_name,my_hobbies)
```

执行结果：

> in func: Alex ['Money', 'XiaoYun', '大保健']
> 金大王 ['Money', 'XiaoYun', '大保健']

*列表被函数修改了，而外面的字符串并无变化 



### 2.2 函数参数类型

#### 必备参数（位置参数）

- 必备，不传值会报错
- 传的值是有顺序的，从左到右，每个参数一一对应

<img src="/Users/alex/Documents/路飞学城/B站内容营销/2021 PY大课/课件/Day6 函数.assets/image-20210524170055265.png" alt="image-20210524170055265" style="zoom: 33%;" />

#### 关键字参数

- 赋值时指定参数名，不按位置顺序了
- 如果和必备参数混用，必须放在位置参数后边（看后边例子）

```python
def stu_form(name, age, major, phone):
    info = f'''
    Name : {name},
    Age  : {age},
    Major: {major},
    Phone: {phone}
    '''
    print(info)
stu_form(major="Computer Science", name="Alex", phone=13334, age=22)
```

输出：

```
Name : Alex,
Age  : 22,
Major: Computer Science,
Phone: 13334
```

**和位置参数混用**

若这样调用`stu_form(major="Accounting", age=24, "BlackGirl",13444)`  会报错的。

```
/usr/local/bin/python3.9 /Users/alex/PycharmProjects/alex96_daydayup/day7/参数类型.py
  File "/Users/alex/PycharmProjects/alex96_daydayup/day7/参数类型.py", line 12
    stu_form(major="Accounting", age=24, "BlackGirl",13444)
                                                          ^
SyntaxError: positional argument follows keyword argument  
```

因为你先指定了2个关键参数，后边的位置参数就不知道应该跟实际哪个参数对应了， 像`BlackGirl`是代表`name`呢还是`phone`呢？ 说不清的， 所以，如果出现 混用，位置参数必须放在最左边, 关键参数后边禁止跟位置参数：

```python
stu_form( "BlackGirl",  major="Accounting", age=24, phone='1445533' ) # 这样ok 
```



#### 默认参数

对于一些调用时非必选的参数，可设置成默认参数，这样，即使用户不填，也不影响函数正常运行。 

```python
def stu_form(name, age, major, phone, nationality='CN'):
    info = f'''
    Name : {name},
    Age  : {age},
    Major: {major},
    Phone: {phone},
    Nation: {nationality}
    '''
    print(info)


stu_form( "BlackGirl",  major="Accounting", age=24, phone='1445533',nationality='JP')  
stu_form( "Alex",  major="IT", age=25, phone='1334444') 
```

上边，`BlackGirl` 指定了nationality='JP', 那就按指定的，`Alex`未指定，则用默认`CN` 

#### 不定长参数

有时， 我们在设计函数时，可能只定了固定数量的参数， 但过了一段时间，有新需求了， 需要再加2个参数，这时候你就要改源代码，一改源代码就需要重新进行测试环境 、预生成环境的各种严格的测试流程，没问题后，再能再重新部署到生产系统。 如果能一开始设计时 就留好后期扩展的空间，就省事了，也提高了程序的可扩展性。  

这就可用不定长参数来实现， 共2种方式，`*args` 和`**kwargs` 

##### *args  元组传值

多给的值 ，都会给到*args参数里，以元组形式

```
def stu_form(name, age, major, phone, nationality='CN',*args):
    info = f'''
    Name : {name},
    Age  : {age},
    Major: {major},
    Phone: {phone},
    Nation: {nationality}
    '''
    print(info)
    print("不定长列表参数:",args)


stu_form("XiaoYun",23,"Finance",13332,"Thailand",'Alex','Movies') #多写了最后2个参数
```

输出

```bash
Name : XiaoYun,
Age  : 23,
Major: Finance,
Phone: 13332,
Nation: Thailand
不定长列表参数: ('Alex', 'Movies') 
```

##### **kwargs 字典传值

接收多余的关键字参数，并以dict形式给到kwargs

```
def stu_form(name, age, major, phone, nationality='CN',*args,**kwargs):
    info = f'''
    Name : {name},
    Age  : {age},
    Major: {major},
    Phone: {phone},
    Nation: {nationality}
    '''
    print(info)
    print("不定长列表参数:",args,kwargs)


stu_form("XiaoYun",23,"Finance",13332,"Thailand",'Alex','Movies', hometown="HeNan",university="BeiDaQingNiao") # 多写了hometown, university 2个指定参数
```

输出

```python
Name : XiaoYun,
    Age  : 23,
    Major: Finance,
    Phone: 13332,
    Nation: Thailand
    
不定长列表参数: ('Alex', 'Movies') {'hometown': 'HeNan', 'university': 'BeiDaQingNiao'}
```

##### 直接传列表or dict 

直接按下面这种方式 传也可以， 但要加上* 和**符号， 输出效果跟上面一样。

```python
info = {'hometown':"河南",'university':"北大青鸟"}
hobbies = ["Alex",'Movies',"LiveHouse"]

stu_form("XiaoYun",23,"Finance",13332,"Thailand",'Alex','Movies',*hobbies,**info)
```



## 三、函数嵌套

列表里可以嵌入子列表、字典里可嵌入子字典，函数里也可以嵌子函数

子函数只能在父函数内部调用 。

```python
def stu_form():

    form = {
        "name": input("Name:").strip(),
        "age": input("Age:").strip(),
        "major": input("Major:").strip(),
        "phone": input("Phone:").strip()
    }

    print(form)
    # 下面边个子函数，是写了一个可以改form dict值 的功能
    def change_form(form_data):  # 这个函数只能在stu_form内调用
        print(form_data.keys())
        print("--------------修改信息--------------")
        while True:
            key = input("输入要改的key>:").strip()
            if not key:continue
            if key in form_data.keys():
                print(f"({key})的当前值{form_data[key]}")
                key_new_val = input("输入要改的新值:").strip()
                form_data[key] = key_new_val
                break
            else:
                print("不合法的key...")

    change_form(form) # 内部调用 
    print("new form:",form) 

    return form

stu_form()
```

以后学装饰器时，嵌套函数大有用途，现在你先知道它的用法就行



## 四、全局变量 VS 局部变量

在函数内部声明的变量叫局部变量， 它只在函数内部生效，函数执行结束后，该变量也行将消亡

```python
def change_name():
    name = "Alex" # 局部变量，只在函数内部生效
    print("in func:", name)

name = "金角大王"  # 全局变量， 整个代码文件全局生效

change_name()
print("global var:",name)
```

输出

```
in func: Alex
global var: 金角大王
```

为什么在函数内部改了name的值后， 在外面print的时候却没有改呢？ 因为这两个name根本不是一回事

- 在函数中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
- 全局变量作用域(即有效范围)是整个程序，局部变量作用域是定义该变量的函数。
- 变量的查找顺序是**局部变量>全局变量**
- 当全局变量与局部变量同名时，在定义局部变量的函数内，局部变量起作用；在其它地方全局变量起作用。
- 在函数里是不能直接修改全局变量的

目前函数内部的name变量, 和外部的name没任何关系 ， 是存活在2个内存空间里的。 就像你们2个村子里都有个叫`尼古拉.赵四` 一样。 

如果想在函数内部，修改外面的`name`变量怎么办呢？ 

#### globa声明全局变量

globa 语法告诉解释器， 我要在函数内部引用并修改全局变量

```python
def change_name():
    global name # 声明要引用全局变量
    name = "Alex" # 这时是改的全局变量
    print("in func:", name)

name = "金角大王"  # 全局变量， 整个代码文件全局生效

change_name()
print("global var:",name)
```

```
in func: Alex
global var: Alex
```

## 五、匿名函数lambda

匿名函数就是不需要显式的指定函数名的函数

啊？？？

<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fim6.leaderhero.com%2Femotion%2F5905%2F1838368257%2F5e39ee3c31.jpg&refer=http%3A%2F%2Fim6.leaderhero.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1624937537&t=edd5b165302cb3a17bc40c888d892745" alt="img" style="zoom:33%;" />

```python
>>> func = lambda x,y:x*y   
>>> func(8,9)
72

# 相当于传统函数
def func(x,y):
  return x*y 
```

注意`lambda`后边的代码，一般只写一行，不能像传统函数一样，写很多行。

匿名函数有啥用？ 

就是为了省事，有的时候 只为了实现个简单的功能，懒得再单独写一个函数，就可用匿名函数。 一般会搭配在各种其它方法里使用。 

啊？？什么意思？ 跟谁搭配？ 

先说一个我们一会会学的内置函数`map`吧， 

map的作用就是，把一个可遍历的数据集扔给map, map用指定的函数对该数据集的每个值进行处理，下面的例子是把每个值+1

```python
def add_one(n):
  return n+1
li = [9,11,2,3,4,8,19,12,30]
print(list(map(add_one, li))) # 给列表里每个值+1 , 用传统函数


print(list(map(lambda n:n+1, li))) # 给列表里每个值+1
```



## 六、高阶函数

变量可以指向函数名，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

```python
>>> def get_square(n): # 
...     """求平方"""
...     return n*n
... 
>>> 
>>> 
>>> get_square   
<function get_square at 0x7fdfe018f160>
>>> f = get_square # 把一个函数名，赋值给变量
>>> f(3)  
9

```

把函数当作参数，传递给另一个函数

```python
def get_abs(n):
    if n < 0 :
        n = int(str(n).strip("-"))
    return n
  
def add(x,y,f):
    return f(x) + f(y)
res = add(3,-6,get_abs)
print(res)
```

只需满足以下任意一个条件，即是高阶函数

- 接受一个或多个函数作为输入
- return 返回另外一个函数

## 七、递归

### 7.1 递归是什么？

先看例子：

求100不断除以2直到商为0为止，打印每次除的商， 用循环实现

```python
n = 100
while n > 0:
    n = int(n/2)
    print(n)
```

输出：

50

25

12

6

3

1

0

如果用函数，怎么实现呢？ 

```python
def divide_calc(n):
    print(n)
    if n > 0 :
        divide_calc(int(n/2))  # 只需重复调用一次自己就可

divide_calc(10)
```

##### 递归定义

在函数内部，可以调用其他函数。**如果一个函数在内部调用自已本身，这个函数就叫做递归函数**。上面我们写的这个代码就是递归

#### 7.2 递归的执行过程

```python
def divide_calc(n):
    print(n)
    if n > 0 :
        divide_calc(int(n/2))
    return n
res = divide_calc(10)
print(res)
```

输出：

> 10
> 5
> 2
> 1
> 0
> 10

为何最后有个10？ 

![img](/Users/alex/Documents/路飞学城/B站内容营销/2021 PY大课/课件/Day6 函数.assets/chapter3-.png)

如上图所示，函数在每进入下一层的时候，当前层的函数并未结束，它必须等它调用的下一层函数执行结束返回后才能继续往下走。 所以最下面的那句`return n`会等最里层的函数执行时才会执行，然后不断往外退层，所以最后一次的`return n`执行的是最外层调用函数的， 那个n一开始就是10

![image-20210606182016801](/Users/alex/Documents/路飞学城/B站内容营销/2021 PY大课/课件/Day7 函数.assets/image-20210606182016801.png)

**递归特性:**

1. 必须有一个明确的结束条件()
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3. 递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）

递归在特定场景下还是挺有用的，以后学的一些算法就得用到递归，比如堆排、快排等，现在看还是有些复杂的，以后再讲。



## 练习题

用递归实现2分查找的算法，以从列表 a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107] 查找指定的值。









注：参考答案，但尽量先自己写。

```python
a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107]


def b_search(start,end,li,find_n):

    mid_index = int( (start + end ) / 2 ) # 每次找到列表中间的位置的索引
    if len(li[start:end]) == 1: # 碰头了，查完了
        if li[start] != find_n: # 完了，找不到了
            print("找不到该值.")
            return
        else:
            print("找到了，",li[start])
            return
    if li[mid_index] > find_n: # the val you looking for should be in the left part
        print("去左边一半的数据里查:",li[mid_index], li[start:mid_index])
        b_search(start,mid_index,li,find_n)
    else: # val in right
        print("去右边一半的数据里查:",li[mid_index], li[mid_index:end])
        b_search(mid_index,end,li,find_n)

b_search(0,len(a)-1,a,38)
```





## 八、内置函数

Python的`len()  、 print()` 等方法 为什么你可以直接用？肯定是解释器启动时就定义好了。为了提高你的开发效率，Python内置了很多已经可用的函数，你可以直接调用 



下图是所有所内置函数列表，除了为师打`x`号的，其它的你都应该会用。。。

![image-20210602144943700](/Users/alex/Documents/路飞学城/B站内容营销/2021 PY大课/课件/Day6 函数.assets/image-20210602144943700.png)

内置参数详解https://docs.python.org/3/library/functions.html?highlight=built#ascii

```python
abs # 求绝对值
all #Return True if bool(x) is True for all values x in the iterable.If the iterable is empty, return True.
any #Return True if bool(x) is True for any x in the iterable.If the iterable is empty, return False.
ascii #Return an ASCII-only representation of an object,ascii(“中国”) 返回”‘\u4e2d\u56fd’”
bin #返回整数的2进制格式
bool # 判断一个数据结构是True or False, bool({}) 返回就是False, 因为是空dict
bytearray # 把byte变成 bytearray, 可修改的数组
bytes # bytes(“中国”,”gbk”)
callable # 判断一个对象是否可调用
chr # 返回一个数字对应的ascii字符 ， 比如chr(90)返回ascii里的’Z’
classmethod #面向对象时用，现在忽略
compile #py解释器自己用的东西，忽略
complex #求复数，一般人用不到
delattr #面向对象时用，现在忽略
dict #生成一个空dict
dir #返回对象的可调用属性
divmod #返回除法的商和余数 ，比如divmod(4,2)，结果(2, 0)
enumerate #返回列表的索引和元素，比如 d = [“alex”,”jack”]，enumerate(d)后，得到(0, ‘alex’) (1, ‘jack’)
eval #可以把字符串形式的list,dict,set,tuple,再转换成其原有的数据类型。
exec #把字符串格式的代码，进行解义并执行，比如exec(“print(‘hellworld’)”)，会解义里面的字符串并执行
exit #退出程序
filter #对list、dict、set、tuple等可迭代对象进行过滤， 例子：filter(lambda x:x>10,[0,1,23,3,4,4,5,6,67,7])过滤出所有大于10的值
float #转成浮点
format #没用
frozenset #把一个集合变成不可修改的
getattr #面向对象时用，现在忽略
globals #打印全局作用域里的值
hasattr #面向对象时用，现在忽略
hash #hash函数
help
hex #返回一个10进制的16进制表示形式,hex(10) 返回’0xa’
id #查看对象内存地址
input
int
isinstance #判断一个数据结构的类型，比如判断a是不是fronzenset, isinstance(a,frozenset) 返回 True or False
issubclass #面向对象时用，现在忽略
iter #把一个数据结构变成迭代器，讲了迭代器就明白了
len
list
locals  # 打印所有的局部变量
map # map(lambda x:x**2,[1,2,3,43,45,5,6,]) 输出 [1, 4, 9, 1849, 2025, 25, 36]
max # 求最大值
memoryview # 一般人不用，忽略
min # 求最小值
next # 生成器会用到，现在忽略
object #面向对象时用，现在忽略
oct # 返回10进制数的8进制表示
open
ord # 返回ascii的字符对应的10进制数 ord(‘a’) 返回97，
print
property #面向对象时用，现在忽略
quit
range
repr #没什么用
reversed # 可以把一个列表反转
round #可以把小数4舍5入成整数 ，round(10.15,1) 得10.2
set
setattr #面向对象时用，现在忽略
slice # 没用
sorted # 
staticmethod #面向对象时用，现在忽略
str
sum #求和,a=[1, 4, 9, 1849, 2025, 25, 36],sum(a) 得3949
super #面向对象时用，现在忽略
tuple 
type
vars #返回一个对象的属性，面向对象时就明白了
zip #可以把2个或多个列表拼成一个， a=[1, 4, 9, 1849, 2025, 25, 36]，b = [“a”,”b”,”c”,”d”]，
  list(zip(a,b)) #得结果 
  [(1, 'a'), (4, 'b'), (9, 'c'), (1849, 'd')]
```

#### 几个刁钻古怪的内置方法用法提醒

```python
#compile
  f = open("函数递归.py")
  data =compile(f.read(),'','exec')
  exec(data) 

#print
  msg = "又回到最初的起点"
  f = open("tofile","w")
  print(msg,"记忆中你青涩的脸",sep="|",end="",file=f)
```





## 九、本日作业



### 员工信息修改程序

在一个文件里存多个人的个人信息，如以下

```py
username,password,age,position,department,phone
alex,abc123,30,Engineer,IT,13651830433
rain,df2@432,25,Teacher,Teching,18912334223
黑姑娘,df2@432,26,行政,人事,13811177306
```

需求：

1.输入用户名密码，正确后登录系统 ，打印

```py
1. 修改个人信息
2. 打印个人信息
3. 修改密码
```

2. 每个选项写一个方法
3. 当用户选择1时，提示用户选择要修改的字段，根据用户输入对相应字段进行修改
4. 登录时输错3次退出程序

执行时应该达到的效果参考：

`python 个人信息修改练习.py`

```py
Username:alex
Password:abc123
-------------------welcome alex --------------------
1. 打印个人信息
2. 修改个人信息
3. 修改密码
>>>1
    ------------------
    Name:   abc123
    Age :   30
    Job :   Engineer
    Dept:   Sales
    Phone:  13651830433
    ------------------
1. 打印个人信息
2. 修改个人信息
3. 修改密码
>>>2
person data: ['alex', 'abc123', '30', 'Engineer', 'Sales', '13651830433']
0.  Username: alex
1.  Password: abc123
2.  Age: 30
3.  Job: Engineer
4.  Dept: Sales
5.  Phone: 13651830433
[select column id to change]:4
current value>: Sales
new value>:Marketing
['alex', 'abc123', '30', 'Engineer', 'Marketing', '13651830433']
1. 打印个人信息
2. 修改个人信息
3. 修改密码
>>>q
bye.
```

代码提示：

![img](/Users/alex/Documents/路飞学城/B站内容营销/2021 PY大课/课件/Day6 函数.assets/image.png)

