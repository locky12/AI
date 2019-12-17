import pygame
from pygame.locals import *
import constante as const
import Signilisation.signalisation as signal

#feu rouge
class Stop():
    def __init__(self):
        self.fonction = "arreter"
        #signal.Signalisation.__init__(self, "stop")

    def getFontion(self):
        return self.fonction
