stack = []
quit = False

while not quit:
    userInput = input("Command:")
    commands = userInput.split()
    if commands[0] == "push" :
        stack.append(commands[1])
    elif commands[0] == "pop" :
        if len(stack) > 0:
            stack.pop(len(stack) - 1)
        else:
            print("No Data")
    elif commands[0] == "quit" :
        quit = True
    else:
        print("Wrong Input")

print(stack)
