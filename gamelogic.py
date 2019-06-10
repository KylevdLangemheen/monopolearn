
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
        self.tilename = "Dummy"
        return

class Board:
    def __init__(self):
        self.tiles = []
        for i in range(40):
            self.tiles.append(Tile(Dummytile()))

class Players:
    def __init__(self,p1,p2,p3,p4):
        self.players = [p1,p2,p3,p4]

def doAPoly():
    return