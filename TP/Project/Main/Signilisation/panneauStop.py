import pygame
from pygame.locals import *
import constante as const

#feu rouge
class Stop():
    def __init__(self):
        self.name = "stop"
        self.fonction = "continue"
        #signal.Signalisation.__init__(self, "stop")

    def getFonction(self):
        return self.fonction
