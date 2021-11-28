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
