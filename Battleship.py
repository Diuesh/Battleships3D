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
    #Setat coordonata z pentru  avioane,submarine


    def corners_b(self):
        box = self.loader.loadModel("models/box")
        box.setPos(1, 4, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(10, 4, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(1, 13, 0)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(10, 13, 0)
        box.reparentTo(self.render)

    def corners_a(self):
        box = self.loader.loadModel("models/box")
        box.setPos(1, 4, 14)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(10, 4, 14)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(1, 13, 14)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(10, 13, 14)
        box.reparentTo(self.render)

    def corners_s(self):
        box = self.loader.loadModel("models/box")
        box.setPos(1, 4, -14)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(10, 4, -14)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(1, 13, -14)
        box.reparentTo(self.render)

        box = self.loader.loadModel("models/box")
        box.setPos(10, 13, -14)
        box.reparentTo(self.render)

    def cruiser(self, x, y):

        if (1 < x < 10 and 4 < y < 13):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, 0)
            box.reparentTo(self.render)

            box = self.loader.loadModel("models/box")
            box.setPos(x, y+1, 0)
            box.reparentTo(self.render)

            box = self.loader.loadModel("models/box")
            box.setPos(x, y+2, 0)
            box.reparentTo(self.render)
        else:
            raise Exception('Object outside Arena')

    def boat(self, x, y):
        if (1 < x < 10 and 4 < y < 13):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, 0)
            box.reparentTo(self.render)
        else:
            raise Exception('Object outside Arena')

    def submarine(self, x, y):
        if(1<x<10 and 4<y<13):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, -14)
            box.reparentTo(self.render)

            box = self.loader.loadModel("models/box")
            box.setPos(x, y+1, -14)
            box.reparentTo(self.render)
        else:
            raise Exception('Object outside Arena')


    def plane(self, x, y):
        if (1 < x < 10 and 4 < y < 13):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, 14)
            box.reparentTo(self.render)
        else:
            raise Exception('Object outside Arena')


    #alegerea pozitiilor

    def pieces_settup(self):
        sx1 = int(input("X submarin 1:"))
        sy1 = int(input("Y submarin 1:"))
        sx2 = int(input("X submarin 2:"))
        sy2 = int(input("Y submarin 2:"))

        ax1 = int(input("X avion 1:"))
        ay1 = int(input("Y avion 1:"))
        ax2 = int(input("X avion 2:"))
        ay2 = int(input("Y avion 2:"))

        cx = int(input("X nava mare 1:"))
        cy = int(input("Y nava mare 1:"))
        bx1 = int(input("X barca 1:"))
        by1 = int(input("Y barca 1:"))
        bx2 = int(input("X barca 2:"))
        by2 = int(input("Y barca 2:"))

        self.submarine(sx1, sy1)
        self.submarine(sx2, sy2)

        self.plane(ax1, ay1)
        self.plane(ax2, ay2)

        self.cruiser(cx, cy)
        self.boat(bx1, by1)
        self.boat(bx2, by2)


