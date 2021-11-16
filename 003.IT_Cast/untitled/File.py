file = open("file.md", "r")
print(file.read(12))
print(file.read(22))
print("==========")
print(file.read())
file.close()

file = open("file.md")
cont = file.read()
print(cont)
file.close()

file = open("file.md", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

file = open("file.md", "r")
str = file.read()
print(len(str))
file.close()

file = open("file.md", "r")
print(len(file.readlines()))
file.close()

file = open("file.md", "r")
for line in file:
    print(line)
file.close()





print('===============')

#file = open("file.md", "r")
len(open("file.md").readlines())
