
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
    if deplacement == "d":
        #x go right
        x -= 1
        print(x)
    elif deplacement == "q":
        #x go left
        x += 1
        print(x)
    elif deplacement == "z":
        #x go up
        y -= 1
        print(y)
    elif deplacement == "s":
        #x go down
        y += 1
        print(y)

i = 0
while i !=9: #permet de faire une boucle demandant l'input
    deplacement() #appel la fonction pour les déplacements du snake
    while i !=y:
        print("|        |")      
    if  i == y:
        print("|", (x-1)*"", snake, (8 - x)*"", "|",)
        for i in range(8 - y):
            print("|        |")
        #for i in range(8 - x):
        #    print(' ', end='')
        #    print("|", end='')

"""
i = 1
while i != 0: #permet de faire une boucle demandant l'input 
    deplacement() #appel la fonction pour les déplacements du snake
    for c in range(8): #initialise la barre du haut
        print("-", end="") 
    for c in range(8): #imprime les barres sur le côté gauche
        print("|")
    for c in range(x): #print le serpent en bas à gauche 
        print(snake, end="")
    for c in range(8): #print la barre du bas
        #print("", "-",end="")
        print("-", end="")
    # il faut réussir à garder snake unique
    # et ensuite à faire en sorte qu'il reste sur le même axe
"""