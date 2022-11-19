import random
from time import sleep

#ajouter un score

def opponent_move():
    global comp_move
    global my_move
    moves = ["rock", "paper", "scissors"]
    comp_move = random.choice(moves)
    my_move = input("What's your move ? \n")
    if my_move != "rock" and my_move != "paper" and my_move != "scissors":
        print("This is not a valid move")
        return
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
    elif my_move == "rock" and comp_move == "scissors":
        print("Win")
    elif my_move == "paper" and comp_move == "rock":
        print("Win")
    elif my_move == "paper" and comp_move == "scissors":
        print("Loss")
    elif my_move == "paper" and comp_move == "paper":
        print("Equality")
    elif my_move == "scissors" and comp_move == "paper":
        print("Win")
    elif my_move == "scissors" and comp_move == "rock":
        print("Loss")
    elif my_move == "scissors" and comp_move == "scissors":
        print("Equality")
    
opponent_move()