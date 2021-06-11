
queue=[]
quit = False
while not quit:
    userInput = input("Command:")
    inputs = userInput.split()
    if inputs[0] == "in" :
        queue.append(inputs[1])
    elif inputs[0] == "out":
        queue.pop(0)
    elif inputs[0] == "quit":
        quit = True
    else:
        print("Only in/out supported")

print(queue)