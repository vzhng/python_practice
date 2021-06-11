import random

quitplay = False
while (quitplay == False):
    computer = random.choice(['rock', 'paper', 'scissor'])
    you = input("Please input (rock, paper, scissor, quit): ")
    print (computer)

    if computer == you:
        print ("tie")

    elif computer == "rock" and you == "paper":
        print ("you win!")
    elif computer == "rock" and you == "scissor":
        print ("you lose!")

    elif computer == "paper" and you == "rock":
        print ("you lose!")
    elif computer == "paper" and you == "scissor":
        print ("you win!")

    elif computer == "scissor" and you == "paper":
        print ("you lose!")
    elif computer == "scissor" and you == "rock":
        print ("you win!")

    elif you == "quit":
        print ("Okay.")
        break
