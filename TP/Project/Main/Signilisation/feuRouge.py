import pygame
from pygame.locals import *
import constante as const
import Signilisation.signalisation as signal

#feu rouge
class FeuRouge():
    def __init__(self, color):
        self.color = color
        #signal.Signalisation.__init__(self, "feu rouge")

    def printFeuRouge(self, window, x, y):
        pygame.draw.circle(window, (0,0,0), (x + 25, y + 25), 12)
        pygame.draw.circle(window, self.color, (x + 25, y + 25), 10)

    def getFontion(self):
        if self.color == (255,0,0):
            return "arreter"
        else :
            return "avancer"
