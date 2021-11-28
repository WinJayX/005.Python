
while True:
    msg = input(">:").strip()
    if not msg:continue #if len(msg) == 0 :
    # 'Hello baby, I miss you so much , want to see you , but afraid the female tiger find out ..'
    str_count = 0
    int_count = 0
    space_count = 0
    special_count = 0
    for i in msg:
        if i.isalpha():
            str_count += 1
        elif i.isdigit():
            int_count += 1
        elif i.isspace():
            space_count += 1
        else:
            print("->",i)
            special_count += 1
    print(f"str count:{str_count}, int count:{int_count}, space count:{space_count}, special count:{special_count}.")


