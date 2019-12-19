import pygame
from pygame.locals import *
import random
import time
from math import *
from constante import *
import sys
sys.path.append("..")
from Events import events
tailleCase = 50
tailleAvance = 50
decalY = 1
decalX = 1
timeStop = 1

stopTab = [0, 0]
waitTab = [0, 0]
continueTab = [0, 0]

class Car():

    def __init__(self, map, depart_x, depart_y):
        self.car = pygame.image.load("./Data/Images/carDown.png").convert_alpha()
        self.car = pygame.transform.scale(self.car, (50, 50))
        self.direction = 1
        self.time = 0
        self.distance = 50
        self.case_x = 100
        self.case_y = 100
        self.x = depart_x
        self.y = depart_y
        self.map = map

    def printCar (self, window) :
        # self.map.loadImages (window,self)
        self.map.viewMap(window)
        window.blit(self.car,(self.y,self.x))
        pygame.display.flip()

    def carMove(self, number, windows, map):
        for i in range(number):
            self.randomMove(windows, map)
        Car.afficheStat()

    def randomMove(self, windows, map) :
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        if caseCar == "0" and float(int(map.positionX/50)) == map.positionX/50 and float(int(map.positionY/50)) == map.positionY/50:
            if self.direction == 0:
                self.caseFromTopDirection(windows, map)
            if self.direction == 1:
                self.caseFromRightDirection(windows, map)
            if self.direction == 2:
                self.caseFromBotDirection(windows, map)
            if self.direction == 3:
                self.caseFromLeftDirection(windows, map)
        else:
            self.move(windows, map)

        self.printCar(windows)

    def moveRight(self, windows, map):
        self.direction = (self.direction+1)%4
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        while caseCar == "0":
            self.move(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char

    def moveFront(self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        while caseCar == "0":
            self.move(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char

    def moveLeft(self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        self.move(windows, map)
        self.printCar(windows)
        while float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50:
            self.move(windows, map)
            self.printCar(windows)
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        self.direction = (self.direction+3)%4
        while caseCar == "0":
            self.move(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char

    def move (self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        # print(caseCar)
        time.sleep(self.time)
        if (self.direction == 0):
            caseFront = map.matrix[int(abs(map.positionX/50))-1 + decalX][int(abs(map.positionY/50))+decalY]
            self.moveStep(windows, map, "positionX", tailleAvance, caseFront)
        if (self.direction == 1):
            caseFront = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+1 + decalY]
            self.moveStep(windows, map, "positionY", -tailleAvance, caseFront)
        if (self.direction == 2):
            caseFront = map.matrix[int(abs(map.positionX/50))+1 + decalX][int(abs(map.positionY/50))+ decalY]
            self.moveStep(windows, map, "positionX", -tailleAvance, caseFront)
        if (self.direction == 3):
            caseFront = map.matrix[int(abs(map.positionX/50))+ decalX][int(abs(map.positionY/50))-1 + decalY]
            self.moveStep(windows, map, "positionY", tailleAvance, caseFront)

    def moveStep(self, windows, map, axe, change, caseFront):
        if axe == "positionY":
            self.moveY(windows, map, change, caseFront)
        elif axe == "positionX":
            self.moveX(windows, map, change, caseFront)

    def moveY(self, windows, map, change, caseFront):
        if float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50 or caseFront.signalisation == 0 or events.Events.getEvenement(caseFront.signalisation) == "continue":
            if caseFront.char == "6": # TODO if sur signalisation feu vert et passage pieton vide
                continueTab[1] += 1
            elif caseFront.char == "6": # TODO if signalisation feu rouge passage pieton occupé ou panneau stop
                continueTab[0] += 1
            map.positionY += change
        elif events.Events.getEvenement(caseFront.signalisation) == "wait":
            if caseFront.char == "6": # TODO if sur panneau stop
                waitTab[1] += 1
            else:
                waitTab[0] += 1
            time.sleep(timeStop)
            map.positionY += change
        elif events.Events.getEvenement(caseFront.signalisation) == "stop":
            if caseFront.char == "6": # TODO if signalisation feu rouge passage pieton occupé
                stopTab[1] += 1
            else:
                stopTab[0] += 1

    def moveX(self, windows, map, change, caseFront):
        if float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50 or caseFront.signalisation == 0 or events.Events.getEvenement(caseFront.signalisation) == "continue":
            if caseFront.char == "2": # TODO if sur signalisation feu vert et passage pieton vide
                continueTab[1] += 1
            elif caseFront.char == "2": # TODO if signalisation feu rouge passage pieton occupé ou panneau stop
                continueTab[0] += 1

            map.positionX += change
        elif events.Events.getEvenement(caseFront.signalisation) == "wait":
            if caseFront.char == "2": # TODO if sur panneau stop
                waitTab[1] += 1
            else:
                waitTab[0] += 1

            time.sleep(timeStop)
            map.positionX += change
        elif events.Events.getEvenement(caseFront.signalisation) == "stop":
            if caseFront.char == "2": # TODO if signalisation feu rouge passage pieton occupé
                stopTab[1] += 1
            else:
                stopTab[0] += 1


    def caseFromTopDirection(self, windows, map):
        caseFront = map.matrix[int(abs(map.positionX/tailleCase))-2 + decalX][int(abs(map.positionY/tailleCase)) + decalY].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase)) + decalX][int(abs(map.positionY/tailleCase))+1 + decalY].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))-1 + decalX][int(abs(map.positionY/tailleCase))-2 + decalY].char
        sum = 0
        res = []
        if caseFront == "6":
            sum += 1
            res.append(self.moveFront)
        if caseRight == "2":
            sum += 1
            res.append(self.moveRight)
        if caseLeft == "8":
            sum += 1
            res.append(self.moveLeft)
        rand = random.uniform(0,1)
        for case in range(len(res)):
            if rand < (case+1)/sum and rand > case/sum:
                res[case](windows, map)

    def caseFromRightDirection(self, windows, map):
        caseFront = map.matrix[int(abs(map.positionX/tailleCase)) + decalX][int(abs(map.positionY/tailleCase))+ 2 + decalY].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase))+ 1 + decalX][int(abs(map.positionY/tailleCase)) + decalY].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))- 2 + decalX][int(abs(map.positionY/tailleCase))+ 1 + decalY].char
        sum = 0
        res = []
        if caseFront == "2":
            sum += 1
            res.append(self.moveFront)
        if caseRight == "4":
            sum += 1
            res.append(self.moveRight)
        if caseLeft == "6":
            sum += 1
            res.append(self.moveLeft)
        rand = random.uniform(0,1)
        for case in range(len(res)):
            if rand < (case+1)/sum and rand > case/sum:
                res[case](windows, map)

    def caseFromBotDirection(self, windows, map):
        caseFront = map.matrix[int(abs(map.positionX/tailleCase))+2 + decalX][int(abs(map.positionY/tailleCase)) + decalY].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase)) + decalX][int(abs(map.positionY/tailleCase))-1 + decalY].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))+1 + decalX][int(abs(map.positionY/tailleCase))+2 + decalY].char
        sum = 0
        res = []
        if caseFront == "4":
            sum += 1
            res.append(self.moveFront)
        if caseRight == "8":
            sum += 1
            res.append(self.moveRight)
        if caseLeft == "2":
            sum += 1
            res.append(self.moveLeft)
        rand = random.uniform(0,1)
        for case in range(len(res)):
            if rand < (case+1)/sum and rand > case/sum:
                res[case](windows, map)

    def caseFromLeftDirection(self, windows, map):
        caseFront = map.matrix[int(abs(map.positionX/tailleCase)) + decalX][int(abs(map.positionY/tailleCase))-2 + decalY].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase))-1 + decalX][int(abs(map.positionY/tailleCase)) + decalY].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))+2 + decalX][int(abs(map.positionY/tailleCase))-1 + decalY].char
        sum = 0
        res = []
        if caseFront == "8":
            sum += 1
            res.append(self.moveFront)
        if caseRight == "6":
            sum += 1
            res.append(self.moveRight)
        if caseLeft == "4":
            sum += 1
            res.append(self.moveLeft)
        rand = random.uniform(0,1)
        for case in range(len(res)):
            if rand < (case+1)/sum and rand > case/sum:
                res[case](windows, map)

    def afficheStat():
        print("\n\tfaux", "\tjuste")
        print("continue", continueTab[0], "\t", continueTab[1])
        print("stop\t", stopTab[0], "\t", stopTab[1])
        print("wait\t", waitTab[0], "\t", waitTab[1], "\n")
