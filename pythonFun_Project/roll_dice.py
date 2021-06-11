import random

quitroll = False

while (quitroll == False):
    command = input("Roll? ")
    if command == "yes" or command == "y":
        number = random.randrange(1, 7)
        print (number)
    elif command == "no" or command == "n":
        print ("Okay.")
        quitroll = True
        break
