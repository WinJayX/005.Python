
f = open("model_contacts.txt",encoding="utf-8")

for line in f:
    if "梦竹" in line:
        print(line)