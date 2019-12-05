import pygame
from pygame.locals import *
from constante import *
# from map import *

class Car():

    def __init__(self, map, depart_x, depart_y):
        self.car = pygame.image.load("./Data/Images/carDown.png").convert_alpha()
        self.car = pygame.transform.scale(self.car, (50, 50))
        self.direction = "droite"
        self.vitesse = 0.1
        self.distance = 50
        self.case_x = 0
        self.case_y = 0
        self.x = depart_x
        self.y = depart_y
        self.map = map




    def printCar (self, window) :
        # self.map.loadImages (window,self)
        self.map.viewMap(window)
        window.blit(self.car,(self.x,self.y))
        pygame.display.flip()

    def move (self , direction, window):
        if direction == "droite" :
            if self.case_x < (100) :
                if self.map.matrix[self.case_y][self.case_x+1] != "a":
                    self.case_x += 1
                    self.x = self.case_x * taille_case

        if direction == "gauche" :
            if self.case_x > -1 :
                if self.map.matrix[self.case_y][self.case_x-1] != "a":
                    self.case_x -=1
                    self.x = self.case_x * taille_case
        if direction == "haut" :
            if self.case_y > -1 :
                if self.map.matrix[self.case_y-1][self.case_x] != "a":
                    self.case_y -=1
                    self.y = self.case_y * taille_case
        if direction == "bas" :
            if self.case_x < (100) :
                if self.map.matrix[self.case_y+1][self.case_x] != "a":
                    self.case_y +=1

                    self.y = self.case_y * taille_case
