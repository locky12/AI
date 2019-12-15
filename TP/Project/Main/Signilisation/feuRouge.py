import pygame
from pygame.locals import *
import constante as const
import Signilisation.signalisation as signal

#feu rouge

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
    def __init__(self, name):
        signal.Signalisation.__init__(self, name, "feu rouge")
        self.color = 0
        self.group = 0

    def printFeuRouge(self, window, x, y):
        pygame.draw.circle(window, self.color, (x + 25, y + 25), 10)
