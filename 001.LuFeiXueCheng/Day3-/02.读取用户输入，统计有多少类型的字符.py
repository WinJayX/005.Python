

while True:
    msg = input('>: ').strip()
    if not msg: continue


    str_count = 0
    digit_count = 0
    space_count = 0
    special_count = 0

    for i in msg:
        if i.isalpha():
            # print(i)
            str_count += 1
        elif i.isdigit():
            digit_count += 1
        elif i.isspace():
            space_count += 1
        else:
            special_count += 1
            # print('--->', i)

    print(f'字母有{str_count}个, 数字有{digit_count}个, 空格有{space_count}个, 特殊字符有{special_count}个')
