from direct.gui.DirectButton import DirectButton
from direct.task.Task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import loadPrcFile
import keyboard

loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase


class Bship(ShowBase):
    def __init__(self):
        super().__init__()

        #camera settup
        self.camera.setHpr(-35, -24, 0)
        self.camera.setPos(-2.5, -4, 7)

        #disable camera
        self.disable_mouse()

        #env settup
        self.setBackgroundColor(0.1, 0.6, 1.0)



        #TaskManager
        taskMgr.add(self.movCameraTask, 'movCameraTask')

    def movCameraTask(self, task):

        pos = self.camera.getPos()
        if keyboard.is_pressed('1'):
            print("Boat")
            pos.z = 7
        if keyboard.is_pressed('2'):
            print("Submarine")
            pos.z = -7
        if keyboard.is_pressed('3'):
            print("Plane")
            pos.z = 21
        self.camera.setPos(pos)

        return Task.cont


    #Entities

    def corners_b(self, x, y):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x + 9, y, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y + 9, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x + 9, y + 9, 0)
        box.reparentTo(self.render)

    def corners_a(self, x, y, z):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x + 9, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y + 9, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x + 9, y + 9, z)
        box.reparentTo(self.render)

    def corners_s(self, x, y, z):
        box = self.loader.loadModel("models/box")
        box.setPos(x, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x + 9, y, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x, y + 9, z)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(x + 9, y + 9, z)
        box.reparentTo(self.render)

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
