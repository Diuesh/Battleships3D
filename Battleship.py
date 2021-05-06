from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *
loadPrcFile("config/conf.prc")


def settext():
    bk_text = ""


class Bship(ShowBase):
    def __init__(self):
        super().__init__()

        #disable camera
        self.disable_mouse()

        #camera settup
        self.camera.setHpr(-35, -24, 0)
        self.camera.setPos(-2.5, -4, 7)

    def planecamera(self, val):
        if val == 1:
            self.camera.setPos(-2.5, -4, 7)
        elif val == 2:
            self.camera.setPos(-2.5, -4, 21)
        elif val == 0:
            self.camera.setPos(-2.5, -4, -7)
        else:
            return 0


        #env settup
        self.setBackgroundColor(0.1, 0.6, 1.0)
# presupunem ca matricea e de 10x10
    v = [1]

    buttons = [DirectRadioButton(text='Submarine', variable=v, value=[0], scale=0.05, pos=(1.4, 0, -0.7), command=settext()),
               DirectRadioButton(text='Barci', variable=v, value=[1], scale=0.05, pos=(1.335, 0, -0.55), command=settext()),
               DirectRadioButton(text='Avioane', variable=v, value=[2], scale=0.05, pos=(1.37, 0, -0.4), command=settext())]
    for button in buttons:
        button.setOthers(buttons)
        planecamera()


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

    def corners_b(self, x, y):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x+9, y, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y+9, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x+9, y+9, 0)
        box.reparentTo(self.render)

    def corners_a(self, x, y, z):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x+9, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y+9, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x+9, y+9, z)
        box.reparentTo(self.render)

    def corners_s(self, x, y, z):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x+9, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y+9, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x+9, y+9, z)
        box.reparentTo(self.render)

    def boat(self, x, y):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, 0)
        box.reparentTo(self.render)

    def submarine(self, x, y, z):
        if(z < 0):
            box = self.loader.loadModel("models/box")
            box.setPos(x, y, z)
            box.reparentTo(self.render)

            box = self.loader.loadModel("models/box")
            box.setPos(x, y+1, z)
            box.reparentTo(self.render)
        else:
            print("Submarines don't float in the air")

    def plane(self, x, y, z):
        if (z >= 0):
            box = self.loader.loadModel("models/box")
            box.setPos(x, y, z)
            box.reparentTo(self.render)

        else:
            print("Planes don't swim... unless they do")
