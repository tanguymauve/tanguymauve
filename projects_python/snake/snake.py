
#créer le terrain de jeu, avec des limites à ne pas dépasser
#créer un serpent
#lui donner 4 mouvements : haut bas gauche droite décidé par l'utilisateur
#faire en sorte que le serpent puisse tout le temps bouger
#lui donner une pomme à manger qui peut apparaître partout
snake = "x"
apple = "o"
print("hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")
print(" ---------")
for i  in range(8):
    print("|         |")
print(" ---------")

def deplacement():
    deplacement = input("direction :")
    if deplacement == "d":
        #x go right
        print("d")
    elif deplacement == "q":
        #x go left
        print("q")
    elif deplacement == "z":
        #x go up
        print("z")
    elif deplacement == "s":
        #x go down
        print("s")

i = 1
while i != 0:
    deplacement()
    print(" ---------")
    for i  in range(8):
        print("|         |")
    print(" ---------")