from direct.gui.DirectButton import DirectButton
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectFrame import DirectFrame
from direct.gui.OnscreenText import OnscreenText
from direct.task.Task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import *
import keyboard

loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase


class Bship(ShowBase):

    val = dict

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


        self.myFrame = DirectFrame(frameColor=(0, 0, 0, 0.3),
                              frameSize=(-0.2, 1, -0.2, 0.5),
                              pos=(1, 0, -0.75))

        myDR = self.win.makeDisplayRegion(0, 1, 0, 1)
        self.mouseWatcherNode.setDisplayRegion(myDR)

        bk_text = ""
        textObject = OnscreenText(text=bk_text, pos=(2, -2), scale=0.07,
                                  fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                                  mayChange=1)
        textObject.reparentTo(self.aspect2d)

        # callback function to set  text
        def setText(textEntered):
            textObject.setText(textEntered)


        print(self.myFrame.getPos())

        # clear the text
        def clearText():
            self.entry.enterText('')
        print(self.myFrame.getPos())

        # add text entry
        self.entry = DirectEntry(text="", scale=.05,  command=setText, numLines=2, focus=0)
        self.entry.reparentTo(self.myFrame)

        if(self.entry['focus'] == 1):
            taskMgr.remove('movCameraTask')
        elif(self.entry['focus'] == 0):
            taskMgr.add(self.movCameraTask, 'movCameraTask')


    #     self.accept("mouse1", self.mouse_click)
    #     self.accept("mouse1-up", self.mouse_click)
    #
    #
    # def mouse_click(self):
    #     md1 = self.win.getPointer(0)
    #     mx = md1.getX()
    #     my = md1.getY()
    #     if (mx != self.myFrame.getPos()[0] and my != self.myFrame.getPos()[2]):
    #         self.entry['focus'] = 0
    #     else:
    #         self.entry['focus'] = 1



        # entry.focusInCommandFunc()
        # entry.focusOutCommandFunc()



        # TaskManager
        taskMgr.add(self.movCameraTask, 'movCameraTask')

    def movCameraTask(self, task):

        pos = self.camera.getPos()

        if (self.entry['focus'] == 0):
            if keyboard.is_pressed('1'):
                pos.z = 7
            if keyboard.is_pressed('2'):
                pos.z = -7
            if keyboard.is_pressed('3'):
                pos.z = 21
        elif (self.entry['focus'] == 1):
            pass

        self.camera.setPos(pos)

        return Task.cont



    #Entities

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
        # sx1 = int(input("X submarin 1:"))
        # sy1 = int(input("Y submarin 1:"))
        # sx2 = int(input("X submarin 2:"))
        # sy2 = int(input("Y submarin 2:"))
        #
        # ax1 = int(input("X avion 1:"))
        # ay1 = int(input("Y avion 1:"))
        # ax2 = int(input("X avion 2:"))
        # ay2 = int(input("Y avion 2:"))
        #
        # cx = int(input("X nava mare 1:"))
        # cy = int(input("Y nava mare 1:"))
        # bx1 = int(input("X barca 1:"))
        # by1 = int(input("Y barca 1:"))
        # bx2 = int(input("X barca 2:"))
        # by2 = int(input("Y barca 2:"))

        sx1 = 2
        self.val.update({'sx1': sx1})
        sy1 = 7
        self.val.update({'sy1': sy1})
        sx2 = 4
        self.val.update({'sx2': sx2})
        sy2 = 5
        self.val.update({'sy2': sy2})

        ax1 = 4
        self.val.update({'ax1': ax1})
        ay1 = 6
        self.val.update({'ay1': ay1})
        ax2 = 4
        self.val.update({'ax2': ax2})
        ay2 = 8
        self.val.update({'ay2': ay2})

        cx = 4
        self.val.update({'cx': cx})
        cy = 6
        self.val.update({'cy': cy})
        bx1 = 7
        self.val.update({'bx1': bx1})
        by1 = 8
        self.val.update({'by1': by1})
        bx2 = 3
        self.val.update({'bx2': bx2})
        by2 = 9
        self.val.update({'by2':by2})


        self.submarine(sx1, sy1)
        self.submarine(sx2, sy2)

        self.plane(ax1, ay1)
        self.plane(ax2, ay2)

        self.cruiser(cx, cy)
        self.boat(bx1, by1)
        self.boat(bx2, by2)


