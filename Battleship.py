from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectFrame import DirectFrame
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import *
import keyboard
import random

loadPrcFile("config/conf.prc")

from direct.showbase.ShowBase import ShowBase


class Bship(ShowBase):

    PLpos = []
    AIpos = []
    AImem = []
    c = 0
    s = 0
    b = 0
    p = 0

    def __init__(self):
        super().__init__()

        self.AISettup()
        #camera settup
        self.camera.setHpr(-35, -24, 0)
        self.camera.setPos(-2.5, -4, 7)

        #disable camera
        self.disable_mouse()

        #env settup
        self.setBackgroundColor(0.1, 0.6, 1.0)

        self.myFrame = DirectFrame(frameColor=(0, 0, 0, 0.3),
                              frameSize=(-0.2, 1, -0.2, 0.5),
                              pos=(1, 0, -0.75))

        # add text entry
        self.entry = DirectEntry(text="", scale=.05,  command=self.event, numLines=1, focus=1, focusOutCommand = self.clearText)
        self.entry.reparentTo(self.myFrame)
        print(self.entry.getPos())

        # TaskManager
        taskMgr.add(self.movCameraTask, 'movCameraTask')


    def clearText(self):
        self.entry.enterText('')

    def event(self, bk_text):
        try:
            if bk_text[0] == 's':
                if self.s <= 1:
                    self.s += 1
                    t = bk_text[2:]
                    self.submarineSpawn(t)
                else:
                    print('submarines limit reached 2/2')
            elif bk_text[0] == 'b':
                if self.b <= 1:
                    self.b += 1
                    t = bk_text[2:]
                    self.boatSpawn(t)
                else:
                    print('boats limit reached 2/2')
            elif bk_text[0] == 'c':
                if self.c == 0:
                    self.c += 1
                    t = bk_text[2:]
                    self.cruiserSpawn(t)
                else:
                    print('cruisers limit reached 1/1')
            elif bk_text[0] == 'p':
                if self.p <= 1:
                    self.p += 1
                    t = bk_text[2:]
                    self.planeSpawn(t)
                else:
                    print('planes limit reached 2/2')
            else:
                if self.c != 1 and self.b != 2 and self.s != 2 and self.p != 2:
                    print('Preperation phase still ongoing \nPlease deploy all your units \n')
                else:
                    self.check(bk_text)
        except ValueError:
            print('Incorrect input')


    def movCameraTask(self, task):

        pos = self.camera.getPos()
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('1'):
                pos.z = 7
            if keyboard.is_pressed('2'):
                pos.z = -7
            if keyboard.is_pressed('3'):
                pos.z = 21
        self.camera.setPos(pos)

        return task.cont



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

        if (1 < x < 10 and 4 < y < 11):

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
            print('Object outside Area')

    def boat(self, x, y):
        if (1 < x < 10 and 4 < y < 13):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, 0)
            box.reparentTo(self.render)
        else:
            print('Object outside Area')

    def submarine(self, x, y):
        if(1<x<10 and 4<y<12):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, -14)
            box.reparentTo(self.render)

            box = self.loader.loadModel("models/box")
            box.setPos(x, y+1, -14)
            box.reparentTo(self.render)
        else:
            print('Object outside Area')


    def plane(self, x, y):
        if (1 < x < 10 and 4 < y < 13):

            box = self.loader.loadModel("models/box")
            box.setPos(x, y, 14)
            box.reparentTo(self.render)
        else:
            print('Object outside Area')


    #Model Spawn

    def submarineSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        print('Submarine deployed ' + str(self.s) + '/2')
        self.PLpos.append([x, y])
        self.submarine(x, y)

    def boatSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        print('Boat deployed ' + str(self.b) + '/2')
        self.PLpos.append([x, y])
        self.boat(x, y)

    def cruiserSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        print('Cruiser deployed ' + str(self.c) + '/1')
        self.PLpos.append([x, y])
        self.cruiser(x, y)

    def planeSpawn(self,bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        print('Plane deployed ' + str(self.p) + '/2')
        self.PLpos.append([x, y])
        self.plane(x, y)


    def AISettup(self):
        c = 0
        p = 0
        b = 0
        s = 0
        for i in range(6):
            if s < 2:
                x = random.randint(2, 9)
                y = random.randint(5, 11)
                self.AIpos.append([x, y])
                s += 1

            elif c < 1:
                x = random.randint(2, 9)
                y = random.randint(5, 10)
                self.AIpos.append([x, y])
                c += 1

            elif p < 2:
                x = random.randint(2, 9)
                y = random.randint(5, 12)
                self.AIpos.append([x, y])
                p += 1

            elif b < 2:
                x = random.randint(2, 9)
                y = random.randint(5, 12)
                self.AIpos.append([x, y])
                b += 1


    def check(self, bk_text):
        if self.PLpos == []:
            print('You lost!')
        elif self.AIpos == []:
            print('You won!')
        else:
            l = []
            if bk_text == "":
                pass
            else:
                x, y = bk_text.split(" ")

                l.append(int(x))
                l.append(int(y))
                print(l)
                if (1 < int(x) < 10 and 4 < int(y) < 13):
                    if l in self.AIpos:
                        print("Lovit")
                        self.PLpos -= l
                    else:
                        print("Blyat")
                else:
                    print('Outside Area')



        AIl =[]
        AIx = random.randint(2, 9)
        AIy = random.randint(5, 12)
        AIl.append(AIx)
        AIl.append(AIy)
        if AIl in self.PLpos:
            print('One of our units has been hit!')
        else:
            for i in range(len(self.AImem) + 1):
                if AIl in self.AImem:
                    while AIl in self.AImem:
                        AIl = []
                        AIx = random.randint(2, 9)
                        AIy = random.randint(5, 12)
                        AIl.append(AIx)
                        AIl.append(AIy)
                    self.AImem.append(AIl)
                else:
                    self.AImem.append(AIl)


game = Bship()
game.corners_b()
game.corners_a()
game.corners_s()
game.run()
