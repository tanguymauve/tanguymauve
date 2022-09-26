
#Modules
import random
from symbol import yield_arg

#Variables
snake = "x"
apple = "o"
x = 0
y = 0

#Intro
print("hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")

#Fonctions 
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
xApple = 0
yApple = 0
def generateApple():
    xApple = random.randrange(8)
    yApple = random.randrange(8)

#Boucle
i = 0
while True: #permet de faire une boucle demandant l'input
    deplacement() #appel la fonction pour les déplacements du snake 
    print(" ........")
    for i in range(8):
        if  i == y:
            print("|" + (x)*" " + snake + (8 - x -1)*" " + "|")
        elif i == yApple:
            print("|" + (xApple)*" " + apple + (8 - xApple -1)*" " + "|")
            if x == xApple and y == yApple:
                generateApple()
        else:
            print("|        |")
    print(" °°°°°°°°")

