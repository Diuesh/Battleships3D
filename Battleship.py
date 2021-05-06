from panda3d.core import loadPrcFile


loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase


class Bship(ShowBase):
    def __init__(self):
        super().__init__()

        #disable camera
        #self.disable_mouse()

        #camera settup
        # self.camera.setPos(-10, -10, -10)
        # self.camera.setHpr(0, 0, 0)

        #env settup
        self.setBackgroundColor(0.1, 0.6, 1.0)

    def cruiser(self, x, y):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y+1, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y+2, 0)
        box.reparentTo(self.render)

    def boat(self, x, y):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, 0)
        box.reparentTo(self.render)

    def submarine(self, x, y, z):
        if(z<0):
            box = self.loader.loadModel("models/box")
            box.setPos(x, y, z)
            box.reparentTo(self.render)

            box = self.loader.loadModel("models/box")
            box.setPos(x, y+1, z)
            box.reparentTo(self.render)
        else:
            print("Submarines dont float")

    def plane(self, x, y, z):
        if (z >= 0):
            box = self.loader.loadModel("models/box")
            box.setPos(x, y, z)
            box.reparentTo(self.render)

        else:
            print("Planes dont swim")