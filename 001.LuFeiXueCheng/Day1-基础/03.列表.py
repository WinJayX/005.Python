# 列表

girl_friend_names = ['XiaoYun', 'Xiaobian', 'xiao Xiu', 'XiaoQian', 'XiaoHua']
print(type(girl_friend_names))
print(girl_friend_names)
print(girl_friend_names[3])     # 列表取单个元素的值
girl_friend_names[3] = '小倩'     # 列表修改单个元素的值

print(girl_friend_names)


print(girl_friend_names[-1] + "    --取列表中末值")        # 取列表中末值
print(girl_friend_names[-2] + '    --取列表中末2值')        # 取列表中末2值

for girl in girl_friend_names:
    print(f'My Dira friend {girl} Happy New Years!!')


# 第二部分：增 删 改 查
# 增     list.append('string') and list.insert(i, 'string')
girl_friend_names.append('小曾')      # append 追加至末尾

print(girl_friend_names)

girl_friend_names.insert(3, '小三')
print(girl_friend_names)            # insert 插入至指定位置（i, x）插入的元素是在i的前面。


# 删 list.remove('string') and list.pop('int') and del list.[int]
girl_friend_names.remove('XiaoHua')     # 删除存在的值，类型必须是str
print(girl_friend_names)

girl_friend_names.pop(3)                # 删除存在的值，类型为int
print(girl_friend_names)

del girl_friend_names[3]                # 删除存在的值，类型为int
print(girl_friend_names)

# Q: list.pop[int] 与 del list[int] 有啥区别？


#  改 list[int] = 'string'
print(girl_friend_names[3])
girl_friend_names[3] = '增曾憎'
print(girl_friend_names[3])
# girl_friend_names['增曾憎'] = '增增增'      #错误示例，必须是int类型
# print(girl_friend_names[3])
#
# 查 list.index('string')

print(girl_friend_names[3])
print('XiaoYun' in girl_friend_names)
print('小五' in girl_friend_names)
print(girl_friend_names.index('XiaoYun'))



# 切片 [i:i:i] 顾头不顾尾

girl_friend_names.extend(['小倩', '小敏', '小芳', '小君', '小燕', '小周', '小赵'])    # 列表与列表扩展，扩展类型只能是list
print(girl_friend_names)
#
# print(girl_friend_names[:])
#
print(girl_friend_names[::3])   # 步进3位  步子的长度，默认为1


print(girl_friend_names[-3:])       # 取末尾后三位[-3:0] 0可省略


# 列表嵌套
print(girl_friend_names)
girl_friend_names.insert(3, ['丽丽', 23, 168, 22])

print(girl_friend_names)
print(girl_friend_names[3][0])
print(girl_friend_names[3][:2])
print(girl_friend_names[3][::2])
girl_friend_names[3][2] = 172

print(girl_friend_names[3])
