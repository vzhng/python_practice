import re

quit = False
while (quit == False):
    x = input("Please input an equation: ")

    if x == "q":
        quit = True
        print ("Bye")
        break

    z = re.search("^([\.\d]+)\s*([\+,\-,\*,/])\s*([\.\d.]+)$", x)
    print (z)

    assert z != None, "Please enter correct equation."

    num1 = float(z.group(1))
    num2 = float(z.group(3))
    op = z.group(2)
    # print (num1)
    # print (num2)
    # print (op)

    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "*":
        print (num1 * num2)
    elif op == "/":
        assert num2 != 0, "Dividend should not be 0."
        print (num1 / num2)
    else:
        print ("Unknown operator", op)


