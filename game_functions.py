import sys, pygame, random
# Gameboard creation and setup

def setupGameBoard(gameBoard, shipList):
    print("--Gameboard setup--")
    # Loops through the shipList and place the ships on the gameboard
    for ship in shipList:
        AutoPlaceShip(gameBoard, ship)
    
def AutoPlaceShip(gameBoard, ship):
    print("-- Auto choosing ship location--")
    # Gets a random position on the gameboard and check if the ship can be placed there in any direction
    directions = []
    while len(directions) == 0:
        print("-Finding a valid position for ship of length: ", ship, "-")
        x, y = getRandomCords(gameBoard)
        directions = availableDIrections(gameBoard, ship, x, y)
    
    # Once a valid position and direction are found, proceed with placing the ship
    print("-Available directions: ", directions)
    # Pick a random direction from the available directions
    direction = random.choice(directions)
    print("-Attempting to place ship of length: ", ship, " at: ", x, y, "facing: ", direction)
    placeShip(gameBoard, ship, x, y, direction)

def placeShip(gameBoard, ship, x, y, direction):
    print("--Placing Ship on game board--")
    # Places the ship on the gameboard
    if(direction == "up"):
        for i in range(ship):
            gameBoard[x][y - i] = ship
    elif(direction == "down"):
        for i in range(ship):
            gameBoard[x][y + i] = ship
    elif(direction == "left"):
        for i in range(ship):
            gameBoard[x - i][y] = ship
    elif(direction == "right"):
        for i in range(ship):
            gameBoard[x + i][y] = ship
    else:
        print("Invalid direction")
    

def printGameBoard(gameBoard):
    print("---Game board---")
    for row in gameBoard:
        print(row)
    print("---End of game board---")

def availableDIrections(gameBoard, ship, x, y):
    print("--Checking available directions--")
    up = True
    down = True
    left = True
    right = True
    # Checks if the ship can be placed up
    if(y - ship >= 0):
        # Checks the values between the ship position and its end position
        for i in range(ship):
            if(gameBoard[x][y - i] != 0):
                print("-Cannot place ship UP")
                up = False
    else:
        up = False

    # Checks if the ship can be placed down
    if(y + ship <= len(gameBoard) - 1):
        for i in range(ship):
            if(gameBoard[x][y + i] != 0):
                print("-Cannot place ship DOWN")
                down = False
    else:
        down = False

    # Checks if the ship can be placed Right
    if(x - ship >= 0):
        for i in range(ship):
            if(gameBoard[x - i][y] != 0):
                print("-Cannot place ship RIGHT")
                left = False
    else:
        left = False

    # Checks if the ship can be placed Left
    if(x + ship <= len(gameBoard[0]) - 1):
        for i in range(ship):
            if(gameBoard[x + i][y] != 0):
                print("-Cannot place ship LEFT")
                right = False
    else:
        right = False

    # Returns a list of available directions
    # This is accomplished by zipping the list of directions with the list of flags and only returning the directions that have a flag of True
        # Flag is the True/False element of the list
        # Direction is the directions name
    return [direction for direction, flag in zip(["up", "down", "left", "right"], [up, down, left, right]) if flag]

def getRandomCords(gameBoard):
    print("--Getting random cords--")
    x = random.randint(0, len(gameBoard) - 1)
    y = random.randint(0, len(gameBoard[0]) - 1)
    print("Random cords: ", x, y)
    return x, y