try:
    print(1)
    print(20 / 0)
    print(2)
    print ("This code will not run")
except ZeroDivisionError:
    print(3)
finally:
    print(4)
    print ("This code will run not seem what")

try:
    with open("file.md") as f:
        print(f.read())
except:
    print("Error")

try:
    print(1)
    assert 2 + 2 == 5
except ArithmeticError:
    print(3)
except:
    print(4)