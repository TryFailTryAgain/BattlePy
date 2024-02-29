import sys, pygame, random
from Classes.gameComponents import GameBoard, Ship
# Gameboard creation and setup

def setupGameBoard(boardSize, shipSizeList):
    print("--Gameboard setup--")
    gameBoard = GameBoard(boardSize)

    # Loops through the shipList and place the ships on the gameboard
    for size in shipSizeList:
        gameBoard.addShip(Ship(size))
    return gameBoard

def placeAllShips(gameBoard):
    print("--Placing all ships--")
    for ship in gameBoard.ships:
        autoPlaceShip(gameBoard, ship)

def autoPlaceShip(gameBoard, ship):
    print("---Auto choosing ship location---")
    # Gets a random position on the gameboard and check if the ship can be placed there in any direction
    directions = []
    while len(directions) == 0:
        print("--Finding a valid position for ship of length: ", ship.length, "--")
        x, y = getRandomCords(gameBoard.board)
        directions = availableDirections(gameBoard.board, ship.length, x, y)
    
    # Once a valid position and direction are found, proceed with placing the ship
    print("-Available directions: ", directions)
    # Pick a random direction from the available directions
    direction = random.choice(directions)
    print("--Attempting to place ship: ")
    print("-Length:", ship.length)
    print("-At:", x, y)
    print("-Facing:", direction)
    # Modify the existing Ship object with the chosen coordinates and direction
    ship.headCord = (x, y)
    ship.direction = direction

    # Place the ship on the gameboard
    placeShip(gameBoard.board, ship)

def placeShip(board, ship):
    x,y = ship.headCord
    direction = ship.direction
    print("--Placing Ship on game board--")
    # Places the ship on the gameboard
    # Also place the x,y coordinates of the ship in the ship object
    if(direction == "up"):
        for i in range(ship.length):
            board[y - i][x] = ship.length
            ship.cordList.append((x, y - i))
    elif(direction == "down"):
        for i in range(ship.length):
            board[y + i][x] = ship.length
            ship.cordList.append((x, y + i))
    elif(direction == "left"):
        for i in range(ship.length):
            board[y][x - i] = ship.length
            ship.cordList.append((x - i, y))
    elif(direction == "right"):
        for i in range(ship.length):
            board[y][x + i] = ship.length
            ship.cordList.append((x + i, y))
    else:
        print("Invalid direction")

def printGameBoard(gameBoard):
    print("---Game board---")
    for x in range(len(gameBoard.board)):
        print(gameBoard.board[x])
    print("---End of game board---")

# Returns a list of available directions for the ship to be placed
def availableDirections(board, shipLength, x, y):
    print("--Checking available directions--")
    up = True
    down = True
    left = True
    right = True
    # Cycles through each direction and check if the ship can be placed there by
        # iterating through the length of the ship and checking if the positions on the gameBoard are empty
    # Checks if the ship can be placed up
    if(y - shipLength >= 0):
        # Checks the values between the ship position and its end position
        for i in range(shipLength):
            if(board[y - i][x] != 0):
                print("-Cannot place ship UP")
                up = False
                break
    else:
        up = False

    # Checks if the ship can be placed down
    if(y + shipLength <= len(board) - 1):
        for i in range(shipLength):
            if(board[y + i][x] != 0):
                print("-Cannot place ship DOWN")
                down = False
                break
    else:
        down = False

    # Checks if the ship can be placed Right
    if(x + shipLength <= len(board[y]) - 1):
        for i in range(shipLength):
            if(board[y][x + i] != 0):
                print("-Cannot place ship RIGHT")
                right = False
                break
    else:
        right = False

    # Checks if the ship can be placed Left
    if(x - shipLength >= 0):
        for i in range(shipLength):
            if(board[y][x - i] != 0):
                print("-Cannot place ship LEFT")
                left = False
                break
    else:
        left = False

    # Returns a list of available directions
    # This is accomplished by zipping the list of directions with the list of flags and only returning the directions that have a flag of True
        # Flag is the True/False element of the list
        # Direction is the directions name
    return [direction for direction, flag in zip(["up", "down", "left", "right"], [up, down, left, right]) if flag]

def getRandomCords(board):
    print("--Getting random cords--")
    x = random.randint(0, len(board[0]) - 1) # Column
    y = random.randint(0, len(board) - 1) # Row
    print("Random cords: (", x, ",", y, ")")
    return x, y

def attack(gameBoard, cords):
    print("--Attacking--")
    x, y = cords
    print("Attacking cords: (", x, ",", y, ")")
    if(gameBoard.board[y][x] == 0):
        print("Miss")
        # Marks the coordinate as missed so it is not attacked again
        gameBoard.board[y][x] = -1
        return 0
    elif(gameBoard.board[y][x] == -1):
        print("Already attacked")
        return -1

    else:
        print("Hit")
        # Marks the coordinate as hit so it is not attacked again
        gameBoard.board[y][x] = "X"
        # Gets the ship object from the gameBoard that lays on that coordinate
        ship = getShip(gameBoard, cords)
        # Removes the coordinates from the ship object
        ship.cordList.remove(cords)
        # If the ship has no more coordinates, it has been destroyed
        if(len(ship.cordList) == 0):
            print("Ship destroyed")
            gameBoard.ships.remove(ship)
        return 1

def getShip(gameboard, cords):
    print("--Getting ship--")
    for ship in gameboard.ships:
        if cords in ship.cordList:
            print("Ship found")
            return ship