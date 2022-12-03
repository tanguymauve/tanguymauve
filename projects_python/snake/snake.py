
#Modules
import random

#Variables
snake = "x" #Head of the snake
apple = "o" #Apple
playerCoordinateX = [0] #List to register every snake's x coordinate 
playerCoordinateY = [0] #List to register every snake's y coordinate 
eatenApple = 0
#Intro
print("Hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")
print(playerCoordinateX)
print(playerCoordinateY)

#Fonctions 
def deplacement(): #Based on the player direction, we add a +1 in the corresponding list
    deplacement = input("direction :")
    if deplacement == "d" and playerCoordinateX[0] < 7:
        playerCoordinateX.append(playerCoordinateX[-1] + 1)
        playerCoordinateY.append(playerCoordinateY[0])
            
    elif deplacement == "q" and playerCoordinateX[0] > 0:
        #player go left
        playerCoordinateX.append(playerCoordinateX[-1] - 1)
        playerCoordinateY.append(playerCoordinateY[0])
        
    elif deplacement == "z" and playerCoordinateY[0] > 0:
        #player_x go up
        playerCoordinateX.append(playerCoordinateX[0])
        playerCoordinateY.append(playerCoordinateY[-1] - 1)
        
    elif deplacement == "s" and playerCoordinateY[0] < 7:
        #player_x go down
        playerCoordinateX.append(playerCoordinateX[0])
        playerCoordinateY.append(playerCoordinateY[-1] + 1)
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
    if xApple == playerCoordinateX[-1] and yApple == playerCoordinateY[-1]:
        eatenApple += 1
        generateApple()
    else:
        playerCoordinateX.pop(0)
        playerCoordinateY.pop(0) 
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
        line += "|" 
        print(line) 
    print(" °°°°°°°°")
    
    print(playerCoordinateX)
    print(playerCoordinateY)
    