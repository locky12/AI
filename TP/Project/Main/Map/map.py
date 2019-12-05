import pygame
from pygame.locals import *
import constante as const
# import feuRouge as FR
tailleCase = 50
COUNT = 0
class Map :

    class Case:
        def __init__ (self,char):
            self.char = char
            self.x = 0
            self.y = 0
            self.caseX = 0
            self.caseY = 0
            self.signalisation = None

    def __init__ (self):
        self.matrix = 0
        self.positionX = 0
        self.positionY = 0
        self.images = dict()


    def genereMap (self) :

        with open("./Data/Map/map.txt", "r") as file:
            struct = []
            for row in file :
                row_struct = []
                for s in row:
                    if s != "\n" :
                        case = self.Case(s)
                        row_struct.append(case)
                struct.append(row_struct)

        self.matrix = struct


        # print(contenu)
    # charge les images et affiches les images
    def initDict(self):
        herbe = pygame.image.load("./Data/Images/herbe.jpg").convert()
        herbe = pygame.transform.scale(herbe, (1900, 1000))

        self.images["herbe"] = herbe

        eau = pygame.image.load("./Data/Images/eau.jpg").convert()
        self.images["eau"] = eau

        carreNoir = pygame.image.load("./Data/Images/carreNoir.jpg").convert()
        carreNoir = pygame.transform.scale(carreNoir, (tailleCase, tailleCase))
        self.images["carreNoir"] = carreNoir

        building = pygame.image.load("./Data/Images/home.png").convert_alpha()
        building = pygame.transform.scale(building, (tailleCase, tailleCase))
        self.images["building"] = building
        # carrefour
        routeSimple = pygame.image.load("./Data/Images/routeSimple.jpg").convert()
        routeSimple = pygame.transform.scale(routeSimple, (tailleCase, tailleCase))
        self.images["routeSimple"] = routeSimple
        #route horizontal haut
        routeHH = pygame.image.load("./Data/Images/routeHorizontalH.jpg").convert()
        routeHH = pygame.transform.scale(routeHH, (tailleCase, tailleCase))
        self.images["routeHH"] = routeHH
        #route horizontal bas
        routeHB = pygame.image.load("./Data/Images/routeHorizontalB.jpg").convert()
        routeHB = pygame.transform.scale(routeHB, (tailleCase, tailleCase))
        self.images["routeHB"] = routeHB
        #route vertical gauche
        routeVG = pygame.image.load("./Data/Images/routeVerticalG.jpg").convert()
        routeVG = pygame.transform.scale(routeVG, (tailleCase, tailleCase))
        self.images["routeVG"] = routeVG
        # route vertical droite
        routeVD = pygame.image.load("./Data/Images/routeVerticalD.jpg").convert()
        routeVD = pygame.transform.scale(routeVD, (tailleCase, tailleCase))
        self.images["routeVD"] = routeVD


    def viewMap (self, window) :
        # road = pygame.image.load("Images/road.png").convert()
        # road = pygame.transform.scale(road, (50, 50))
        num_row = 0
        window.blit(self.images["herbe"],(self.positionX,self.positionY))
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionX
                y = num_row * const.taille_case + self.positionY


                if case.char == "0" :
                    window.blit(self.images["routeSimple"],(x,y))
                if case.char == "8" :
                    window.blit(self.images["routeHH"],(x,y))
                if case.char == "2" :
                    window.blit(self.images["routeHB"],(x,y))
                if case.char == "4" :
                    window.blit(self.images["routeVG"],(x,y))
                if case.char == "6" :
                    window.blit(self.images["routeVD"],(x,y))
                if case.char == "b" :
                    window.blit(self.images["carreNoir"],(x,y))
                    window.blit(self.images["building"],(x,y))
                if case.char == "_" :
                    window.blit(self.images["carreNoir"],(x,y))
                if case.signalisation != None :
                    case.signalisation.printSignilisation()

                case.x, case.y = x,y
                num_case += 1
            num_row += 1
