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
tailleStat = 5

decalY = 1
decalX = 1
timeStop = 1

statTab = [0] * (tailleStat +1)
for i in range(len(statTab)):
    ligne = [0] * (tailleStat + 1)
    statTab[i] = ligne[:]

signTab = ["green", "empty", "stop", "red", "pedestrian", "total"]

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
        Car.viewTabStat()

    def randomMove(self, windows, map) :
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        if caseCar == "0" and Car.itIsInMiddleCase(map):
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
        while not Car.itIsInMiddleCase(map) : # float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50
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
        if not Car.itIsInMiddleCase(map) or caseFront.signalisation == 0:
            map.positionY += change
        else:
            pred = events.Events.getEvenement(caseFront.signalisation)
            real = caseFront.signalisation.getFonction()
            if pred == "green" or pred == "empty":
                map.positionY += change
            if pred == "stop":
                time.sleep(timeStop)
                map.positionY += change
            if pred == "red" or pred == "pedestrian":
                i = 0

            if pred != None and real != None:
                statTab[Car.signalisationReturn(pred)][Car.signalisationReturn(real)] += 1
                statTab[Car.signalisationReturn(pred)][tailleStat] += 1
                statTab[tailleStat][Car.signalisationReturn(real)] += 1
                statTab[tailleStat][tailleStat] += 1

    def moveX(self, windows, map, change, caseFront):
        if not Car.itIsInMiddleCase(map) or caseFront.signalisation == 0:
            map.positionX += change
        else:
            pred = events.Events.getEvenement(caseFront.signalisation)
            real = caseFront.signalisation.getFonction()
            if pred == "green" or pred == "empty":
                map.positionX += change
            if pred == "stop":
                time.sleep(timeStop)
                map.positionX += change
            if pred == "red" or pred == "pedestrian":
                i = 0

            if pred != None and real != None:
                statTab[Car.signalisationReturn(pred)][Car.signalisationReturn(real)] += 1
                statTab[Car.signalisationReturn(pred)][tailleStat] += 1
                statTab[tailleStat][Car.signalisationReturn(real)] += 1
                statTab[tailleStat][tailleStat] += 1

    def signalisationReturn(signalisation):
        for i in range(tailleStat):
            if signalisation == signTab[i]:
                return i

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

    def itIsInMiddleCase(map):
        if float(int(map.positionX/50)) == map.positionX/50 and float(int(map.positionY/50)) == map.positionY/50:
            return True
        else:
            return False

    def viewTabStat():
        print()
        print("pred\\real\t", end="")
        for i in range(len(signTab)):
            for j in range(7):
                if j < len(signTab[i]):
                    print(signTab[i][j], end="")
                else:
                    print(" ", end="")
            print("\t", end="")
        print()

        for i in range(len(statTab)):
            for j in range(10):
                if j < len(signTab[i]):
                    print(signTab[i][j], end="")
                else:
                    print(" ", end="")
            print("\t", end="")
            for j in range(len(statTab[i])):
                print(statTab[i][j], "\t", end ="")
            print()
        print()
