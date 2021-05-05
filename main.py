from direct.gui.DirectGui import *
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
loadPrcFile("config/conf.prc")

v = [1]  # Valoarea initiala (default)
bk_text = "selector plan"


def settext(status=None):
    bk_text = "Valoarea curenta: %s" % v


buttons = [DirectRadioButton(text='Submarine', variable=v, value=[0], scale=0.05, pos=(1, 0, -0.2), command=settext()),
           DirectRadioButton(text='Barci', variable=v, value=[1], scale=0.05, pos=(1, 0, 0), command=settext()),
           DirectRadioButton(text='Avioane', variable=v, value=[2], scale=0.05, pos=(1, 0, 0.2), command=settext())]
for button in buttons:
    button.setOthers(buttons)


class Bship(ShowBase):
    def __init__(self):
        super().__init__()

        # disable camera
        # self.disable_mouse()

        box = self.loader.loadModel("models/box")
        box.setPos(0, 10, 0)
        box.reparentTo(self.render)


game = Bship()
game.run()
