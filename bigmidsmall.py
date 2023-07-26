a=int(input("Input a value for A: "))
b=int(input("Input a value for B: "))
c=int(input("Input a value for C: "))
if a > b:
    if a > c:
        print("a is the greatest")
        if b > c:
            print("b is the middle")
            print("c is the least")
        else:
            print("c is the middle")
            print("b is the least")
if b > a:
    if b > c:
        print("b is the greatest")
        if a > c:
            print("a is the middle")
            print("c is the least")
        else:
            print("c is the middle")
            print("a is the least")
if c > b:
    if c > a:
        print("c is the greatest")
        if b > a:
            print("b is the middle")
            print("c is the least")
        else:
            print("a is the middle")
            print("b is the least")