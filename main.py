import sys, pygame
# Imports functions
from game_functions import *

# Add any new functions here

pygame.init()
running = True

# Defines a ship class TODO: Implement this
class Ship:
    def __init__(self, coordinates, direction, length):
        self.coordinates = coordinates
        self.direction = direction
        self.length = length 

# Define a gameboard for the enemy and the player
playerGameBoard = [[0] * 10 for _ in range(10)]
enemyGameBoard = [[0] * 10 for _ in range(10)]
shipList = [5,4,3,3,2]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # New game setup
    if(True):
        print("New game setup...")
        setupGameBoard(playerGameBoard, shipList)
        printGameBoard(playerGameBoard)
        #setupGameBoard(enemyGameBoard, shipList)
        #printGameBoard(enemyGameBoard)


    running = False


pygame.quit()