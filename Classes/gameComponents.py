class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.ships = []

    def addShip(self, ship):
        self.ships.append(ship)

# Defines a ship class
class Ship:
    def __init__(self, length, coordinates=None, direction=None):
        self.length = length
        self.headCord = coordinates if coordinates is not None else (0, 0)
        self.direction = direction if direction is not None else ''
        self.cordList = []
    # Getters to get the x and y coordinates individually
    @property
    def xcoord(self):
        return self.coordinates[0]

    @property
    def ycoord(self):
        return self.coordinates[1]
