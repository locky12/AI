import pygame
from random import *
from pygame.locals import *
import constante as const

#feu rouge
class PassagePieton():
    def __init__(self):
        self.passants = 0
        #signal.Signalisation.__init__(self, "stop")

    def getFonction(self):
        if self.passants > 0:
            return "arreter"
        else :
            return "avancer"

    def generePieton(self):
        if self.passants == 0:
            if random() > 0.7:
                self.passants = 1
        else :
            if random() > 0.2:
                self.passants = 0
