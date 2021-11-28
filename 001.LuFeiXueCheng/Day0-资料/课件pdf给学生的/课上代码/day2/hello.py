
#
# for count in range(10):
#     print("hello, I love this world and black girl.", count)
#
# for name in ["alex","blackgirl","peiqi"]:
#     print(name)
#
# for i in "alex jack":
#     print(i)
# print(i)
# # 0 - 100
# #
# for i in range(100):
#     if i >= 50:
#         if i % 2 == 0 : # 偶数
#             print(i)

# for i in range(50,100):
#     if i % 2 == 0 : # 偶数
#         print(i)
#

# for i in range(100,50,-1):
#     if i % 2 == 0 : # 偶数
#         print(i)


for floor in range(1,7):
    print(f"当前在{floor}层".center(50,'-'))
    for room in range(1,10):
        print(f"当前房间是{floor}0{room}室.")