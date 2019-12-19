import pygame
import random
from pygame.locals import *
import constante as const

listePPPleins = []
listePPPleins.append("./Data/imagesPPPlein/ppplein1.jpg")
listePPPleins.append("./Data/imagesPPPlein/ppplein2.jpg")
listePPPleins.append("./Data/imagesPPPlein/ppplein3.jpg")
listePPPleins.append("./Data/imagesPPPlein/ppplein4.jpg")
listePPPleins.append("./Data/imagesPPPlein/ppplein5.jpg")

listePPVides = []
listePPVides.append("./Data/imagesPPVide/ppvide1.jpg")
listePPVides.append("./Data/imagesPPVide/ppvide2.jpg")
listePPVides.append("./Data/imagesPPVide/ppvide3.jpg")
listePPVides.append("./Data/imagesPPVide/ppvide4.jpg")
listePPVides.append("./Data/imagesPPVide/ppvide5.jpg")

class PassagePieton():
    def __init__(self):
        self.name = "passagePieton"
        self.passants = 0

    def getFonction(self):
        if self.passants > 0:
            return "pedestrian"
        else :
            return "empty"

    def generePieton(self):
        if self.passants == 0:
            if random.randint(1,10) > 7:
                self.passants = 1
        else :
            if random.randint(1,10) > 2:
                self.passants = 0

    def getRandomImage(self):
        rand = random.randint(0,4)
        if self.getFonction() == "pedestrian" :
            return listePPPleins[rand]
        else :
            return listePPVides[rand]
