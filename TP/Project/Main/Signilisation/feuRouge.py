import pygame
from pygame.locals import *
import constante as const
import Signilisation.signalisation as signal



class ListFeuRouge :
    def __init__ (self):
        self.list = []
    def addlist (feurouge):
        list.append(feurouge)

class GroupFeuRouge :
    def __init__ (self,name):
        self.groupeName = name
        self.list = []
    def addGroupRedLight (redLight) :
        self.list.append(redLight)

class FeuRouge(signal.Signalisation):
    def __init__(self,name):
        signal.Signalisation.__init__(self,name, "stop")
        self.couleur = 0
        self.groupe = 0
        self.serie = 0

    def printSignilisation (self,window,color,x,y) :
        pygame.draw.circle(window, (255,0,0), (x + 25, y + 25), 10)



    def __testRedLightLocation (self,window,case, ccase, crow) :
        if self.matrix[crow][ccase].char == "0":
            fr = FR.FeuRouge("RED")
            case.signilisation = fr
            # fr.__drawRedLight(window,"RED", case.x, case.y)

    def checkRedLightLocation(self,window,case,crow, ccase) :
        if case.char == "4" and crow < 30  :
            self.__testRedLightLocation(window ,case, ccase, crow+1)
        if case.char == "6" and crow > 0 :
            self.__testRedLightLocation(window , case, ccase, crow-1)
        if case.char == "8" and ccase > 0 :
            self.__testRedLightLocation(window ,case,ccase-1, crow)
        if case.char == "2" and ccase < 30 :
            self.__testRedLightLocation(window ,case,ccase+1, crow)
