import random
from time import sleep

def opponent_move():
    global comp_move
    global my_move
    global my_score
    my_score = 0
    global comp_score
    comp_score = 0
    for i in range(3):
        moves = ["rock", "paper", "scissors"]
        comp_move = random.choice(moves)
        my_move = input("What's your move ? \n")
        while my_move != "rock" and my_move != "paper" and my_move != "scissors":
            print("This is not a valid move\n")
            my_move = input("What's your move ? \n")
        print("1 \n")
        sleep(0.5)
        print("2 \n")
        sleep(0.5)
        print("3 \n")
        sleep(0.5)
        print("rock \n")
        sleep(0.5)
        print("paper \n")
        sleep(0.5)
        print("scissors! \n")
        sleep(0.5)
        print("Your opponent played " + comp_move)
        sleep(2)
        if my_move == "rock" and comp_move == "rock":
            print("Equality")
        elif my_move == "rock" and comp_move == "paper":
            print("Loss")
            comp_score += 1
        elif my_move == "rock" and comp_move == "scissors":
            print("Win")
            my_score += 1
        elif my_move == "paper" and comp_move == "rock":
            print("Win")
            my_score += 1
        elif my_move == "paper" and comp_move == "scissors":
            print("Loss")
            comp_score += 1
        elif my_move == "paper" and comp_move == "paper":
            print("Equality")
        elif my_move == "scissors" and comp_move == "paper":
            print("Win")
            my_score += 1
        elif my_move == "scissors" and comp_move == "rock":
            print("Loss")
            comp_score += 1
        elif my_move == "scissors" and comp_move == "scissors":
            print("Equality")
        print(str(my_score) + " / " + str(comp_score))

print("Welcome to rock paper scissors. Game in three. Good luck.")
opponent_move()
print
if comp_score > my_score : 
    print("The computer win")
elif comp_score < my_score:
    print("You win !")
else:
    print("It's a tie.")