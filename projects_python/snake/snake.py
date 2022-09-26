
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
        x += 1
        print(x)
    elif deplacement == "q":
        #x go left
        x -= 1
        print(x)
    elif deplacement == "z":
        #x go up
        y -= 1
        print(y)
    elif deplacement == "s":
        #x go down
        y += 1
        print(y)

def limit(num, minimum=1, maximum=8):
  """Limits input 'num' between minimum and maximum values.
  Default minimum value is 1 and maximum value is 8."""
  return max(min(num, maximum), minimum)

i = 0
while True: #permet de faire une boucle demandant l'input
    deplacement() #appel la fonction pour les déplacements du snake
    #while i !=y:
     #   print("|        |")
    for i in range(8):      
        if  i == y:
            print("|" + (x)*" " + snake + (8 - x -1)*" " + "|")
        else:
            print("|        |")