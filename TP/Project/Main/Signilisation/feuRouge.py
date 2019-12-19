import pygame
import random
from pygame.locals import *
import constante as const

listeFeuRouges = []
listeFeuRouges.append("./Data/imagesFeuRouge/feurouge1.jpg")
listeFeuRouges.append("./Data/imagesFeuRouge/feurouge2.jpg")
listeFeuRouges.append("./Data/imagesFeuRouge/feurouge3.jpg")
listeFeuRouges.append("./Data/imagesFeuRouge/feurouge4.jpg")
listeFeuRouges.append("./Data/imagesFeuRouge/feurouge5.jpg")

listeFeuVerts = []
listeFeuVerts.append("./Data/imagesFeuVert/feuvert1.jpg")
listeFeuVerts.append("./Data/imagesFeuVert/feuvert2.jpg")
listeFeuVerts.append("./Data/imagesFeuVert/feuvert3.jpg")
listeFeuVerts.append("./Data/imagesFeuVert/feuvert4.jpg")
listeFeuVerts.append("./Data/imagesFeuVert/feuvert5.jpg")

class FeuRouge():
    def __init__(self, color):
        self.name = "feuRouge"
        self.color = color

    def printFeuRouge(self, window, x, y):
        pygame.draw.circle(window, (0,0,0), (x + 25, y + 25), 12)
        pygame.draw.circle(window, self.color, (x + 25, y + 25), 10)

    def getFonction(self):
        if self.color == (255,0,0):
            return "red"
        else :
            return "green"

    def getRandomImage(self):
        rand = random.randint(0,4)
        if self.getFonction() == "red" :
            return listeFeuRouges[rand]
        else :
            return listeFeuVerts[rand]
