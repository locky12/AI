import pygame
from pygame.locals import *
import random

listeStops = []
listeStops.append("./Data/imagesStop/stop1.jpg")
listeStops.append("./Data/imagesStop/stop2.jpg")
listeStops.append("./Data/imagesStop/stop3.jpg")
listeStops.append("./Data/imagesStop/stop4.jpg")
listeStops.append("./Data/imagesStop/stop5.jpg")

class Stop():
    def __init__(self):
        self.name = "stop"
        self.fonction = "stop"

    def getFonction(self):
        return self.fonction

    def getRandomImage(self):
        rand = random.randint(0,4)
        return listeStops[rand]
