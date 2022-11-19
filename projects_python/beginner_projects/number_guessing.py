import random

def create_number():
    global nombre_max
    global guess
    print("Guess the secret number")
    nombre_max = int(input("Choisis ton nombre max\n"))
    rand = random.randrange(nombre_max)
    guess = int(input("Choisis un nombre entre 0 et " + str(nombre_max) + "\n"))
    while rand != guess:
        if rand == guess:
            print("Congrats !")
        elif guess > rand:
            print("Plus petit")
        elif guess < rand:
            print("Plus grand") 
        guess = int(input("Choisis un autre nombre \n"))
        if rand == guess:
            print("Bien joué ! Le bon nombre était bien " + str(guess))
            
create_number()
