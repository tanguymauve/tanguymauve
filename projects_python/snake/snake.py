
#Modules
from os import remove
import random

#Variables
snake = "x" #Head of the snake
apple = "o" #Apple
playerCoordinateX = [0,0] #List to register every snake's x coordinate 
playerCoordinateY = [0,0] #List to register every snake's y coordinate 

#Intro
print("hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")

#Fonctions 
def deplacement():
    deplacement = input("direction :")
    if deplacement == "d" and playerCoordinateX[-1] < 7:
        #player go right
        playerCoordinateX.append(playerCoordinateX[-1] + 1)
        playerCoordinateY.append(playerCoordinateY[-1])
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])
            
    elif deplacement == "q" and playerCoordinateX[-1] > 0:
        #player go left
        playerCoordinateX.append(playerCoordinateX[-1] - 1)
        playerCoordinateY.append(playerCoordinateY[-1])
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])  
        
    elif deplacement == "z" and playerCoordinateY[-1] > 0:
        #player_x go up
        playerCoordinateX.append(playerCoordinateX[-1])
        playerCoordinateY.append(playerCoordinateY[-1] - 1)
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])
        
    elif deplacement == "s" and playerCoordinateY[-1] < 7:
        #player_x go down
        playerCoordinateX.append(playerCoordinateX[-1])
        playerCoordinateY.append(playerCoordinateY[-1] + 1)
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])
    else:
        print("The snake is not thin enough !")
        
def generateApple():
    global xApple
    global yApple
    xApple = random.randrange(8)
    yApple = random.randrange(8)

def isThatASnake():
    for i in range(len(playerCoordinateX)):  
                if x == playerCoordinateX[i] and y == playerCoordinateY[i]:
                    return True
    return False

generateApple()
while True:
    deplacement()
    #DEPLACEMENT
    print(" ........")
    for y in range(8):
        line = "|"
        for x in range(8):
            if x == xApple and y == yApple:
                    line += apple
            elif isThatASnake() :
                line += snake
            else:
                    line += " "
    #LOGIQUE
            while playerCoordinateX[-1] != xApple and playerCoordinateY[-1] != yApple:
                playerCoordinateX.pop(0)
                playerCoordinateY.pop(0)
            if playerCoordinateX[-1] == xApple and playerCoordinateY[-1] == yApple:
                generateApple()
        line += "|"
        print(line)
    print(" °°°°°°°°")
    print(playerCoordinateX)
    print(playerCoordinateY)