from Battleship import *

game = Bship()
game.cruiser(3, 4)
game.boat(5, 6)
game.boat(1, 5)
game.submarine(2, 4, -14)
game.plane(3, 4, 14)
game.corners_b(1, 4)
game.corners_a(1, 4, 14)
game.corners_s(1, 4, -14)
game.run()






