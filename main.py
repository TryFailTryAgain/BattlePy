import sys, pygame
#pygame.init()
#define a gameboard for the enemy and the player
playerGameBoard = [[0,0,0]]
enemyGameBoard = [[0,0,0]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #New game setup
    if():
        print("New game setup...")
        setupGameBoard(playerGameBoard)
        setupGameBoard(enemyGameBoard)


