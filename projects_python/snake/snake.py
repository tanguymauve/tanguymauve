
#Modules
from os import remove
import random

#Variables
snake = "x" #Head of the snake
apple = "o" #Apple
player_x = 0 #Coordinate x of the snake's head
player_y = 0 #Coordinate y of the snake's head
playerCoordinateX = [0] #List to register every snake's x coordinate 
playerCoordinateY = [0] #List to register every snake's y coordinate 
eatenApple = 0

#Intro
print("hello and welcome to snake ! d is for going right, q going left, z going up and s going down !")

#Fonctions 
def deplacement():
    global player_x
    global player_y 
    deplacement = input("direction :")
    if deplacement == "d" and player_x <= 6:
        #player_x go right
        player_x += 1
        print("player_x =", player_x, "player_y =", player_y )
    elif deplacement == "q" and player_x >= 1:
        #player_x go left
        player_x -= 1
        print("player_x =", player_x, "player_y =", player_y )   
    elif deplacement == "z" and player_y >= 1: 
        #player_x go up
        player_y -= 1
        print("player_x =", player_x, "player_y =", player_y )
    elif deplacement == "s" and player_y <= 6:
        #player_x go down
        player_y += 1
        print("player_x =", player_x, "player_y =", player_y )
    elif player_x == 7 or player_y ==7 or player_x == 0 or player_y == 0:
        print("The snake is not thin enough !")
        print("player_x =", player_x, "player_y =", player_y)

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
            if x == player_x and y == player_y:
                line += snake
                playerCoordinateX.append(player_x)
                playerCoordinateY.append(player_y)
                for y in range(8):
                    for i in range(eatenApple):
                        if eatenApple >= 1 and x == playerCoordinateX[-1] and y == playerCoordinateY[-1]:
                            line += snake
            elif x == xApple and y == yApple:
                line += apple 
            else:
                line += " "
            if player_x == xApple and player_y == yApple:
                generateApple()
                eatenApple += 1
        line += "|"
        print(line)
    print(" °°°°°°°°")
    print(playerCoordinateX)
    print(playerCoordinateY)