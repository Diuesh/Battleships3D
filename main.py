from panda3d.core import loadPrcFile
loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase

class Bship(ShowBase):
    def __init__(self):
        super().__init__()

        #disable camera
        #self.disable_mouse()

        box = self.loader.loadModel("models/box")
        box.setPos(0, 10, 0)
        box.reparentTo(self.render)






game = Bship()
game.run()