import pygame
from pygame.locals import *
import constante as const
import Signilisation.feuRouge as FR
import Signilisation.panneauStop as STOP
import Signilisation.passagePieton as PP

tailleCase = 50
RED = (255,0,0)
GREEN = (0,255,0)
hashmap = { "routeSimple" : "0",
            "routeHH" : "8",
            "routeHB" : "2",
            "routeVD" : "6",
            "routeVG" : "4",
            "building": "b",
            "carreNoir" : "_",
            "feuHH" : "u",
            "feuHB" : "n",
            "feuVD" : "k",
            "feuVG" : "h",
            "pietonHH" : "z",
            "pietonHB" : "w",
            "pietonVD" : "d",
            "pietonVG" : "q",
            "stopHH" : "p",
            "stopHB" : ":",
            "stopVD" : "ù",
            "stopVG" : "l",}

class Map :

    class Case:
        def __init__(self,char):
            self.char = char
            self.type = ""
            self.signalisation = 0

    def __init__(self):
        self.matrix = 0
        self.positionX = -50
        self.positionY = 0
        self.images = dict()
        self.timerFeuRouge = 5000 # = 5 secondes
        self.timerPieton = 2000 # = 2 secondes
        self.__genereMap()

    def viewMap(self, window) :

        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionY
                y = num_row * const.taille_case + self.positionX
                #routes
                if case.char == hashmap["routeSimple"] :
                    window.blit(self.images["routeSimple"],(x,y))

                elif case.char == hashmap["routeHH"] :
                    window.blit(self.images["routeHH"],(x,y))

                elif case.char == hashmap["routeHB"] :
                    window.blit(self.images["routeHB"],(x,y))

                elif case.char == hashmap["routeVG"] :
                    window.blit(self.images["routeVG"],(x,y))

                elif case.char == hashmap["routeVD"] :
                    window.blit(self.images["routeVD"],(x,y))

                elif case.char == hashmap["building"] :
                    window.blit(self.images["carreNoir"],(x,y))
                    window.blit(self.images["building"],(x,y))

                elif case.char == hashmap["carreNoir"] :
                    window.blit(self.images["carreNoir"],(x,y))
                #feux
                elif case.char == hashmap["feuHH"]:
                    window.blit(self.images["routeHH"],(x,y))

                elif case.char == hashmap["feuHB"]:
                    window.blit(self.images["routeHB"],(x,y))

                elif case.char == hashmap["feuVD"]:
                    window.blit(self.images["routeVD"],(x,y))

                elif case.char == hashmap["feuVG"]:
                    window.blit(self.images["routeVG"],(x,y))
                #passages pietons
                elif case.char == hashmap["pietonHH"]:
                    window.blit(self.images["pietonHH"],(x,y))

                elif case.char == hashmap["pietonHB"]:
                    window.blit(self.images["pietonHB"],(x,y))

                elif case.char == hashmap["pietonVD"]:
                    window.blit(self.images["pietonVD"],(x,y))

                elif case.char == hashmap["pietonVG"]:
                    window.blit(self.images["pietonVG"],(x,y))
                #stop
                elif case.char == hashmap["stopHH"]:
                    window.blit(self.images["routeHH"],(x,y))
                    window.blit(self.images["stop"],(x+15,y+15))

                elif case.char == hashmap["stopHB"]:
                    window.blit(self.images["routeHB"],(x,y))
                    window.blit(self.images["stop"],(x+15,y+15))

                elif case.char == hashmap["stopVD"]:
                    window.blit(self.images["routeVD"],(x,y))
                    window.blit(self.images["stop"],(x+15,y+15))

                elif case.char == hashmap["stopVG"]:
                    window.blit(self.images["routeVG"],(x,y))
                    window.blit(self.images["stop"],(x+15,y+15))

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

        self.__drawSignalisations(window)

    def generePassants(self):
        for countR,row in enumerate(self.matrix):
            for countC, case in enumerate(row) :
                if case.type == "pieton" :
                    case.signalisation.generePieton()


    def reverseRedLightsColor(self):
        for countR,row in enumerate(self.matrix):
            for countC, case in enumerate(row) :
                if case.type == "feu" :
                    if case.signalisation.color == RED :
                        case.signalisation.color = GREEN
                    else :
                        case.signalisation.color = RED

    def __drawSignalisations(self, window):
        num_row = 0
        for countR,row in enumerate(self.matrix):
            num_case = 0
            for countC, case in enumerate(row) :
                x = num_case * const.taille_case + self.positionY
                y = num_row * const.taille_case + self.positionX

                if case.type == "feu" :
                    case.signalisation.printFeuRouge(window, x, y)

                if case.type == "pieton":
                    if case.signalisation.passants == 1:
                        window.blit(self.images["pieton"],(x,y))

                case.x, case.y = x,y
                num_case += 1
            num_row += 1

    def __genereMap (self) :
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
        self.__initSignalisations()

    def __initSignalisations(self) :
        for countR,row in enumerate(self.matrix):
            for countC, case in enumerate(row) :
                #feux
                if case.char == hashmap["feuHH"]:
                    case.type = "feu"
                    case.signalisation = FR.FeuRouge(RED)

                if case.char == hashmap["feuHB"]:
                    case.type = "feu"
                    case.signalisation = FR.FeuRouge(RED)

                if case.char == hashmap["feuVD"]:
                    case.type = "feu"
                    case.signalisation = FR.FeuRouge(GREEN)

                if case.char == hashmap["feuVG"]:
                    case.type = "feu"
                    case.signalisation = FR.FeuRouge(GREEN)
                #pietons
                if case.char == hashmap["pietonVG"] or case.char == hashmap["pietonVD"] or case.char == hashmap["pietonHH"] or case.char == hashmap["pietonHB"] :
                    case.type = "pieton"
                    case.signalisation = PP.PassagePieton()
                #stop
                if case.char == hashmap["stopVG"] or case.char == hashmap["stopVD"] or case.char == hashmap["stopHH"] or case.char == hashmap["stopHB"] :
                    case.type = "stop"
                    case.signalisation = STOP.Stop()

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

        #pieton horizontal haut
        self.images["pietonHH"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonHorizontalH.jpg").convert(), (tailleCase, tailleCase))
        #pieton horizontal bas
        self.images["pietonHB"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonHorizontalB.jpg").convert(), (tailleCase, tailleCase))
        #pieton vertical gauche
        self.images["pietonVG"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonVerticalG.jpg").convert(), (tailleCase, tailleCase))
        #pieton vertical droite
        self.images["pietonVD"] = pygame.transform.scale(pygame.image.load("./Data/Images/pietonVerticalD.jpg").convert(), (tailleCase, tailleCase))

        #panneau stop
        self.images["stop"] = pygame.transform.scale(pygame.image.load("./Data/Images/panneauStop.png").convert(), (tailleCase-25, tailleCase-25))
        #pieton
        self.images["pieton"] = pygame.transform.scale(pygame.image.load("./Data/Images/homme.png").convert_alpha(), (tailleCase, tailleCase))
