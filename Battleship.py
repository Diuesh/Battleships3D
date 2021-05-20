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
    logText = ''
    c = 0
    s = 0
    b = 0
    p = 0
    helptext = ""

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
                              frameSize=(-0.2, 1, -0.3, 0.155),
                              pos=(1, 0, -0.75))

        # add text entry
        self.entry = DirectEntry(text='', scale=.05,  command=self.event, numLines=1, focus=1, focusOutCommand=self.clearText, pos=(-0.195, 0, -0.235))
        self.entry.reparentTo(self.myFrame)
        print(self.entry.getPos())

        self.logTextBox = OnscreenText(text = '', pos = (-0.145, 0.11, 0), scale = 0.05, align=TextNode.ALeft)
        self.logTextBox.reparentTo(self.myFrame)
        constanttext = OnscreenText(text="write h for help, n to hide help", pos=(0.4, -0.9), scale=0.05,fg=(0, 0, 0, 1), mayChange=0)
        self.htext = OnscreenText(text=self.helptext, pos=(0.325, -0.68), scale=0.055, fg=(0, 0, 0, 1),mayChange=1)
        coordtext = OnscreenText(text="b(1<x<10 si 4<y<13),\ns(1<x<10 si 4<y<12),\np(1<x<10 si 4<y<13),\nc(1<x<10 si 4<y<11)", pos=(1.5, -0.4), scale=0.05,fg=(0, 0, 0, 1), mayChange=0)
        mksgridp = "     Planes\n  2    3    4    5    6    7    8    9\n5 |     |     |     |     |     |     |     |     |\n   --------------------------------\n6 |     |     |     |     |     |     |     |     |\n   --------------------------------\n7 |     |     |     |     |     |     |     |     |\n   --------------------------------\n8 |     |     |     |     |     |     |     |     |\n   --------------------------------\n" \
                   "9 |     |     |     |     |     |     |     |     |\n   --------------------------------\n10|     |     |     |     |     |     |     |     |\n   --------------------------------\n11 |     |     |     |     |     |     |     |     |\n   --------------------------------\n12|     |     |     |     |     |     |     |     |"
        mksgridb = "    Boats\n  2    3    4    5    6    7    8    9\n5 |     |     |     |     |     |     |     |     |\n   --------------------------------\n6 |     |     |     |     |     |     |     |     |\n   --------------------------------\n7 |     |     |     |     |     |     |     |     |\n   --------------------------------\n8 |     |     |     |     |     |     |     |     |\n   --------------------------------\n" \
                   "9 |     |     |     |     |     |     |     |     |\n   --------------------------------\n10|     |     |     |     |     |     |     |     |\n   --------------------------------\n11 |     |     |     |     |     |     |     |     |\n   --------------------------------\n12|     |     |     |     |     |     |     |     |"
        mksgrids = "Submarines\n  2    3    4    5    6    7    8    9\n5 |     |     |     |     |     |     |     |     |\n   --------------------------------\n6 |     |     |     |     |     |     |     |     |\n   --------------------------------\n7 |     |     |     |     |     |     |     |     |\n   --------------------------------\n8 |     |     |     |     |     |     |     |     |\n   --------------------------------\n" \
                   "9 |     |     |     |     |     |     |     |     |\n   --------------------------------\n10|     |     |     |     |     |     |     |     |\n   --------------------------------\n11 |     |     |     |     |     |     |     |     |\n   --------------------------------\n12|     |     |     |     |     |     |     |     |"
        showx= OnscreenText(text="X",pos=(0.56, 0.43), scale=0.065, fg=(0, 0, 0, 1), mayChange=0)
        showy = OnscreenText(text="Y", pos=(0.325, 0.675), scale=0.065, fg=(0, 0, 0, 1), mayChange=0)
        xorient = OnscreenText(text="X", pos=(-0.7, 0.45), scale=0.2, fg=(0, 0, 0, 1), mayChange=0)
        yorient = OnscreenText(text="Y", pos=(-1.25, -0.75), scale=0.2, fg=(0, 0, 0, 1), mayChange=0)
        makeshiftgridplane = OnscreenText(text=mksgridp,pos=(1.55, 0.95), scale=0.03, fg=(0, 0, 0, 1), mayChange=0)
        makeshiftgridboat = OnscreenText(text=mksgridb, pos=(1.05, 0.95), scale=0.03, fg=(0, 0, 0, 1), mayChange=0)
        makeshiftgridsubmar = OnscreenText(text=mksgrids, pos=(0.55, 0.95), scale=0.03, fg=(0, 0, 0, 1), mayChange=0)

        # TaskManager
        taskMgr.add(self.movCameraTask, 'movCameraTask')


    def clearText(self):
        self.entry.enterText('')

    def event(self, bk_text):
        try:
            if bk_text[0] == 's':
                if self.s <= 1:

                    t = bk_text[2:]
                    self.submarineSpawn(t)
                else:
                    self.logTextBox.text = 'Submarines limit reached 2/2'
            elif bk_text[0] == 'b':
                if self.b <= 1:

                    t = bk_text[2:]
                    self.boatSpawn(t)
                else:
                    self.logTextBox.text = 'Boats limit reached 2/2'
            elif bk_text[0] == 'c':
                if self.c == 0:
                    t = bk_text[2:]
                    self.cruiserSpawn(t)
                else:
                    self.logTextBox.text = 'Cruisers limit reached 1/1'
            elif bk_text[0] == 'h':
                self.htext.text = "Ctrl + 1/2/3 schimba planul\nplasarea se face in felul urmator:\ns/p/b/c coord x apoi coord y Ex: b 5 8\nalt+F4 pentru inchidere"
            elif bk_text[0] == 'n':
                self.htext.text = ""
            elif bk_text[0] == 'p':
                if self.p <= 1:
                    t = bk_text[2:]
                    self.planeSpawn(t)
                else:
                    self.logTextBox.text = 'Planes limit reached 2/2'
            else:
                if self.c != 1 and self.b != 2 and self.s != 2 and self.p != 2:
                    self.logTextBox.text = 'Preparation phase still ongoing\nPlease deploy all your units\n'
                else:
                    self.check(bk_text)
        except ValueError:
            self.logTextBox.text = 'Incorrect input!Try again'


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
        for i in range(2, 10):
            for j in range(5, 13):
                box = self.loader.loadModel("modeleBS3D/cube.obj")
                box.setPos(i, j, 0)
                box.setScale(0.5)
                texocean = self.loader.load_texture("modeleBS3D/oceancub.jpg")
                box.setTexture(texocean)
                box.reparentTo(self.render)

    def corners_a(self):
        for i in range(2, 10):
            for j in range(5, 13):
                box = self.loader.loadModel("modeleBS3D/cube.obj")
                box.setPos(i, j, 14)
                box.setScale(0.5)
                texcer = self.loader.load_texture("modeleBS3D/noricub.jpg")
                box.setTexture(texcer)
                box.reparentTo(self.render)

    def corners_s(self):
        for i in range(2, 10):
            for j in range(5, 13):
                box = self.loader.loadModel("modeleBS3D/cube.obj")
                box.setPos(i, j, -14)
                box.setScale(0.5)
                texsubapa = self.loader.load_texture("modeleBS3D/subapanisip.jpg")
                box.setColor(0.2,0.5,0.8)
                box.setTexture(texsubapa)
                box.reparentTo(self.render)

    def cruiser(self, x, y):

        if (1 < x < 10 and 4 < y < 11):
            carrier = self.loader.loadModel("modeleBS3D/Carrier.obj")
            carrier.setPos(x, y + 1, 0.5)
            carrier.setHpr(-180, 90, 0)
            carrier.setScale(0.0125, 0.01, 0.01)
            texcarrier = self.loader.load_texture("modeleBS3D/texboat3.jpg")
            carrier.setTexture(texcarrier)
            carrier.reparentTo(self.render)
            self.c += 1
        else:
            self.logTextBox.text = 'Object outside Area'

    def boat(self, x, y):
        if (1 < x < 10 and 4 < y < 13):
            boat2 = self.loader.load_model("modeleBS3D/Boat2.obj")
            boat2.setPos(x , y , 0.5)
            boat2.setHpr(-90, 0, 0)
            boat2.setScale(0.0005)
            texboat2 = self.loader.load_texture("modeleBS3D/texboat3.jpg")
            boat2.setTexture(texboat2)
            boat2.reparentTo(self.render)
            self.b += 1
        else:
            self.logTextBox.text = 'Object outside Area'

    def submarine(self, x, y):
        if(1<x<10 and 4<y<12):
            sub1 = self.loader.loadModel("modeleBS3D/Submarine1.obj")
            sub1.setPos(x + 0.425, y + 1.5, -13)
            sub1.setHpr(-180, 90, 0)
            sub1.setScale(0.04)
            texsub1 = self.loader.load_texture("modeleBS3D/texplane.jpg")
            sub1.setTexture(texsub1)
            sub1.reparentTo(self.render)
            self.s += 1
        else:
            self.logTextBox.text = 'Object outside Area'


    def plane(self, x, y):
        if (1 < x < 10 and 4 < y < 13):
            plane3 = self.loader.loadModel("modeleBS3D/Plane5.obj")
            plane3.setPos(x, y, 15)
            plane3.setHpr(180, -270, 180)
            plane3.setScale(0.08)
            texplane3 = self.loader.load_texture("modeleBS3D/texplane3.jpg")
            plane3.setTexture(texplane3)
            plane3.reparentTo(self.render)
            self.p += 1
        else:
            self.logTextBox.text = 'Object outside Area'


    #Model Spawn

    def submarineSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        self.logTextBox.text = 'Submarine deployed ' + str(self.s + 1) + '/2'
        self.PLpos.append([x, y])
        self.submarine(x, y)


    def boatSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        self.logTextBox.text = 'Boat deployed ' + str(self.b + 1) + '/2'
        self.PLpos.append([x, y])
        self.boat(x, y)


    def cruiserSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        self.logTextBox.text = 'Cruiser deployed ' + str(self.c + 1) + '/1'
        self.PLpos.append([x, y])
        self.cruiser(x, y)


    def planeSpawn(self,bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        self.logTextBox.text = 'Plane deployed ' + str(self.p + 1) + '/2'
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
            self.logTextBox.text = 'You lost!'
        elif self.AIpos == []:
            self.logTextBox.text = 'You won!'
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
                        self.logTextBox.text = "Hit"
                        self.PLpos -= l
                    else:
                        self.logTextBox.text = "Miss"
                else:
                    self.logTextBox.text = 'Outside Area'



        AIl =[]
        AIx = random.randint(2, 9)
        AIy = random.randint(5, 12)
        AIl.append(AIx)
        AIl.append(AIy)
        if AIl in self.PLpos:
            self.logTextBox.text = 'One of our units has been hit!'
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
