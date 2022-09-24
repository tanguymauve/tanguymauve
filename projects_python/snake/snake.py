
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
print(" ---------")
for i  in range(8):
    print("|         |")
print(" ---------")

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
        y += 1
        print(y)
    elif deplacement == "s":
        #x go down
        y -= 1
        print(y)
        
#print("|", end='')
#for i in range(x):
#print(' ', end='')
# print(snake, end='')
#for i in range(8 - x):
#print(' ', end='')
#print("|", end='')

i = 1
c = 1
while i != 0:
    deplacement()
    print(" ---------")
    for c in range(8):
        print("|")
    for c in range(x):
            #print("|", end="")
        print(x*"", end="")
        print(y*"", end="")
        print(snake, end="")
    print(" ---------")