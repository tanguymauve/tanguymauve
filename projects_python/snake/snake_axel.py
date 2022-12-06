import random

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

keys = {
    "z": UP,
    "s": DOWN,
    "q": LEFT,
    "d": RIGHT
}

snake = [(0, 0)]
BOARD_SIZE = 8
apple = (0, 0)

def display():
    board = "#" * (BOARD_SIZE + 2) + '\n'
    for y in range(BOARD_SIZE):
        board += "#"
        for x in range(BOARD_SIZE):
            if (x, y) in snake:
                board += "X"
            elif (x, y) == apple:
                board += "O"
            else:
                board += " "
        board += "#\n"
    board += "#" * (BOARD_SIZE + 2)
    print(board)

def generateAppleCoords():
    apple = snake[0]
    while apple in snake:
        apple = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
    return apple

def getInput():
    key = input("Enter key:")
    if key in keys.keys():
        return key
    else:
        print("Wrong key")
        return getInput()


apple = generateAppleCoords()
while snake[0][0] >= 0 and snake[0][0] < BOARD_SIZE and snake[0][1] >= 0 and snake[0][1] < BOARD_SIZE:
    display()
    
    key = getInput()
    delta = keys[key]
    newCoords = (snake[0][0] + delta[0], snake[0][1] + delta[1])
    snake.insert(0, newCoords)
    if newCoords == apple:
        apple = generateAppleCoords()
    else:
        snake.pop()

print("GAME OVER")