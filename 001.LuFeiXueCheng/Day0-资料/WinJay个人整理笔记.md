### 1.2 格式化⽅法

```bash
s.capitalize( ⾸字符改成⼤写
s.casefold( 为了⽅便字符串之前对⽐，都改成⼩写
s.center( 字符串两边填充
s.expandtabs( 将代码中的\t转换成Tab形式显示，可定义=多少个空格。		# 默认是8个空格
s.ljust( 字符串左边填充
s.rjust( 字符串右填充
s.lower( 全变⼩写
s.swapcase( ⼤⼩写互换
s.title( 改成标题，即每个单词⾸字⺟⼤写
s.upper( 改⼤写
s.zfill( 字符串空的地⽅填0
s.strip( 两边去空，中间的不去。
s.lstrip( 左边去空
s.rstrip( 右边去空
s.format( 引⽤外部变量
```

### 1.3 字符串判断

```
s.startswith(
s.endswith(

s.isalpha( 是不是字⺟
s.isalnum( 是不是字⺟or数字. 两个条件，是不是字母或数字，有一个满足即True

s.isdigit( 是不是整数字，不能判断小数
s.isidentifier( 是不是合法的可以做变量的名字
s.islower( 判断是否是小写
s.isnumeric( 是不是数字，跟isdigit有何关系 呢？ 支持中文的数字形式。
s.isprintable( 是否可打印
s.isspace( 是不是空格
s.istitle( 首字母是不是都是大写
s.isupper(	是不是都是大写 



s.isascii( 暂不⽤，没学
s.isdecimal( 不要⽤， 垃圾
```

### 1.4 字符串查找&计数&修改&替换

```bash
s.find(		查
s.rfind(	右边查

s.index(	取索引
s.rindex(	右边取索引

s.count(	计数，统计某个字符出现的次数

s.split( 将字符串转换成列表，默认使用空格切片
s.rsplit(	配合maxsplit=4使用，在右边开始，分成4个元素
s.splitlines(	可以将带有\n的字符串以\n为间隔进行切割生成列表

s.removeprefix(	去掉前面指定的字符
s.removesuffix(	去掉后面指定的字符

s.replace( 指定字符串替换。（'old', 'new'）
```

### 1.5 特殊变态⽅法

```bash
s.encode( 字符编码相关，还没学
'-'.join(list)	把列表 转成字符串，每个元素拼接起来，按指定格式

s.maketrans( ⽣成密码本
s.translate( 加密,解密也是此方法
```

### 1.6 练习：统计⼀段话各类字符的个数



### 1.7 练习：开发⼀个加密程序







## ⼆、列表精讲

### 列表特性
有序 有索引、可切⽚、可遍历

### 2.1 增

names.append(
names.insert(
2.2 删除
names.clear(
names.pop(
names.remove(
del names
