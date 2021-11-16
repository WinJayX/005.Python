squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(len(squares))
print(squares[4:9])
print(squares[0:1])

sqs = [0,1,4,9,16,25,36,49,64]
print(len(sqs))
print(sqs[4:7])

print(squares[:7])

print(squares[4:])

print("============")

print(squares[::2])
print(squares[2:8:3])

print(squares[1::4])


print(squares[::-1])


squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[7:5:-1])
#先保留原有Key值，再进行翻转，然后取出对应的Key的值 运行为:49,36