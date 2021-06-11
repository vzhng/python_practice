quit = False
while (quit == False):
    x = input("Please input an equation with spaces: ")

    if x == "q":
        quit = True
        print ("Bye")
        break

    y = x.split()

    assert len(y) == 3, "Need space between 3 inputs!"

    num1 = float(y[0])
    num2 = float(y[2])
    op = y[1]

    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "x":
        print (num1 * num2)
    elif op == "/":
        print (num1 / num2)
    else:
        print ("Unknown operator", op)

