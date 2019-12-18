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
tailleAvance = 10
decalY = 1
decalX = 1
timeStop = 1

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
            self.moveStep(windows, map)

    def moveRight(self, windows, map):
        self.direction = (self.direction+1)%4
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        while caseCar == "0":
            self.moveStep(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char

    def moveFront(self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        while caseCar == "0":
            self.moveStep(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char

    def moveLeft(self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        self.moveStep(windows, map)
        self.printCar(windows)
        while float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50:
            self.moveStep(windows, map)
            self.printCar(windows)
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        self.direction = (self.direction+3)%4
        while caseCar == "0":
            self.moveStep(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char

    def moveStep (self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+decalY].char
        # print(caseCar)
        time.sleep(self.time)
        if (self.direction == 0):
            caseFront = map.matrix[int(abs(map.positionX/50))-1 + decalX][int(abs(map.positionY/50))+decalY]
            if float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50 or caseFront.signalisation == 0 or events.Events.getEvenement(caseFront.signalisation) == "continue":
                map.positionX += tailleAvance
            elif events.Events.getEvenement(caseFront.signalisation) == "wait":
                time.sleep(timeStop)
                map.positionX += tailleAvance
        if (self.direction == 1):
            caseFront = map.matrix[int(abs(map.positionX/50))+decalX][int(abs(map.positionY/50))+1 + decalY]
            if float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50 or caseFront.signalisation == 0 or events.Events.getEvenement(caseFront.signalisation) == "continue":
                map.positionY -= tailleAvance
            elif events.Events.getEvenement(caseFront.signalisation) == "wait":
                time.sleep(timeStop)
                map.positionY -= tailleAvance
        if (self.direction == 2):
            caseFront = map.matrix[int(abs(map.positionX/50))+1 + decalX][int(abs(map.positionY/50))+ decalY]
            if float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50 or caseFront.signalisation == 0 or events.Events.getEvenement(caseFront.signalisation) == "continue":
                map.positionX -= tailleAvance
            elif events.Events.getEvenement(caseFront.signalisation) == "wait":
                time.sleep(timeStop)
                map.positionX -= tailleAvance
        if (self.direction == 3):
            caseFront = map.matrix[int(abs(map.positionX/50))+ decalX][int(abs(map.positionY/50))-1 + decalY]
            if float(int(map.positionX/50)) != map.positionX/50 or float(int(map.positionY/50)) != map.positionY/50 or caseFront.signalisation == 0 or events.Events.getEvenement(caseFront.signalisation) == "continue":
                map.positionY += tailleAvance
            elif events.Events.getEvenement(caseFront.signalisation) == "wait":
                time.sleep(timeStop)
                map.positionY += tailleAvance

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
        print(res)
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
