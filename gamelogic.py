
#This is going to contain the game logic for monopoly

class Tile:
    def __init__(self,tiletype):
        self.tiletype = tiletype
        self.players = []

    def moveHere(self,player):
        player.attile.players.remove(player)
        player.attile = self
        self.players.append(player)

class Player:
    def __init__(self,name):
        self.name = name
        self.attile = None

class Dummytile:
    def __init__(self):
        return

class Board:
    def __init__(self):
        self.tiles = []
        for i in range(40):
            self.tiles.append(Tile(Dummytile()))