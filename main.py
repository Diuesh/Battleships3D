from Battleship import *

game = Bship()
def PlayerArena():
    game.corners_b()
    game.corners_a()
    game.corners_s()
    game.run()


def AIArena():
    # game.enemycruiser(13, 14)
    # game.enemyboat(15, 16)
    # game.enemyboat(11, 15)
    # game.enemysubmarine(12, 14, -14)
    # game.enemyplane(13, 14, 14)
    # game.enemycorners_b(11, 14)
    # game.enemycorners_a(11, 14, 14)
    # game.enemycorners_s(11, 14, -14)
    pass
PlayerArena()
AIArena()







