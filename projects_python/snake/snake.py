
#créer le terrain de jeu, avec des limites à ne pas dépasser
#créer un serpent
#lui donner 4 mouvements : haut bas gauche droite décidé par l'utilisateur
#faire en sorte que le serpent puisse tout le temps bouger
#lui donner une pomme à manger qui peut apparaître partout
snake = "x"
apple = "o"
x = 0
y = 0
print("hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")

def deplacement():
    global x
    global y 
    deplacement = input("direction :")
    if deplacement == "d" and x <= 6:
        #x go right
        x += 1
        print(x)
    elif deplacement == "q" and x >= 1:
        #x go left
        x -= 1
        print(x)
    elif deplacement == "z" and y >= 1:
        #x go up
        y -= 1
        print(y)
    elif deplacement == "s" and y <= 6:
        #x go down
        y += 1
        print(y)
    elif x == 7 or y ==7 or x == 0 or y == 0:
        print("The snake is not thin enough !")
        print(x)

i = 0
while True: #permet de faire une boucle demandant l'input
    deplacement() #appel la fonction pour les déplacements du snake
    print(" ........")
    for i in range(8):      
        if  i == y:
            print("|" + (x)*" " + snake + (8 - x -1)*" " + "|")
        else:
            print("|        |")
    print(" °°°°°°°°")