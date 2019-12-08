import pygame
from pygame.locals import *
import constante as const
import Signilisation.signalisation as signal

#feu rouge
GREEN = (0,255,0)
RED = (255,0,0)
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
        self.color = GREEN
        self.group = 0

    def printSignalisation (self,window,color,x,y) :
        pygame.draw.circle(window, self.color, (x + 25, y + 25), 10)
