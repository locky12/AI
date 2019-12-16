import pygame
from pygame.locals import *
import random
import time
from math import *
from constante import *
# from car import *
tailleCase = 50
tailleAvance = 25

class Car():

    def __init__(self, map, depart_x, depart_y):
        self.car = pygame.image.load("./Data/Images/carDown.png").convert_alpha()
        self.car = pygame.transform.scale(self.car, (50, 50))
        self.direction = 1
        self.time = 0.1
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
        caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char
        if(caseCar == "0" and float(int(abs(map.positionX/50)+1)) == abs(map.positionX/50)+1 and float(int(abs(map.positionY/50)+1)) == abs(map.positionY/50)+1):
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
        caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char
        while caseCar == "0":
            self.moveStep(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char

    def moveFront(self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char
        while caseCar == "0":
            self.moveStep(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char

    def moveLeft(self, windows, map):
        caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char
        self.moveStep(windows, map)
        self.printCar(windows)
        while float(int(abs(map.positionX/50)+1)) != abs(map.positionX/50)+1 or float(int(abs(map.positionY/50)+1)) != abs(map.positionY/50)+1:
            self.moveStep(windows, map)
            self.printCar(windows)
        caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char
        self.direction = (self.direction+3)%4
        while caseCar == "0":
            self.moveStep(windows, map)
            self.printCar(windows)
            caseCar = map.matrix[int(abs(map.positionX/50))+1][int(abs(map.positionY/50))+1].char

    def moveStep (self, windows, map):
        time.sleep(self.time)
        if (self.direction == 0):
            map.positionX += tailleAvance
        if (self.direction == 1):
            map.positionY -= tailleAvance
        if (self.direction == 2):
            map.positionX -= tailleAvance
        if (self.direction == 3):
            map.positionY += tailleAvance

    def caseFromTopDirection(self, windows, map):
        caseFront = map.matrix[int(abs(map.positionX/tailleCase))-1][int(abs(map.positionY/tailleCase))+1].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase))+1][int(abs(map.positionY/tailleCase))+2].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))][int(abs(map.positionY/tailleCase))-1].char
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
        caseFront = map.matrix[int(abs(map.positionX/tailleCase))+1][int(abs(map.positionY/tailleCase))+3].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase))+2][int(abs(map.positionY/tailleCase))+1].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))-1][int(abs(map.positionY/tailleCase))+2].char
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
        caseFront = map.matrix[int(abs(map.positionX/tailleCase))+3][int(abs(map.positionY/tailleCase))+1].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase))+1][int(abs(map.positionY/tailleCase))].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))+2][int(abs(map.positionY/tailleCase))+3].char
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
        caseFront = map.matrix[int(abs(map.positionX/tailleCase))+1][int(abs(map.positionY/tailleCase))-1].char
        caseRight = map.matrix[int(abs(map.positionX/tailleCase))][int(abs(map.positionY/tailleCase))+1].char
        caseLeft  = map.matrix[int(abs(map.positionX/tailleCase))+3][int(abs(map.positionY/tailleCase))].char
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
