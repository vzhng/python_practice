import random
Number = random.randrange(0,101)

CorrectlyGuessed = False

while (CorrectlyGuessed == False):
    Guess = int(input("Please input a number: "))
    if Guess > Number:
        print ("Too Big")
    elif Guess < Number:
        print ("Too Small")
    else:
        print ("Yay!")
        CorrectlyGuessed = True
        break



