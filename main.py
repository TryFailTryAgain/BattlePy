import sys, pygame
from Classes.gameComponents import GameBoard, Ship
# Imports functions
from game_functions import *

# Add any new functions here

pygame.init()
running = True

# Define a gameboard for the enemy and the player
# Allows for changing the size of the gameboard
boardSize = 10
# Allows for changing the size and quantity of the ships to be placed
shipSizeList = [5,4,3,3,2]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # New game setup
    if(True):
        print("New game setup...")
        player1GameBoard = setupGameBoard(boardSize, shipSizeList)
        placeAllShips(player1GameBoard)
        printGameBoard(player1GameBoard)
        print(player1GameBoard.ships[0].cordList)
        while(attack(player1GameBoard, player1GameBoard.ships[0].cordList[0]) == -1):
            print("Target already hit, try again...")
        printGameBoard(player1GameBoard)
               
        #setupGameBoard(enemyGameBoard, shipList)
        #printGameBoard(enemyGameBoard)


    running = False


pygame.quit()