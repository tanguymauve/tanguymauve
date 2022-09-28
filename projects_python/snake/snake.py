
#Modules
from os import remove
import random

#Variables
snakeHead = "x" #Head of the snake
apple = "o" #Apple
playerCoordinateX = [0] #List to register every snake's x coordinate 
playerCoordinateY = [0] #List to register every snake's y coordinate 
eatenApple = 0

#Intro
print("hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")

#Fonctions 
def deplacement():
    deplacement = input("direction :")
    if deplacement == "d" and playerCoordinateX[-1] <= 6:
        #player go right
        playerCoordinateX.append(playerCoordinateX[-1] + 1)
        playerCoordinateY.append(playerCoordinateY[-1])
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])
            
    elif deplacement == "q" and playerCoordinateX[-1] <= 6:
        #player go left
        playerCoordinateX.append(playerCoordinateX[-1] - 1)
        playerCoordinateY.append(playerCoordinateY[-1])
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])  
        
    elif deplacement == "z" and playerCoordinateY[-1] <= 6:
        #player_x go up
        playerCoordinateX.append(playerCoordinateX[-1])
        playerCoordinateY.append(playerCoordinateY[-1] - 1)
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])
        
    elif deplacement == "s" and playerCoordinateY[-1] <= 6:
        #player_x go down
        playerCoordinateX.append(playerCoordinateX[-1])
        playerCoordinateY.append(playerCoordinateY[-1] + 1)
        print("player_x =", playerCoordinateX[-1], "player_y =", playerCoordinateY[-1])
        
    elif playerCoordinateX[-1] == 7 or playerCoordinateY[-1] == 7 or playerCoordinateX[-1] == 0 or playerCoordinateY[-1] == 0:
        print("The snake is not thin enough !")

def generateApple():
    global xApple
    global yApple
    xApple = random.randrange(8)
    yApple = random.randrange(8)
     
generateApple()
while True:
    deplacement()
    print(" ........")
    for y in range(8):
        line = "|"
        for x in range(8):
            if x == playerCoordinateX[-1] and y == playerCoordinateY[-1]:
                line += snakeHead
            elif x == xApple and y == yApple:
                line += apple 
            else:
                line += " "
            '''
            if eatenApple >= 1:
                x = playerCoordinateX[-1]
                y = playerCoordinateY[-1]
                for y in range(playerCoordinateY):
                    for x in range(playerCoordinateX):
                        line += snakeHead
            '''
        line += "|"
        print(line)
    print(" °°°°°°°°")

    print(playerCoordinateX)
    print(playerCoordinateY)
    print(playerCoordinateX[-1], playerCoordinateY[-1])