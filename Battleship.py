from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectEntry import DirectEntry
from direct.gui.DirectFrame import DirectFrame
from direct.task.TaskManagerGlobal import taskMgr
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import keyboard
import random

loadPrcFile("config/conf.prc")


class Bship(ShowBase):

    PLposb = []
    PLposs = []
    PLposp = []
    AIposp = []
    AIposs = []
    AIposb = []
    AImemb = []
    AImems = []
    AImemp = []
    logText = ''
    c = 0
    s = 0
    b = 0
    p = 0
    helptext = ""

    def __init__(self):
        super().__init__()

        self.AISettup()
        # camera settup
        self.camera.setHpr(-35, -24, 0)
        self.camera.setPos(-2.5, -4, 7)

        # disable camera
        self.disable_mouse()

        # env settup
        self.setBackgroundColor(0.1, 0.6, 1.0)

        self.myFrame = DirectFrame(frameColor=(0, 0, 0, 0.3), frameSize=(-0.2, 1, -0.3, 0.155), pos=(1, 0, -0.75))

        # add text entry
        self.entry = DirectEntry(text='', scale=.05,  command=self.event, numLines=1, focus=1, focusOutCommand=self.clearText, pos=(-0.195, 0, -0.235))
        self.entry.reparentTo(self.myFrame)
        print(self.entry.getPos())

        self.logTextBox = OnscreenText(text='', pos=(-0.145, 0.11, 0), scale=0.05, align=TextNode.ALeft)
        self.logTextBox.reparentTo(self.myFrame)
        constanttext = OnscreenText(text="write h for help, n to hide help", pos=(0.4, -0.9), scale=0.05, fg=(0, 0, 0, 1), mayChange=0)
        self.htext = OnscreenText(text=self.helptext, pos=(0.325, -0.68), scale=0.055, fg=(0, 0, 0, 1), mayChange=1)
        coordtext = OnscreenText(text="b(1<x<10 si 4<y<13),\ns(1<x<10 si 4<y<12),\np(1<x<10 si 4<y<13),\nc(1<x<10 si 4<y<11)", pos=(1.5, -0.4), scale=0.05, fg=(0, 0, 0, 1), mayChange=0)
        mksgridp = "     Planes\n  2    3    4    5    6    7    8    9\n5 |     |     |     |     |     |     |     |     |\n   --------------------------------\n6 |     |     |     |     |     |     |     |     |\n   --------------------------------\n7 |     |     |     |     |     |     |     |     |\n   --------------------------------\n8 |     |     |     |     |     |     |     |     |\n   --------------------------------\n" \
                   "9 |     |     |     |     |     |     |     |     |\n   --------------------------------\n10|     |     |     |     |     |     |     |     |\n   --------------------------------\n11 |     |     |     |     |     |     |     |     |\n   --------------------------------\n12|     |     |     |     |     |     |     |     |"
        mksgridb = "    Boats\n  2    3    4    5    6    7    8    9\n5 |     |     |     |     |     |     |     |     |\n   --------------------------------\n6 |     |     |     |     |     |     |     |     |\n   --------------------------------\n7 |     |     |     |     |     |     |     |     |\n   --------------------------------\n8 |     |     |     |     |     |     |     |     |\n   --------------------------------\n" \
                   "9 |     |     |     |     |     |     |     |     |\n   --------------------------------\n10|     |     |     |     |     |     |     |     |\n   --------------------------------\n11 |     |     |     |     |     |     |     |     |\n   --------------------------------\n12|     |     |     |     |     |     |     |     |"
        mksgrids = "Submarines\n  2    3    4    5    6    7    8    9\n5 |     |     |     |     |     |     |     |     |\n   --------------------------------\n6 |     |     |     |     |     |     |     |     |\n   --------------------------------\n7 |     |     |     |     |     |     |     |     |\n   --------------------------------\n8 |     |     |     |     |     |     |     |     |\n   --------------------------------\n" \
                   "9 |     |     |     |     |     |     |     |     |\n   --------------------------------\n10|     |     |     |     |     |     |     |     |\n   --------------------------------\n11 |     |     |     |     |     |     |     |     |\n   --------------------------------\n12|     |     |     |     |     |     |     |     |"
        showx = OnscreenText(text="X", pos=(0.56, 0.43), scale=0.065, fg=(0, 0, 0, 1), mayChange=0)
        showy = OnscreenText(text="Y", pos=(0.325, 0.675), scale=0.065, fg=(0, 0, 0, 1), mayChange=0)
        xorient = OnscreenText(text="X", pos=(-0.7, 0.45), scale=0.2, fg=(0, 0, 0, 1), mayChange=0)
        yorient = OnscreenText(text="Y", pos=(-1.25, -0.75), scale=0.2, fg=(0, 0, 0, 1), mayChange=0)
        makeshiftgridplane = OnscreenText(text=mksgridp, pos=(1.55, 0.95), scale=0.03, fg=(0, 0, 0, 1), mayChange=0)
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
                if self.c != 1 or self.b != 2 or self.s != 2 or self.p != 2:
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

    # Entities

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
                box.setColor(0.2, 0.5, 0.8)
                box.setTexture(texsubapa)
                box.reparentTo(self.render)

    def cruiser(self, x, y):

        if 1 < x < 10 and 4 < y < 11:
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
        if 1 < x < 10 and 4 < y < 13:
            boat2 = self.loader.load_model("modeleBS3D/Boat2.obj")
            boat2.setPos(x, y, 0.5)
            boat2.setHpr(-90, 0, 0)
            boat2.setScale(0.0005)
            texboat2 = self.loader.load_texture("modeleBS3D/texboat3.jpg")
            boat2.setTexture(texboat2)
            boat2.reparentTo(self.render)
            self.b += 1
        else:
            self.logTextBox.text = 'Object outside Area'

    def submarine(self, x, y):
        if 1 < x < 10 and 4 < y < 12:
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
        if 1 < x < 10 and 4 < y < 13:
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

    # Model Spawn

    def submarineSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        l = []
        l2 = []
        l.append(x)
        l.append(y)
        l2.append(x)
        l2.append(y + 1)

        if l in self.PLposs or l2 in self.PLposs:
            self.logTextBox.text = 'There already is a unit on that position'
        else:
            self.logTextBox.text = 'Submarine deployed ' + str(self.s + 1) + '/2'
            self.PLposs.append([x, y])
            self.PLposs.append([x, y + 1])
            self.submarine(x, y)

    def boatSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        l = []
        l.append(x)
        l.append(y)

        if l in self.PLposb:
            self.logTextBox.text = 'There already is a unit on that position'
        else:
            self.logTextBox.text = 'Boat deployed ' + str(self.b + 1) + '/2'
            self.PLposb.append([x, y])
            self.boat(x, y)

    def cruiserSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        l = []
        l2 = []
        l3 = []
        l.append(x)
        l.append(y)
        l2.append(x)
        l2.append(y + 1)
        print(l2)
        l3.append(x)
        l3.append(y + 2)
        if l in self.PLposb or l2 in self.PLposb or l3 in self.PLposb:
            self.logTextBox.text = 'There already is a unit on that position'
        else:
            self.logTextBox.text = 'Cruiser deployed ' + str(self.c + 1) + '/1'
            self.PLposb.append([x, y])
            self.PLposb.append([x, y + 1])
            self.PLposb.append([x, y + 2])
            self.cruiser(x, y)

    def planeSpawn(self, bk_text):
        x, y = bk_text.split(" ")
        x = int(x)
        y = int(y)
        l = []
        l.append(x)
        l.append(y)

        if l in self.PLposp:
            self.logTextBox.text = 'There already is a unit on that position'
        else:
            self.logTextBox.text = 'Plane deployed ' + str(self.p + 1) + '/2'
            self.PLposp.append([x, y])
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
                self.AIposs.append([x, y])
                self.AIposs.append([x, y + 1])
                s += 1

            elif c < 1:
                x = random.randint(2, 9)
                y = random.randint(5, 10)
                self.AIposb.append([x, y])
                self.AIposb.append([x, y + 1])
                self.AIposb.append([x, y + 2])
                c += 1

            elif p < 2:
                x = random.randint(2, 9)
                y = random.randint(5, 12)
                self.AIposp.append([x, y])
                p += 1

            elif b < 2:
                x = random.randint(2, 9)
                y = random.randint(5, 12)
                self.AIposb.append([x, y])
                b += 1

    def check(self, bk_text):
        if self.PLposs == [] and self.PLposb == [] and self.PLposp == []:
            self.logTextBox.text = 'You lost!'
        elif self.AIposs == [] and self.AIposb == [] and self.AIposp == []:
            self.logTextBox.text = 'You won!'
        else:
            if bk_text[0] == '1':
                bk_text = bk_text[2:]
                l = []
                if bk_text == "":
                    pass
                else:
                    x, y = bk_text.split(" ")

                    l.append(int(x))
                    l.append(int(y))
                    print(l)
                    if 1 < int(x) < 10 and 4 < int(y) < 13:
                        if l in self.AIposs:
                            self.logTextBox.text = "Hit"
                            self.hit = OnscreenText(text='X', pos=(
                            0.39 + 0.0442857142857143 * (int(x) - 2), 0.88 - 0.0592857142857143 * (int(y) - 5), 0),
                                                    scale=0.05,
                                                    align=TextNode.ALeft)
                        else:
                            self.logTextBox.text = "Miss"
                            self.hit = OnscreenText(text='O', pos=(
                            0.39 + 0.0442857142857143 * (int(x) - 2), 0.88 - 0.0592857142857143 * (int(y) - 5), 0),
                                                    scale=0.05,
                                                    align=TextNode.ALeft)
                    else:
                        self.logTextBox.text = 'Outside Area'
            elif bk_text[0] == '2':
                bk_text = bk_text[2:]
                l = []
                if bk_text == "":
                    pass
                else:
                    x, y = bk_text.split(" ")

                    l.append(int(x))
                    l.append(int(y))
                    print(l)
                    if 1 < int(x) < 10 and 4 < int(y) < 13:
                        if l in self.AIposb:
                            self.logTextBox.text = "Hit"
                            self.hit = OnscreenText(text='X', pos=(
                                0.89 + 0.0442857142857143 * (int(x) - 2), 0.88 - 0.0592857142857143 * (int(y) - 5), 0),
                                                    scale=0.05,
                                                    align=TextNode.ALeft)
                        else:
                            self.logTextBox.text = "Miss"
                            self.hit = OnscreenText(text='O', pos=(
                                    0.89 + 0.0442857142857143 * (int(x) - 2), 0.88 - 0.0592857142857143 * (int(y) - 5), 0),
                                                        scale=0.05,
                                                        align=TextNode.ALeft)
                    else:
                        self.logTextBox.text = 'Outside Area'
            elif bk_text[0] == '3':
                bk_text = bk_text[2:]
                l = []
                if bk_text == "":
                    pass
                else:
                    x, y = bk_text.split(" ")

                    l.append(int(x))
                    l.append(int(y))
                    print(l)
                    if 1 < int(x) < 10 and 4 < int(y) < 13:
                        if l in self.AIposp:
                            self.logTextBox.text = "Hit"
                            self.hit = OnscreenText(text='X', pos=(
                                1.39 + 0.0442857142857143 * (int(x) - 2), 0.88 - 0.0592857142857143 * (int(y) - 5), 0),
                                                        scale=0.05,
                                                        align=TextNode.ALeft)
                        else:
                            self.logTextBox.text = "Miss"
                            self.hit = OnscreenText(text='O', pos=(
                                1.39 + 0.0442857142857143 * (int(x) - 2), 0.88 - 0.0592857142857143 * (int(y) - 5), 0),
                                                        scale=0.05,
                                                        align=TextNode.ALeft)
                    else:
                        self.logTextBox.text = 'Outside Area'

        AIl = []
        AIx = random.randint(2, 9)
        AIy = random.randint(5, 12)
        AIl.append(AIx)
        AIl.append(AIy)
        AIz = random.randint(1, 3)
        print(AIz)
        if AIz == 1:
            if AIl in self.PLposs:
                self.logTextBox.text = 'One of our units has been hit!'
                box = self.loader.loadModel("modeleBS3D/cube.obj")
                box.setPos(AIx, AIy, -13)
                box.setScale(0.48)
                texfoc = self.loader.load_texture("modeleBS3D/flama.jpg")
                box.setTexture(texfoc)
                box.reparentTo(self.render)
                self.PLposs.remove(AIl)
            else:

                if AIl in self.AImems:
                    while AIl in self.AImems:
                        AIl = []
                        AIx = random.randint(2, 9)
                        AIy = random.randint(5, 12)
                        AIl.append(AIx)
                        AIl.append(AIy)
                    self.AImems.append(AIl)
                    box = self.loader.loadModel("modeleBS3D/cube.obj")
                    box.setPos(AIx, AIy, -13.75)
                    box.setScale(0.3)
                    box.setColor(1, 0.1, 0.1, 0.3)
                    box.reparentTo(self.render)
                else:
                    box = self.loader.loadModel("modeleBS3D/cube.obj")
                    box.setPos(AIx, AIy, -13.75)
                    box.setScale(0.3)
                    box.setColor(1, 0.1, 0.1, 0.3)
                    box.reparentTo(self.render)
                    self.AImems.append(AIl)
        if AIz == 2:
            if AIl in self.PLposb:
                self.logTextBox.text = 'One of our units has been hit!'
                box = self.loader.loadModel("modeleBS3D/cube.obj")
                box.setPos(AIx, AIy, 0.5)
                box.setScale(0.48)
                texfoc = self.loader.load_texture("modeleBS3D/flama.jpg")
                box.setTexture(texfoc)
                box.reparentTo(self.render)
                self.PLposb.remove(AIl)
            else:

                if AIl in self.AImemb:
                    while AIl in self.AImemb:
                        AIl = []
                        AIx = random.randint(2, 9)
                        AIy = random.randint(5, 12)
                        AIl.append(AIx)
                        AIl.append(AIy)
                    self.AImems.append(AIl)
                    box = self.loader.loadModel("modeleBS3D/cube.obj")
                    box.setPos(AIx, AIy, 0.25)
                    box.setScale(0.3)
                    box.setColor(1, 0.1, 0.1, 0.3)
                    box.reparentTo(self.render)
                else:
                    box = self.loader.loadModel("modeleBS3D/cube.obj")
                    box.setPos(AIx, AIy, 0.25)
                    box.setScale(0.3)
                    box.setColor(1, 0.1, 0.1, 0.3)
                    box.reparentTo(self.render)
                    self.AImemb.append(AIl)
        if AIz == 3:
            if AIl in self.PLposp:
                self.logTextBox.text = 'One of our units has been hit!'
                box = self.loader.loadModel("modeleBS3D/cube.obj")
                box.setPos(AIx, AIy, 15)
                box.setScale(0.48)
                texfoc = self.loader.load_texture("modeleBS3D/flama.jpg")
                box.setTexture(texfoc)
                box.reparentTo(self.render)
                self.PLposp.remove(AIl)
            else:

                if AIl in self.AImemp:
                    while AIl in self.AImemp:
                        AIl = []
                        AIx = random.randint(2, 9)
                        AIy = random.randint(5, 12)
                        AIl.append(AIx)
                        AIl.append(AIy)
                    self.AImemp.append(AIl)
                    box = self.loader.loadModel("modeleBS3D/cube.obj")
                    box.setPos(AIx, AIy, 14.25)
                    box.setScale(0.3)
                    box.setColor(1, 0.1, 0.1, 0.3)
                    box.reparentTo(self.render)
                else:
                    box = self.loader.loadModel("modeleBS3D/cube.obj")
                    box.setPos(AIx, AIy, 14.25)
                    box.setScale(0.3)
                    box.setColor(1, 0.1, 0.1, 0.3)
                    box.reparentTo(self.render)
                    self.AImemp.append(AIl)


game = Bship()
game.corners_b()
game.corners_a()
game.corners_s()
game.run()
