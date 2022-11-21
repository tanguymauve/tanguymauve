import random
import math

def dice_roll():
    global nombre_max
    global nombre_de_dé
    global rand
    global guess
    global dice_sum
    rand = []
    nombre_de_dé = int(input("Choisis ton nombre de dés\n"))
    nombre_max = int(input("Choisis le nombre de face\n"))
    print("\n")
    for i in range(nombre_de_dé):
        rand.append(random.randrange(nombre_max))
        dice_sum = math.fsum(rand)
    print(str(rand))
    print("\n")
    print(dice_sum)
        

dice_roll()