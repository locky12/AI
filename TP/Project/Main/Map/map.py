import pygame
from pygame.locals import *
import constante as const
import Signilisation.feuRouge as FR
tailleCase = 50
COUNT = 0
RED = (255,0,0)
GREEN = (0,255,0)
class Map :

    class Case:
        def __init__ (self,char):
            self.char = char
            self.x = 0
            self.y = 0
            self.caseX = 0
            self.caseY = 0
            self.signalisation = 0

    def __init__ (self):
        self.matrix = 0
        self.positionX = 0
        self.positionY = 0
        self.images = dict()



    def genereMap (self) :
        self.__initDict()
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
        self.__initRedLightLocation()

    def viewMap (self, window) :
        # road = pygame.image.load("Images/road.png").convert()
        # road = pygame.transform.scale(road, (50, 50))
        window.blit(self.images["herbe"],(self.positionX,self.positionY))

        num_row = 0
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

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

        self.__drawRedLight(window)

    def reverseRedLightsColor(self):
        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionX
                y = num_row * const.taille_case + self.positionY

                if case.signalisation != 0 :
                    if case.signalisation.color == RED :
                        case.signalisation.color = GREEN
                    else :
                        case.signalisation.color = RED

                case.x, case.y = x,y
                num_case += 1
            num_row += 1
            
    def __drawRedLight(self, window):
        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionX
                y = num_row * const.taille_case + self.positionY

                if case.signalisation != 0 :
                    case.signalisation.printFeuRouge(window, x, y)

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

    def __initRedLightLocation(self) :
        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionX
                y = num_row * const.taille_case + self.positionY

                if case.char == "4" and self.matrix[num_row+1][num_case].char == "0":
                    case.signalisation = FR.FeuRouge("RED")
                    case.signalisation.color = RED

                if case.char == "6" and self.matrix[num_row-1][num_case].char == "0":
                    case.signalisation = FR.FeuRouge("RED")
                    case.signalisation.color = RED

                if case.char == "8" and self.matrix[num_row][num_case-1].char == "0":
                    case.signalisation = FR.FeuRouge("RED")
                    case.signalisation.color = GREEN

                if case.char == "2" and self.matrix[num_row][num_case+1].char == "0":
                    case.signalisation = FR.FeuRouge("RED")
                    case.signalisation.color = GREEN

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

    # charge les images et affiches les images
    def __initDict(self):
        self.images["herbe"] = pygame.transform.scale(pygame.image.load("./Data/Images/herbe.jpg").convert(), (1900, 1000))

        self.images["eau"] = pygame.image.load("./Data/Images/eau.jpg").convert()

        self.images["carreNoir"] = pygame.transform.scale(pygame.image.load("./Data/Images/carreNoir.jpg").convert(), (tailleCase, tailleCase))

        self.images["building"] = pygame.transform.scale(pygame.image.load("./Data/Images/home.png").convert_alpha(), (tailleCase, tailleCase))
        # carrefour
        self.images["routeSimple"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeSimple.jpg").convert(), (tailleCase, tailleCase))
        #route horizontal haut
        self.images["routeHH"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeHorizontalH.jpg").convert(), (tailleCase, tailleCase))
        #route horizontal bas
        self.images["routeHB"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeHorizontalB.jpg").convert(), (tailleCase, tailleCase))
        #route vertical gauche
        self.images["routeVG"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeVerticalG.jpg").convert(), (tailleCase, tailleCase))
        # route vertical droite
        self.images["routeVD"] = pygame.transform.scale(pygame.image.load("./Data/Images/routeVerticalD.jpg").convert(), (tailleCase, tailleCase))
