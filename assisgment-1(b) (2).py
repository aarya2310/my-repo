# calculator
def arith():
    while True:
        a=int(input("Enter First Element:"))
        b=int(input("Enter Second Element:"))
        print("1:add \n 2:sub \n 3:mul \n 4:div \n 5:Exit")
        c=int(input("Enter arithmetic operation to be perform:"))
        if c==1:
            print(a+b)
        elif c==2:
            print(a-b)
        elif c==3:
            print(a*b)
        elif c==4:
            print(a/b)
        elif c==5:
            print("Exiting")
            break
        else:
            print("invalid input")
arith()