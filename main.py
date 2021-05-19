from Battleship import *

game = Bship()
def PlayerArena():
    game.corners_b()
    game.corners_a()
    game.corners_s()
    game.pieces_settup()
    game.run()

def AIArena():
    pass

PlayerArena()






